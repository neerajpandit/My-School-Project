# Generated by Django 3.2.7 on 2022-07-25 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0005_auto_20220725_2133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passout',
            name='facebook',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='passout',
            name='insta',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='passout',
            name='linked',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='passout',
            name='twitter',
            field=models.CharField(max_length=300),
        ),
    ]