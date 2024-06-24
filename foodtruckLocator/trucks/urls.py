from django.urls import path
from .views import FoodTruckList, index

urlpatterns = [
    path('trucks/api/foodtrucks/', FoodTruckList.as_view(), name='foodtruck-list'),
    path('trucks/', index, name='index'),
]
