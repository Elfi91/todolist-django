"""
API Utility functions.
Author: Elisabetta
Style: antirez-inspired (clear, narrative, essential).
"""

from django.http import JsonResponse

def error_response(message, details=None, status=400):
    """
    This function returns a standardized JSON error object. We use 'status' 
    to indicate the failure and 'code' to mirror the HTTP status, making 
    the response easy to parse for any client.
    """
    
    response_data = {
        "status": "error",
        "code": status,
        "message": message
    }
    if details:
        response_data["details"] = details
        
    return JsonResponse(response_data, status=status)