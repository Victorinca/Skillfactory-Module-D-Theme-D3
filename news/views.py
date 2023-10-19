# from django.shortcuts import render
from django.utils import timezone
from datetime import datetime
# импортируем класс, говорящий о том, что в этом представлении будем выводить список объектов из БД
from django.views.generic import ListView, DetailView
from .models import Post


# Create your views here.
class PostsList(ListView):
# указываем модель, объекты которой мы будем выводить
    model = Post
# указываем имя шаблона, в котором будет лежать HTML,
# в нём будут все инструкции о том, как именно пользователю должны вывестись наши объекты
    template_name = 'news/newslist.html'
# далее имя списка (по заданию нужно 'news'), в котором будут лежать все объекты,
# его надо указать, чтобы обратиться к самому списку объектов через HTML-шаблон
    context_object_name = 'news'
# вывод объектов в обратном порядке, начиная с последнего созданного объекта
#    queryset = Post.objects.all().order_by('-id')
    queryset = Post.objects.all().order_by('-postCreated')

# создаём представление, в котором будут детали конкретного отдельного поста
class PostDetail(DetailView):
    model = Post  # модель всё та же, но мы хотим получать детали конкретно отдельного поста
    template_name = 'news/post.html'  # название шаблона будет post.html
    context_object_name = 'post'  # название объекта
