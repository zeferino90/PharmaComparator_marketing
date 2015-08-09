from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def hello_world(request):
    return HttpResponse("Hello catalonia <br/> <a href='/product/test2/'>test2</a>")

def test2(request):
    return render(request, 'product/index.html')