from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:page>/', views.index, name='index'),
    path('work/<int:pk>/', views.detail, name='detail')
]