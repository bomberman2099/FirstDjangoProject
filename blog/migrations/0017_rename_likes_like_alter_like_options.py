# Generated by Django 4.2.4 on 2023-10-12 16:51

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0016_alter_contactus_options_likes'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Likes',
            new_name='Like',
        ),
        migrations.AlterModelOptions(
            name='like',
            options={'ordering': ('created_at',), 'verbose_name': 'لایک', 'verbose_name_plural': 'لایک ها'},
        ),
    ]