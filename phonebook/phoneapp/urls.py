from django.urls import path
from . import views
urlpatterns = [
    path('+<str:phonenumber>', views.phonenumber, name='phonenumber'),
    path('<str:name>', views.name, name='name')

]
