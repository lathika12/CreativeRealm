from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'index.html',{})

def poetry(request):
    return render(request,'poetry.html',{})

def musings(request):
    return render(request,'musings.html',{})

def fiction(request):
    return render(request,'fiction.html',{})

def misc(request):
    return render(request,'misc.html',{})

def sayhi(request):
    return render(request,'sayhi.html',{})
