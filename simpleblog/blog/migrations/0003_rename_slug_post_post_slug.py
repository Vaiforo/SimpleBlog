# Generated by Django 5.0.7 on 2024-07-25 15:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_post_options_post_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='slug',
            new_name='post_slug',
        ),
    ]