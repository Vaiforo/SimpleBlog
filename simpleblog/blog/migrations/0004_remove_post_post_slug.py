# Generated by Django 5.0.7 on 2024-07-25 17:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_rename_slug_post_post_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='post_slug',
        ),
    ]
