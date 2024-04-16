from django.urls import path

from main import views

app_name='main'

urlpatterns = [
    path('', views.index, name='index'),
    path('reg/', views.reg, name='reg'),
    path('user/', views.user, name='user')
]