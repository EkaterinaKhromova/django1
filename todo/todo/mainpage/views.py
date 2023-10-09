from django.shortcuts import render

# всё, что ниже - написано вручную!
from django.http import HttpResponse

#  традиционно главная функция страницы называется index (как перечень)
#  она принимает в качестве аргумента объект HttpRequest
def index (request):
    return render(
        request,
        'mainpage/index.html'
)

def page (*a, **b):
    return HttpResponse('<h1>privet</h1>')