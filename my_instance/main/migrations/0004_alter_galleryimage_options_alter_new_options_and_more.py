# Generated by Django 4.2.2 on 2023-11-15 06:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_video'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='galleryimage',
            options={'permissions': (('can_upload_image', 'upload_image'),)},
        ),
        migrations.AlterModelOptions(
            name='new',
            options={'permissions': (('can_create', 'create'),), 'verbose_name': 'Статья', 'verbose_name_plural': 'Статьи'},
        ),
        migrations.AlterModelOptions(
            name='video',
            options={'permissions': (('can_add_video', 'add_video'),)},
        ),
    ]
