from django.urls import path
from .import views

urlpatterns = [
    path('',views.index, name='home'),
    # path('admin',contrib.admin, name='admin'),
    path('about-us',views.about, name='about'),
    path('create',views.create, name='create'),
    path('upload_image',views.upload_image, name='upload_image'),
    path('gallery',views.gallery_view, name='gallery'),
    path('video', views.video_page, name='video'),
    path('add_video/', views.add_video, name='add_video'),
    path('post/<slug:post_slug>/',views.show_post, name='post'),
    path('category/<int:cat_id>/',views.show_category, name='category'),
    path('login', views.login_user, name='login'),
    path('logout', views.logout_user, name='logout'),
    path('register/', views.register, name='register'),
]
