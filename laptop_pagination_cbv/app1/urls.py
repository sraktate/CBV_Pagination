from django.urls import path
from .views import Home_view,Laptop_add_view, LaptopListView

urlpatterns=[
    path('home/',Home_view,name='home'),
    path('laptopadd/',Laptop_add_view,name='laptopadd'),
    path('laptopshow/',LaptopListView.as_view(),name='laptopshow'),
]