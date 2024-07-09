from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import UmraTour
from .serializers import UmraTourSerializer
from rest_framework.permissions import IsAuthenticated

class UmraTourViewSet(viewsets.ModelViewSet):
    queryset = UmraTour.objects.all()
    serializer_class = UmraTourSerializer
    permission_classes = [IsAuthenticated]
