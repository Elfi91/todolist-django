"""
Tag Views.
Handling the creation and listing of tags. 
We use 'get_or_create' to be idempotent: if the tag exists, we just return it.
"""
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST, require_GET
import json
from .models import Tag
from core.utils import error_response

@csrf_exempt
@require_POST
def create_tag(request):
    """Creates a new tag or retrieves an existing one by name."""
    try:
        data = json.loads(request.body)
        
        if 'name' not in data or not data['name']:
            return error_response("Missing field", "The 'name' field is mandatory.", 400)
        
        # Idempotent logic: prevents duplicates while remaining efficient.
        tag, created = Tag.objects.get_or_create(name=data['name'])
        status_code = 201 if created else 200
        
        return JsonResponse({
            "status": "success",
            "message": "Tag is ready.",
            "id": tag.id,
            "is_new": created
        }, status=status_code)
        
    except json.JSONDecodeError:
        return error_response("Invalid JSON", "Check your request body format.", 400)
    except Exception as e:
        return error_response("Server Error", str(e), 500)
    
@require_GET
def list_tags(request):
    """Returns all tags available in the system."""
    tags = Tag.objects.all()
    if not tags.exists():
        return error_response("No Tags", "The tag database is empty.", 404)
        
    data = [{"id": t.id, "name": t.name} for t in tags]
    return JsonResponse({"status": "success", "tags": data})