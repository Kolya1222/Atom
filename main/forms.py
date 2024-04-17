from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from main.models import clients
from django import forms

User = get_user_model()

class UserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields =("username", "full_name") 

class MyModelForm(forms.ModelForm):
    class Meta:
        model = clients
        fields = [
        "id_score",
        "first_name","middle_name","last_name",
        "date_birth",
        "inn",
        "user",
        "status",
        ]