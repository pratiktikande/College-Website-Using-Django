from django.contrib import admin
from django.urls import path ,include
from . import views

urlpatterns = [
    path('' ,views.index,name='index'),
    path('about/' ,views.about,name='about us'),
    path('contact/' ,views.contact,name='contact us'),
    path('tracker/' ,views.tracker,name='tracker'),
    path('search/' ,views.search,name='search'),
    path('products/<int:myid>' ,views.productview,name='productview'),
    path('checkout/' ,views.checkout,name='checkout'),
]