import logging
from django.http import JsonResponse
from django.conf import settings
import jwt


logger = logging.getLogger(__name__)


class ApiAuthMiddleware:
    """
    Middleware to enforce authentication on specific API endpoints.
    This version manually decodes the JWT token to check authentication.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        protected_paths = ['/api/dashboard/', '/api/articles/create/', '/api/articles/']

        if request.path in protected_paths:
            auth_header = request.headers.get('Authorization')
            if auth_header:
                try:
                    token = auth_header.split(' ')[1]
                    payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
                    # Optionally, set request.user to the user instance here if needed
                    # For example: request.user = User.objects.get(pk=payload['user_id'])
                except (jwt.ExpiredSignatureError, jwt.DecodeError, jwt.InvalidTokenError):
                    return JsonResponse({'detail': 'Invalid token.'}, status=401)
            else:
                return JsonResponse({'detail': 'Authentication credentials were not provided.'}, status=401)

        return self.get_response(request)






























# class RateLimitMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response
#         # Rate limit settings: 5 attempts per minute per IP
#         self.RATE_LIMIT = 5
#         self.WINDOW_SECONDS = 60

#     def __call__(self, request):
#         if request.path in ['/api/auth/login/', '/api/auth/register/']:
#             ip = request.META.get('REMOTE_ADDR')
#             cache_key = f'rate_limit_{ip}_{request.path}'
            
#             request_count = cache.get(cache_key, 0)
#             if request_count >= self.RATE_LIMIT:
#                 return HttpResponseForbidden("Too many requests. Try again later.")
            
#             cache.set(cache_key, request_count + 1, self.WINDOW_SECONDS)
        
#         return self.get_response(request)