from django.urls import path
from . import views

urlpatterns = [
   path('get_number/', views.getNumber.as_view()),
   path('check_number/', views.checkToken.as_view()),
   path('singin/', views.singin.as_view()),
   path('register/', views.register.as_view()) 
]
