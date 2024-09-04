from django.urls import path 
from .import views

urlpatterns = [
   path('',views.index,name='index'),
   path('image/',views.image,name='image'),
   path('video/',views.video,name='video'),
   path('mycustomer/',views.mycustomer,name='mycustomer'),
   path('customervideos/',views.customervideos,name='customervideos'),
   path('services/',views.services,name='services'),
]
