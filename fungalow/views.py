from .models import Home
from .serializers import HomeSerializer
from rest_framework import generics

class HomeList(generics.ListCreateAPIView):
    queryset = Home.objects.all()
    serializer_class = HomeSerializer

