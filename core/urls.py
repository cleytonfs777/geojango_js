from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('mapa/', views.mapa, name='mapa'),

    
]