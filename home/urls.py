from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('applications/wizard/', views.wizard, name='wizard'),
]
