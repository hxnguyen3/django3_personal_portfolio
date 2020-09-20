from django.urls import path
from . import views

app_name = 'blog' #Name of app. Useful bc if you have multiple detail pages, django needs to know which to use

urlpatterns = [
    path('', views.all_blogs, name = 'all_blogs'),
    path('<int:blog_id>/', views.detail, name = 'detail'),
]