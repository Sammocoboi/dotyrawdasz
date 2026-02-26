from .serializers import CarSerializer,FirmSerializer
from rest_framework import viewsets
from .models import Car,Firm
class CarViews(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
class FirmViews(viewsets.ModelViewSet):
    queryset = Firm.objects.all()
    serializer_class = FirmSerializer
    