from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
import json

from tasks.models import Task

# Create your views here.

@csrf_exempt
@require_POST
def create_task(request):
    # 1. Leggiamo i dati inviati da Postman
    data = json.loads(request.body)

    project_id = data.get('project')
        
    # 2. Creiamo l'istanza del modello
    new_task = Task.objects.create(
        title=data['title'],
        project_id=project_id
    )
        
    # 3. Rispondiamo a Postman che è andata bene
    return JsonResponse({"message": "Task aggiunta!", "id": new_task.id})