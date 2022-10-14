from http.client import HTTPResponse
from django.http import HttpResponse

def index(request):
    return HttpResponse("hello world")

def detail(request):
    return HttpResponse("detail page")