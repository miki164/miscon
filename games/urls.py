from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('rent', views.Rent.as_view(), name='rent'),
    path('give-back', views.GiveBackView.as_view(), name='give-back')
]
