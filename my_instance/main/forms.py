from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import *
from django.forms import *

class NewForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["cat"].empty_label = "Категория не выбрана"


    class Meta:
        model = New

        fields = ["title", "posts", "photo", "cat", "slug"]

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название'
            }),
            "posts": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите описание'
            }),
            "photo": FileInput(attrs={
                'class' : 'FileInput',
                'placeholder' : 'Выберите изображение'
            }),
            "cat": Select(attrs={
                'class': 'Select',
                'placeholder' : 'Выберите категорию'
            }),
            "slug": TextInput(attrs={
                'class': 'form-control',
                'placeholder':  "URL"
            })
        }


class ImageForm(ModelForm):
    class Meta:
        model = GalleryImage

        fields = ["image"]

        widgets = {

            "image": FileInput(attrs={
                'class' : 'FileInput',
                'placeholder' : 'Выберите изображение'
            })
        }

class VideoForm(ModelForm):
    class Meta:
        model = Video
        fields = ['url']

class LoginUserForm(forms.Form):
    username = CharField(label='Логин', widget=TextInput(attrs={'class': 'form-input'}))
    password = CharField(label='Пароль', widget=PasswordInput(attrs={'class': 'form-input'}))

class RegisterUserForm(ModelForm):
    username = CharField(label="Логин")
    password = CharField(label="Пароль", widget=PasswordInput)
    # password2 = CharField(label="Повтор пароля", widget=PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']#lastname 'first_name','password2'
        labels = {
            'email': 'E-mail',
            # 'first_name': 'Имя'
            #'last_name': 'Фамилия',
        }