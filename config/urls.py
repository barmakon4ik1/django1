"""Первой строкой из модуля django.contrib импортируется класс AdminSite,
который предоставляет возможности работы с интерфейсом администратора.
Второй строкой из модуля django.urls импортируется функция path.
Эта функция задает сопоставление определенного маршрута с функцией обработки.
Так, в данном случае маршрут "admin/" будет обрабатываться методом admin.site.urls."""
from django.urls import path, re_path
from myApp import views


"""Чтобы использовать функцию views.index вначале импортируем модуль views. 
Затем определяем сопоставление маршрута ' ' и функции views.index и также 
дополнительно имя для маршрута: name='home'. 
По сути маршрут ' ' будет сопоставляться с запросом к корню приложения.

Преимущество re_path состоит в том, что она позволяет задать адреса URL с 
помощью регулярных выражений."""
urlpatterns = [
    # path('', views.index),
    re_path(r'^hello', views.hello),
    path('', views.index, name='index'),
    re_path(r'^about/contact', views.contact),
    re_path(r'^about', views.about, kwargs={'name': 'Alexander', 'age': 54}),
    path('index', views.index),
]
