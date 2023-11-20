from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def test(request):
    return HttpResponse('<h1><marquee>We All Are Welcome<h1><marquee>')
