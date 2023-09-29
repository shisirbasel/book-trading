from django.shortcuts import render

# Create your views here.
def login(request):
    context={

    }
    return render(request,"signup.html",context)

def register(request):
    context={

    }
    return render(request,"login.html",context)

def home(request):
    context={

    }
    return render(request,"index.html",context)