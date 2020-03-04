from django.http import HttpResponse
from django.shortcuts import render


def index(request):
  return render(request, 'my_to_do_app/index.html')


def createTodo(request):
  return HttpResponse('create Todo를 할 거야!')