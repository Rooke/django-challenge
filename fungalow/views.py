from django.shortcuts import render
from .models import Home

def home_list(request):
    return JsonResponse(list(Home.objects.values()), safe=False)

