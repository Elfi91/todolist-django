from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST, require_GET
import json
from tags.models import Tag

@csrf_exempt
@require_POST
def create_tag(request):
    try:
        data = json.loads(request.body)
        if 'name' not in data:
            return JsonResponse({"error": "Il campo 'name' è obbligatorio."}, status=400)
        
        tag, created = Tag.objects.get_or_create(name=data['name'])
        status = 201 if created else 200
        return JsonResponse({"message": "Tag pronto!", "id": tag.id, "new": created}, status=status)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)
    
@require_GET
def list_tags(request):
    tags = Tag.objects.all()
    data = [{"id": t.id, "name": t.name} for t in tags]
    return JsonResponse({"tags": data})