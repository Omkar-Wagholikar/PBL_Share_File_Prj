# Generated by Django 4.1.7 on 2023-03-26 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='files',
            name='file_name',
        ),
        migrations.RemoveField(
            model_name='files',
            name='keywords',
        ),
        migrations.AddField(
            model_name='files',
            name='file',
            field=models.FileField(default='', upload_to=''),
        ),
    ]
