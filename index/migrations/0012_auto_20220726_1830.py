# Generated by Django 3.2.7 on 2022-07-26 13:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0011_auto_20220726_1818'),
    ]

    operations = [
        migrations.RenameField(
            model_name='passout',
            old_name='passout_imgage',
            new_name='passout_image',
        ),
        migrations.RenameField(
            model_name='student10',
            old_name='s_image',
            new_name='s10_image',
        ),
    ]