from django.shortcuts import render


def index(request):
  return render(request, 'my_to_do_app/index.html')
