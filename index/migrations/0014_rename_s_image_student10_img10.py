# Generated by Django 3.2.7 on 2022-07-26 13:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0013_rename_s10_image_student10_s_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student10',
            old_name='s_image',
            new_name='img10',
        ),
    ]
