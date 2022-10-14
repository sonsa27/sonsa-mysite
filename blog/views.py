from http.client import HTTPResponse
from django.http import HttpResponse

def index(request):
    return HTTPResponse("hello world")

def detail(request):
    return HttpResponse("detail page")