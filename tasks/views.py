from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST, require_http_methods
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

@require_http_methods(["GET"])
def get_taks_by_project(request):
    project_id = request.GET.get('project_id')

    taks = Task.objects.filter(project_id=project_id)

    task_list = []
    for t in taks:
        task_list.append({
            "id": t.id,
            "title": t.title,
            "description": t.description,
        })

    return JsonResponse({"project_id": project_id, "tasks": task_list})

@csrf_exempt
@require_http_methods(["DELETE"])
def delete_task(request, task_id):
    try:
        task = Task.objects.get(id=task_id)
        task_title = task.title
        task.delete
        return JsonResponse({"message": f"Task '{task_title}' (ID: {task_id} deleted successfully!"})
    except Task.DoesNotExist:
        return JsonResponse({"error": "Task not found"}, status=404)
    
@csrf_exempt
@require_http_methods(["PATCH"])
def patch_task(request, task_id):
    try:
        task = Task.objects.get(id=task_id)
        data = json.loads(request.body)

        if 'title' in data:
            task.title = data['title']
        if 'description' in data:
            task.description = data['description']
        if 'project' in data:
            task.project_id = data['project']

        task.save()
        return JsonResponse({"message": f"Task {task_id} updated!", "id": task.id})
    except Task.DoesNotExist:
        return JsonResponse({"error": "Task not found"}, status=404)
    
@csrf_exempt
@require_http_methods(["PUT"])
def put_task(request, task_id):
    try:
        task = Task.objects.get(id=task_id)
        data = json.loads(request.body)
        
        # Con PUT, sovrascriviamo tutto
        task.title = data.get('title')
        task.description = data.get('description')
        task.project_id = data.get('project')
        
        task.save()
        return JsonResponse({"message": f"Task {task_id} fully updated (PUT)!"})
    except Task.DoesNotExist:
        return JsonResponse({"error": "Task not found"}, status=404)
    except KeyError:
        return JsonResponse({"error": "Missing required fields for PUT"}, status=400)