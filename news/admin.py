from venv import create

from django.contrib import admin

from .models import News

# Register your models here.
from .models import News

class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'updated_at', 'is_published')

admin.site.register(News, NewsAdmin)
