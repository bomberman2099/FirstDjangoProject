# Generated by Django 4.2.4 on 2023-10-12 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_rename_likes_like_alter_like_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='like',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
    ]
