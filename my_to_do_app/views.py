from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Todo


def index(request):
  todos = Todo.objects.all()
  content = {'todos': todos}
  return render(request, 'my_to_do_app/index.html', content)


def createTodo(request):
  user_input_str = request.POST['todoContent']
  new_todo = Todo(content=user_input_str)
  new_todo.save()
  return HttpResponseRedirect(reverse('index'))
