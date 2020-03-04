from django.http import HttpResponse


def index(request):
  return HttpResponse('my_to_do_app first page')
