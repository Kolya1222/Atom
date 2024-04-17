from django.urls import include, path

from main.views import Register,CreateMyModelView

app_name='main'

urlpatterns = [
    path('',include("django.contrib.auth.urls")),
    path('register/', Register.as_view(), name='register'),
    path('abc/',CreateMyModelView.as_view(), name='abc'),
]