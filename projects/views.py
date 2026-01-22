from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST, require_http_methods
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

@require_http_methods(["GET"])
def list_projects(request):
    projects = Project.objects.all()
    data = [{"id": p.id, "name": p.name, "description": p.description} for p in projects]
    return JsonResponse({"projects": data})

@csrf_exempt
@require_http_methods(["DELETE"])
def delete_project(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    project.delete()
    return JsonResponse({"message": f"Project {project_id} and all its tasks deleted!"})