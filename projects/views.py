"""
Project Views.
Logic for creating, listing, and filtering projects by deadline.
"""

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST, require_http_methods
from django.utils import timezone
from datetime import timedelta
import json

from .models import Project, ProjectDetail
from core.utils import error_response

@csrf_exempt
@require_POST
def create_project(request):
    """Creates a new project from JSON input."""
    try:
        data = json.loads(request.body)
        
        # We enforce the presence of 'name' at the application level.
        if 'name' not in data or not data['name']:
            return error_response("Missing name", "The 'name' field is required.", 400)
            
        project = Project.objects.create(
            name=data['name'],
            description=data.get('description', ''),
            deadline=data.get('deadline')
        )
        return JsonResponse({
            "status": "success", 
            "message": "Project created successfully", 
            "id": project.id
        }, status=201)

    except json.JSONDecodeError:
        return error_response("Invalid JSON", "Could not parse the request body.", 400)
    except Exception as e:
        return error_response("Server Error", str(e), 500)

@require_http_methods(["GET"])
def list_projects(request):
    """Returns a list of all existing projects."""
    projects = Project.objects.all()
    if not projects.exists():
        return error_response("Not Found", "No projects found in the database.", 404)
        
    data = [{
        "id": p.id, 
        "name": p.name, 
        "description": p.description, 
        "deadline": p.deadline
    } for p in projects]
    
    return JsonResponse({"status": "success", "projects": data})

@csrf_exempt
@require_http_methods(["DELETE"])
def delete_project(request, project_id):
    """Removes a project and its associated details via CASCADE."""
    try:
        project = Project.objects.get(id=project_id)
        project.delete() 
        return JsonResponse({
            "status": "success", 
            "message": f"Project {project_id} deleted."
        })
    except Project.DoesNotExist:
        return error_response("Not Found", "Project ID does not exist.", 404)

@require_http_methods(["GET"])
def get_expiring_projects(request):
    """
    Returns projects due within the next 7 days.
    Useful for dashboard notifications.
    """
    today = timezone.now().date()
    window = today + timedelta(days=7)
    
    expiring = Project.objects.filter(
        deadline__range=[today, window]
    ).order_by('deadline')

    if not expiring.exists():
        return error_response("No Deadlines", "No projects expiring soon.", 404)

    results = [{
        "id": p.id,
        "name": p.name,
        "deadline": p.deadline,
        "days_left": (p.deadline - today).days
    } for p in expiring]

    return JsonResponse({"status": "success", "results": results})

@csrf_exempt
@require_POST
def add_project_details(request):
    """Links metadata to an existing project (1:1 relationship)."""
    try:
        data = json.loads(request.body)
        project = Project.objects.get(id=data.get('project_id'))
        
        # Check if details already exist to prevent 1:1 violation.
        if hasattr(project, 'details'):
             return error_response("Conflict", "Project already has details.", 400)

        detail = ProjectDetail.objects.create(
            project=project,
            client_name=data.get('client_name', ''),
            start_date=data.get('start_date')
        )
        return JsonResponse({
            "status": "success", 
            "message": "Project details linked.", 
            "id": detail.id
        })
    except Project.DoesNotExist:
        return error_response("Not Found", "Invalid project_id.", 404)
    except Exception as e:
        return error_response("Error", str(e), 400)