from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from main.models import clients
from django import forms

User = get_user_model()

class UserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields =("username", "full_name")

    def __init__(self, *args, **kwargs):
        super(UserCreationForm,self).__init__(*args, **kwargs)
        fields =("username", "full_name","password1","password2")
        placehold = {
            "username":"Логин",
            "full_name":"Фамилия Имя Отчество",
            "password1":"Пароль",
            "password2":"Повторный ввод пароля",
        }
        for i in fields:
            self.fields[i].widget.attrs.update({'class':'input-box'})
            self.fields[i].widget.attrs.update({'placeholder':placehold[i]})
            self.fields[i].label = ""
            self.fields[i].widget.attrs.update({'label':""})

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
