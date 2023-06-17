from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Car
from .serializers import CarTelematicsSerializer
from django.http import JsonResponse

class CarTelematicsView(APIView):
    serializer_class = CarTelematicsSerializer

    def get(self, request, *args, **kwargs):
        cars = Car.objects.all()
        serializer = CarTelematicsSerializer(cars, many=True)
        return Response(serializer.data)

def dashboard(request):
    car_vins = Car.objects.values_list('vin', flat=True).distinct()
    return render(request, 'telematics/index.html', {'car_vins': car_vins})

def car_data(request, vin):
    car_data = Car.objects.filter(vin=vin).order_by('timestamp')
    car_list = list(car_data.values()) 
    return JsonResponse(car_list, safe=False)
