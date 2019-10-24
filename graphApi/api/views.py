from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'pages/index.html')

def cat(request,pk):
    data={
        'pk':pk
    }
    return render(request,'pages/ingrediant.html',data)

def detail(request):
    return render(request,'pages/detail.html')