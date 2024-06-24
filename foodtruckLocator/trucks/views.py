

from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import FoodTruck
from .serializers import FoodTruckSerializer
from django.contrib.auth.mixins import LoginRequiredMixin


#view to retun 5 suggested food trucks nearby
class FoodTruckList(generics.ListAPIView,LoginRequiredMixin):
    serializer_class = FoodTruckSerializer

    def get_queryset(self):
        latitude = self.request.query_params.get('latitude')
        longitude = self.request.query_params.get('longitude')
        if latitude and longitude:
            latitude = float(latitude)
            longitude = float(longitude)
            # Filter logic (e.g., simple bounding box for proximity)
            return FoodTruck.objects.filter(
                latitude__gte=latitude - 0.01,
                latitude__lte=latitude + 0.01,
                longitude__gte=longitude - 0.01,
                longitude__lte=longitude + 0.01
            )[:5]
        
        return FoodTruck.objects.none()
    
def index(request):
    return render(request, 'trucks/index.html')

