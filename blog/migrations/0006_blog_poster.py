# Generated by Django 5.1.2 on 2024-11-21 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_blog_genre'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='poster',
            field=models.CharField(default='', max_length=250),
        ),
    ]
