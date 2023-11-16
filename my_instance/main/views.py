from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.core.paginator import Paginator
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from .models import New, Category, GalleryImage, Video
from .forms import NewForm, ImageForm, VideoForm, RegisterUserForm, LoginUserForm


def index(request):
    posts = New.objects.all()
    paginator = Paginator(posts, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    cats = Category.objects.all()
    return render(request, 'main/index.html', {'page_obj': page_obj, 'title':'Главная страница сайта', 'posts': posts, 'cat_selected': 0, 'cats': cats})

def about(request):
    return render(request, 'main/about.html')
@permission_required('catalog.can_create')
@login_required
def create(request):
    if not request.user.is_authenticated:
        return "Зарегистрируйтесь, чтобы создать статью"
    if request.method == 'POST':
        form = NewForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма была неверной'

    form = NewForm()
    context = {
        'form': form
    }
    return render(request, 'main/create.html', context)

# def login(request):
#     return render(request, 'main/login.html')

def show_post(request, post_slug):
    post = get_object_or_404(New, slug=post_slug)

    context = {

        'post': post,
        'title': post.title,
        'cat_selected': post.cat_id,
    }
    return render(request, 'main/post.html', context=context)


def show_category(request, cat_id):
    posts = New.objects.filter(cat_id=cat_id)
    # post_for = New.objects.all()
    paginator = Paginator(posts, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    cats = Category.objects.all()
    if len(posts) == 0:
        raise Http404()

    context = {
        'page_obj': page_obj,
        'posts': posts,
        'cats': cats,
        'title': 'Виды походов',
        'cat_selected': cat_id,
    }

    return render(request, 'main/index.html', context=context)

def gallery_view(request):
    images = GalleryImage.objects.all()
    return render(request, 'main/gallery.html', {'images': images})

@permission_required('catalog.can_upload_image')
@login_required
def upload_image(request):
    if not request.user.is_authenticated:
        return "Зарегистрируйтесь, чтобы создать статью"
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  # Сохранение изображения в модель
            return redirect('gallery')  # Перенаправление на страницу галереи
    else:
        form = ImageForm()
    return render(request, 'main/upload_image.html', {'form': form})

def video_page(request):
    video_url = Video.objects.all()  # URL-адрес вашего видео
    # context = {
    #     'video_url': video_url
    # }
    vid = []
    for video in video_url:
        video1 = "https://www.youtube.com/embed/"+str(video.url.split('=')[1])
        vid.append(video1)
    context = {
        'vid' : vid,
        'video_url': video_url
        }
    return render(request, 'main/video.html', context)
@permission_required('catalog.can_add_video')
@login_required
def add_video(request):
    if request.method == 'POST':
        form = VideoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('video')  # перенаправление на страницу со списком видео
    else:
        form = VideoForm()
    return render(request, 'main/add_video.html', {'form': form})

# def login(request):
#     form = UserCreationForm()
#     return render(request, 'main/login.html', {'form': form})

def login_user(request):
    if request.method == 'POST':
        form = LoginUserForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user and user.is_active:
                login(request, user)
                return HttpResponseRedirect('login')
    else:
        form = LoginUserForm()
    return render(request, 'main/login.html', {'form': form})

def logout_user(request):
    logout(request)
    return HttpResponseRedirect('login')

def register(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save() #(commit=False)  # создание объекта без сохранения в БД
            user.set_password(form.cleaned_data['password'])
            user.save()
            return render(request, 'main/register_done.html')
    else:
        form = RegisterUserForm()
    return render(request, 'main/register.html', {'form': form})