from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST, require_http_methods
import json
from projects.models import Project, ProjectDetail

@csrf_exempt
@require_POST
def create_project(request):
    data = json.loads(request.body)
    new_project = Project.objects.create(
        name=data['name'],
        description=data.get('description', ''),
    )
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
    project_name = project.name
    # Qui scatta il CASCADE: cancella Task, TaskDetail e ProjectDetail
    project.delete() 
    return JsonResponse({"message": f"Project '{project_name}' and all associated data deleted!"})

@csrf_exempt
@require_POST
def add_project_details(request):
    try:
        data = json.loads(request.body)
        detail = ProjectDetail.objects.create(
            project_id=data['project_id'],
            client_name=data.get('client_name', ''),
            start_date=data.get('start_date')
        )
        return JsonResponse({"message": "Project details added!", "detail_id": detail.id})
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)