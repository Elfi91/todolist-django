from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
import json

from projects.models import Project

# Create your views here.

@csrf_exempt
@require_POST
def create_project(request):
    # 1. Leggiamo i dati inviati da Postman
    data = json.loads(request.body)
        
    # 2. Creiamo l'istanza del modello
    new_project = Project.objects.create(
        name=data['name'],
        description=data.get('description', ''),
    )
        
    # 3. Rispondiamo a Postman che è andata bene
    return JsonResponse({"message": "Progetto creato!", "id": new_project.id})