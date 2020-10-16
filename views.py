import requests
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    index_html = open("content/index.html").read()
    context = {
    "content": index_html,
    "title": "Home",
    }
    return render(request,"base.html", context)

def blog(request):
    blog_html = open("content/blog.html").read()
    context = {
    "content": blog_html,
    "title": "Blog",
    }
    return render(request, "base.html", context)


def purchase(request):
    purchase_html = open("content/purchase.html").read()
    context = {
    "content": purchase_html,
    "title": "Purchase"
    }
    return render(request, "base.html", context)


