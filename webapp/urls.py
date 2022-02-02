from django.urls import path,include
from webapp import views
from webapp.models import *
urlpatterns = [

    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('products/', views.products, name='products'),
    path('analogmen/', views.analogmen, name='analogmen'),
    path('analogwomen/', views.analogwomen, name='analogwomen'),
    path('registration/', views.registration, name='registration'),
    path('loginh/', views.loginh, name='loginh'),

    path('logouth/', views.logouth, name='logouth'),
    path('buy1/', views.buy1, name='buy1'),
    path('buy2/', views.buy2, name='buy2'),
    path('buy3/', views.buy3, name='buy3'),
    path('buy4/', views.buy4, name='buy4'),
    path('buy5/', views.buy5, name='buy5'),
    path('buy6/', views.buy6, name='buy6'),
    path('buy7/', views.buy7, name='buy7'),
    path('buy8/', views.buy8, name='buy8'),
    path('buy9/', views.buy9, name='buy9'),
    path('buy10/', views.buy10, name='buy10'),
    path('buy11/', views.buy11, name='buy11'),
    path('buy12/', views.buy12, name='buy12'),
    path('buy13/', views.buy13, name='buy13'),
    path('buy14/', views.buy14, name='buy14'),
    path('buy15/', views.buy15, name='buy15'),
    path('buy16/', views.buy16, name='buy16'),

]