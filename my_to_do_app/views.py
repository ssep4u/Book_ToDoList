from django.http import HttpResponse
from django.shortcuts import render


def index(request):
  return render(request, 'my_to_do_app/index.html')


def createTodo(request):
  user_input_str = request.POST['todoContent']
  return HttpResponse('create Todo를 할 거야! =>' + user_input_str)
