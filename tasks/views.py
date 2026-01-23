from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST, require_http_methods
import json
from tasks.models import Task, TaskDetail

@csrf_exempt
@require_POST
def create_task(request):
    data = json.loads(request.body)
    project_id = data.get('project')
    new_task = Task.objects.create(
        title=data['title'],
        project_id=project_id
    )
    return JsonResponse({"message": "Task aggiunta!", "id": new_task.id})

@require_http_methods(["GET"])
def get_taks_by_project(request):
    project_id = request.GET.get('project_id')
    tasks = Task.objects.filter(project_id=project_id)
    task_list = [{"id": t.id, "title": t.title, "description": t.description} for t in tasks]
    return JsonResponse({"project_id": project_id, "tasks": task_list})

@csrf_exempt
@require_http_methods(["DELETE"])
def delete_task(request, task_id):
    try:
        task = Task.objects.get(id=task_id)
        task_title = task.title
        task.delete() # Corretto: aggiunte parentesi
        return JsonResponse({"message": f"Task '{task_title}' deleted successfully!"})
    except Task.DoesNotExist:
        return JsonResponse({"error": "Task not found"}, status=404)

@csrf_exempt
@require_http_methods(["PATCH"])
def patch_task(request, task_id):
    try:
        task = Task.objects.get(id=task_id)
        data = json.loads(request.body)
        if 'title' in data: task.title = data['title']
        if 'description' in data: task.description = data['description']
        if 'project' in data: task.project_id = data['project']
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
        task.title = data.get('title')
        task.description = data.get('description')
        task.project_id = data.get('project')
        task.save()
        return JsonResponse({"message": f"Task {task_id} fully updated!"})
    except Task.DoesNotExist:
        return JsonResponse({"error": "Task not found"}, status=404)

@csrf_exempt
@require_http_methods(["POST"])
def add_task_details(request):
    try:
        data = json.loads(request.body) # Corretto: request.body
        detail = TaskDetail.objects.create(
            task_id=data['task_id'],
            deadline=data.get('deadline'),
            priority=data.get('priority', 'Medium')
        )
        return JsonResponse({"message": "Task details created!", "detail_id": detail.id})
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)