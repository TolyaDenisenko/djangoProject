from django import template

from django.db.models import Count, F
from news.models import Category

register = template.Library()

#decoraqtor
@register.simple_tag(name= 'get_list_categories')
def get_categories():
    return Category.objects.all()

@register.inclusion_tag('news/list_categories.html')
def show_categories(arg1="hello", arg2="world"):
    #categories =  Category.objects.all()
   # categories = Category.objects.annotate(cnt=Count('news')).filter(cnt__gt=0)
    categories = Category.objects.annotate(cnt=Count('news',filter=F('news__is_published'))).filter(cnt__gt=0)
    return {"categories" : categories, "arg1":arg1, "arg2":arg2}