from django.http import HttpResponse
from django.shortcuts import render

from .models import Todo


def index(request):
  return render(request, 'my_to_do_app/index.html')


def createTodo(request):
  user_input_str = request.POST['todoContent']
  new_todo = Todo(content=user_input_str)
  new_todo.save()
  return HttpResponse('create Todo를 할 거야! =>' + user_input_str)
