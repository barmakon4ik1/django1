"""В данном случае мы импортируем класс HttpResponse из стандартного пакета
django.http. Затем определяется функция index(), которая в качестве параметра
получает объект запроса request. Класс HttpResponse предназначен для создания
ответа, который отправляется пользователю. И с помощью выражения return
HttpResponse("Hello world") мы отправляем пользователю строку
"Hello world"""

from django.http import HttpResponse
# from django.shortcuts import render


def hello(request):
    return HttpResponse("<h1>Hello, Alex</h1>")


# В данном случае получаем два заголовка "HTTP_HOST" и "HTTP_USER_AGENT" и запрошенный путь.
def index(request):
    # return render(request, 'index.html')
    host = request.META['HTTP_HOST'] # получаем адрес сервера
    user_agent = request.META['HTTP_USER_AGENT'] # данные браузера
    path = request.path # получаем запрошенный путь

    return HttpResponse(f"""
        <p>Host: {host}</p>
        <p>Path: {path}</p>
        <p>User-Agent: {user_agent}</p>
    """)


def about(request, name, age):
    return HttpResponse(f"""
        <h2>О пользователе</h2>
        <p>Имя: {name}</p>
        <p>Возраст: {age}</p>    
    """)


def contact(request):
    return HttpResponse("<h2>Контакты</h2>")
