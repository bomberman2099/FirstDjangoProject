# Generated by Django 4.2.4 on 2023-09-28 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_a'),
    ]

    operations = [
        migrations.DeleteModel(
            name='a',
        ),
        migrations.AddField(
            model_name='profile',
            name='email',
            field=models.EmailField(default='a', max_length=254),
        ),
        migrations.AddField(
            model_name='profile',
            name='first_name',
            field=models.CharField(default='a', max_length=30),
        ),
        migrations.AddField(
            model_name='profile',
            name='last_name',
            field=models.CharField(default='a', max_length=150),
        ),
        migrations.AddField(
            model_name='profile',
            name='username',
            field=models.CharField(default='a', max_length=150),
        ),
    ]