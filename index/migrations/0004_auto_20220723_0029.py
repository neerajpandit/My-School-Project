# Generated by Django 3.2.7 on 2022-07-22 18:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0003_rename_timg_timage_photo'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Timage',
            new_name='Image',
        ),
        migrations.RenameField(
            model_name='image',
            old_name='photo',
            new_name='new_image',
        ),
    ]