from django.shortcuts import render, redirect
from main.models import clients
from django.views import View
from django.contrib.auth import authenticate,login

from main.forms import UserCreationForm

# Create your views here.

# def reg(request):
#     return render(request,'main/reg.html')

class Register(View):
    template_name='registration/register.html'

    def get(self, request):
        context = {
            'form': UserCreationForm()
        }
        return render(request, self.template_name,context)
    
    def post(self,request):
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username,password=password)
            login(request,user)
            return redirect('home')
        context = {
            'form': form
        }
        return render(request, self.template_name, context)

def home(request):
    client = clients.objects.all()
    context = {
        "content":client
    }
    return render(request,'main/user.html')