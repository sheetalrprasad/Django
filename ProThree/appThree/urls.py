from django.urls import path
from appThree import views

urlpatterns = [
    path('',views.users,name='users'),
]
