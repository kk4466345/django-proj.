from django.http import HttpResponse
from django.shortcuts import render
def homepage(request):
    return render(request,"home.html")

def count(request):
    data = request.GET['fulltextarea']
    return render(request, 'count.html', {'fulltext':data})

def about(request):
    return render(request, "about.html")
