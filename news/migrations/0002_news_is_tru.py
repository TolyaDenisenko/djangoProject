# Generated by Django 4.0 on 2024-12-18 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='is_tru',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
