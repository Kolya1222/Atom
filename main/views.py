from django.shortcuts import render,redirect
from main.models import clients
from django.views import View
from django.contrib.auth import authenticate,login
from django.views.generic.edit import CreateView

from main.forms import UserCreationForm,MyModelForm

class Register(View):
    template_name='registration/register.html'

    def get(self, request):
        context = {
            'form': UserCreationForm()
        }
        return render(request, self.template_name,context)
    
    def post(self,request, *args, **kwargs):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username,password=password)
            login(request,user)
            return redirect('home')
        context = {
            'form': form,
            'title':"Привет"
        }      
        return render(request, self.template_name, context)

def home(request):
    context = {}
    if request.user.is_authenticated:
        name=request.user.full_name
        client = clients.objects.filter(user=name)
        context = {
            "context":client,
            "text":name
        }
    return render(request,'main/user.html',context)

class CreateMyModelView(CreateView):
    model = clients
    form_class = MyModelForm
    template_name = 'main/test.html'
    success_url = "/"
