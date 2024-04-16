from django.shortcuts import render
from main.models import clients

# Create your views here.
def index(request):
    return render(request,'main/index.html')

def reg(request):
    return render(request,'main/reg.html')

def user(request):
    client = clients.objects.all()
    context = {
        "content":client
    }
    return render(request,'main/user.html')