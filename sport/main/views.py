from django.shortcuts import render
from .models import * 

# Create your views here.
def index(request):
    posts = Sport.objects.all()
    return render(request, 'main/index.html', {'sss': posts})

def newproject(request):
    var = MenPrize.objects.all()
    return render(request, 'main/newproject.html', {'var': var})

def login(request):
    return render(request, 'main/login.html')



def men(request):
    inf = Men.objects.all() 
    
    return render(request, 'main/men.html',{'inf': inf})     




def women(request):
    infw = Women.objects.all()
    return render(request, 'main/women.html',{'infw': infw})

def index2(request):
    return render(request,'main/index2.html')   
