from lib2to3.fixes.fix_input import context

from django.contrib.admin.templatetags.admin_list import pagination
from django.shortcuts import render , get_object_or_404, redirect
from django.http import HttpResponse
from django.template.defaultfilters import title
from unicodedata import category
from .utils import MyMixin
from django.core.paginator import Paginator
from .models import News,Category
from .forms import NewsForm, UserRegisterForm, UserLoginForm
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import login, logout

# def test(request):
#    objects = ['jonh1','pol2','sem3','willy4','george5','phillip6','masters7',]
#    paginator = Paginator(objects,2)
#    page_num = request.GET.get('page',1)
#    page_objects = paginator.get_page(page_num)
#    return render (request, 'news/test.html',{'page_obj':page_objects})


def register(request):
   if request.method == 'POST':
      form = UserRegisterForm(request.POST)
      if form.is_valid():
         user = form.save()
         login(request, user)
         messages.success(request,'Вы успешно зарагистровались')
         return redirect('login')
   else:
      messages.error(request, 'Ошибка регистрации')
      form = UserRegisterForm()

   return render(request, 'news/register.html', {"form":form})


def user_login(request):
   if request.method == 'POST':
      form = UserLoginForm(data=request.POST)
      if form.is_valid():
         user = form.get_user()
         login(request, user)
         return redirect('home')

   else:
      form = UserLoginForm()
   return render(request, 'news/login.html', {"form": form})

def user_logout(request):
   logout(request)
   return redirect('login')

class HomeNews(MyMixin,ListView):
   model = News
   template_name = 'news/home_news_list.html'
   context_object_name = 'news'
   extra_context = {'title': 'Главная'}
   mixin_prop = 'hello world Mixin Prop'
   paginate_by = 5 #параметр разбития на страницы

   def get_context_data(self, *, object_list=None, **kwargs):
      context = super().get_context_data(**kwargs)
      context['title'] = self.get_upper('Главная Страница')
      context['mixin_prop'] = self.get_prop()
      return context

   def get_queryset(self):
      return News.objects.filter(is_published=True).select_related('category')



class NewsByCategory(MyMixin,ListView):
   model = News
   template_name = 'news/home_news_list.html'
   context_object_name = 'news'
   allow_empty = False
   paginate_by = 3

   def get_context_data(self, *, object_list=None, **kwargs):
      context = super().get_context_data(**kwargs)
      context['title'] =self.get_upper( Category.objects.get(pk=self.kwargs['category_id']))
      return context

   def get_queryset(self):
      return News.objects.filter(category_id=self.kwargs['category_id'],is_published=True).select_related('category')


class ViewNews (DetailView):
   model = News
   context_object_name = 'news_item'
   #template_name = 'news/news_detail.html'
   # pk_url_kwarg = 'news_id'


class CreateNews(LoginRequiredMixin,CreateView):
   form_class = NewsForm
   template_name = 'news/add_news.html'
   # success_url = reverse_lazy('home')
   login_url = '/admin/'
   raise_exception = True

# Create your views here.

# def index(request):
#    news = News.objects.all()
#
#    context = {
#       'news':news,
#       'title': 'Список новостей',
#
#    }
#    return render(request,template_name='news/index.html', context=context)

# def get_category(request, category_id):
#
#    news = News.objects.filter(category_id=category_id)
#    category = Category.objects.get(pk=category_id)
#    return render(request,'news/category.html', {'news': news,  'category':category})

# def view_news(request, news_id):
#    #news_item = News.objects.get(pk=news_id)
#    news_item=get_object_or_404(News,pk=news_id)
#    return render(request,'news/view_news.html', {"news_item":news_item})

# def add_news(request):
#    if request.method == 'POST':
#       form = NewsForm(request.POST)
#       if form.is_valid():
#          # print(form.cleaned_data)
#         #news = News.objects.create(**form.cleaned_data)
#          news = form.save()
#          return redirect(news)
#    else:
#       form = NewsForm()
#    return render(request, 'news/add_news.html', {'form': form})