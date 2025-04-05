from django.db import models
from django.template.defaultfilters import title
from django.urls import reverse


class News(models.Model):
    title = models.CharField(max_length=150, verbose_name='Наименование')
    content = models.TextField(blank=True, verbose_name='Контент')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата Публикации')
    updated_at = models.DateTimeField(auto_now=True , verbose_name='Обновлено')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True, verbose_name='Фото')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    category = models.ForeignKey('Category', verbose_name='Категория',on_delete=models.PROTECT)
    def get_absolute_url(self):
        return reverse('view_news', kwargs={'news_id': self.pk})

    # def my_func(self):
    #     return 'Hello from model'



    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural  = "Новости"
        ordering  = ['-created_at']

class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Наименование Категории')
    class Meta:
        verbose_name = "Категория"
        verbose_name_plural  = "Категории"
        ordering  = ['title']

    def get_absolute_url(self):
        return reverse('category', kwargs={'category_id': self.pk})
    def __str__(self):
        return self.title
