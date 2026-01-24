"""
Task Management Views.
Implements CRUD operations and complex filtering (by priority and tags).
"""

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST, require_http_methods
import json

from .models import Task, TaskDetail
from tags.models import Tag
from core.utils import error_response 

@csrf_exempt
@require_POST
def create_task(request):
    """Creates a task assigned to a project."""
    try:
        data = json.loads(request.body)
        if 'title' not in data or not data['title']:
            return error_response("Missing Data", "Title is required.", 400)
        if 'project' not in data:
            return error_response("Missing Project", "Task must belong to a project.", 400)

        task = Task.objects.create(
            title=data['title'],
            description=data.get('description', ''),
            project_id=data['project']
        )
        return JsonResponse({"status": "success", "id": task.id}, status=201)
    except Exception as e:
        return error_response("Error", str(e), 500)

@require_http_methods(["GET"])
def get_tasks_by_project(request):
    """Returns tasks for a project, with optional priority/tag filtering."""
    project_id = request.GET.get('project_id')
    priority = request.GET.get('priority')
    tag_id = request.GET.get('tag_id')

    if not project_id:
        return error_response("Query Error", "project_id is required.", 400)

    tasks = Task.objects.filter(project_id=project_id)
    
    if priority:
        tasks = tasks.filter(details__priority=priority)
    if tag_id:
        tasks = tasks.filter(tags__id=tag_id)

    if not tasks.exists():
        return error_response("Not Found", "No tasks match your criteria.", 404)

    results = [{
        "id": t.id,
        "title": t.title,
        "priority": t.details.priority if hasattr(t, 'details') else "N/A",
        "tags": list(t.tags.values('id', 'name'))
    } for t in tasks]

    return JsonResponse({"status": "success", "tasks": results})

@csrf_exempt
@require_http_methods(["DELETE"])
def delete_task(request, task_id):
    """Removes a task from the system."""
    try:
        task = Task.objects.get(id=task_id)
        task.delete()
        return JsonResponse({"status": "success", "message": f"Task {task_id} deleted."})
    except Task.DoesNotExist:
        return error_response("Not Found", "Task ID not found.", 404)

@csrf_exempt
@require_http_methods(["PATCH"])
def patch_task(request, task_id):
    """Partial update of a task."""
    try:
        task = Task.objects.get(id=task_id)
        data = json.loads(request.body)
        if 'title' in data: task.title = data['title']
        if 'description' in data: task.description = data['description']
        task.save()
        return JsonResponse({"status": "success", "message": "Task updated."})
    except Task.DoesNotExist:
        return error_response("Not Found", "Task not found.", 404)

@csrf_exempt
@require_http_methods(["PUT"])
def put_task(request, task_id):
    """Full update of a task."""
    try:
        task = Task.objects.get(id=task_id)
        data = json.loads(request.body)
        if 'title' not in data or 'project' not in data:
            return error_response("Incomplete Data", "Title and project are required for PUT.", 400)
        task.title = data['title']
        task.description = data.get('description', '')
        task.project_id = data['project']
        task.save()
        return JsonResponse({"status": "success", "message": "Task replaced."})
    except Task.DoesNotExist:
        return error_response("Not Found", "Task not found.", 404)

@csrf_exempt
@require_POST
def add_task_details(request):
    """Links metadata to a task (1:1)."""
    try:
        data = json.loads(request.body)
        task = Task.objects.get(id=data.get('task_id'))
        if hasattr(task, 'details'):
            return error_response("Conflict", "Details already exist.", 400)

        detail = TaskDetail.objects.create(
            task=task,
            deadline=data.get('deadline'),
            priority=data.get('priority', 'Medium')
        )
        return JsonResponse({"status": "success", "id": detail.id})
    except Task.DoesNotExist:
        return error_response("Not Found", "Task not found.", 404)

@csrf_exempt
@require_POST
def attach_tag_to_task(request, task_id):
    """Junction handler for M:N relationship."""
    try:
        data = json.loads(request.body)
        task = Task.objects.get(id=task_id)
        tag = Tag.objects.get(id=data.get('tag_id'))
        task.tags.add(tag)
        return JsonResponse({"status": "success", "message": f"Tag {tag.name} attached."})
    except Exception:
        return error_response("Not Found", "Task or Tag missing.", 404)