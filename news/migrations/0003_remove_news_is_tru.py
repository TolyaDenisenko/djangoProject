# Generated by Django 4.0 on 2024-12-18 13:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_news_is_tru'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='is_tru',
        ),
    ]
