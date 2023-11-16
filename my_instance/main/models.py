from django.db import models
from django.urls import reverse


class New(models.Model):
    title = models.CharField('Название', max_length=50)
    posts = models.TextField('Описание')
    slug = models.SlugField(unique=True, max_length=255, db_index=True, verbose_name="URL")
    photo = models.ImageField(upload_to="photos/", verbose_name="Фото")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Время изменения")
    is_published = models.BooleanField(default=True, verbose_name="Публикация")
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name="Категории")
    objects = models.Manager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        permissions = (("can_create", "create"),)

class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name="Категория")
    slug = models.SlugField(unique=True, max_length=255, db_index=True, verbose_name="URL")
    objects = models.Manager()
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_id': self.pk})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['id']

class GalleryImage(models.Model):
    image = models.ImageField(upload_to='gallery/')
    class Meta:
        permissions = (("can_upload_image", "upload_image"),)

class Video(models.Model):
    url = models.URLField()
    class Meta:
        permissions = (("can_add_video", "add_video"),)

