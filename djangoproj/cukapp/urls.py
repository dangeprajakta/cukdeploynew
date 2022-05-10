from django.contrib import admin
from django.urls import path
from . import views
from .views import home_view


urlpatterns = [
   # path('', views.home_view),
    #path('newpage/', views.new_page, name="my_function")
    path('',home_view),
   # path('newpage/', views.new_page, name="newpage")
]
