from django import views
from django.urls import path
from . import views

urlpatterns=[
    path('', views.home),
    path('registarCurso/', views.registarCurso),
    path('eliminacionCurso/<codigo>', views.eliminarCurso),
    path('edicionCurso/<codigo>', views.edicionCurso),
    path('editarCurso/', views.editarCurso),
]