from django.urls import path
from .views import CarTelematicsView, dashboard, car_data

urlpatterns = [
    path('api/cars/', CarTelematicsView.as_view(), name='home'),
    path('dashboard/', dashboard, name='dashboard'),
    path('car_data/', car_data, name='car_data'),
]
