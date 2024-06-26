from django.shortcuts import render
from django.http import HttpResponse

# 메인페이지
def index(request):
    return HttpResponse('Hello World')
