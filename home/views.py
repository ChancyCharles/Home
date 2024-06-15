from django.shortcuts import render

# Create your views here.
def home(request):

    return render(request,"home.html",{"home":home})

def form(request):

    return render(request,"form.html",{"form":form})


def login(request):

    return render(request,"login.html",{"login":login})