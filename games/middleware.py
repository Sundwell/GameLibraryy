from django.shortcuts import redirect
from django.urls import reverse, resolve
import logging

logger = logging.getLogger(__name__)


class LoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.exempt_urls = ['/login/', '/register/', '/']

    def __call__(self, request):
        logger.info(f"Path: {request.path}, Authenticated: {request.user.is_authenticated}")

        if not request.user.is_authenticated:
            try:
                resolved_path = resolve(request.path)
                if resolved_path.url_name not in ['login', 'register'] and not any(
                    request.path.startswith(url) for url in self.exempt_urls):
                    logger.info(f"Redirecting to register page from {request.path}")
                    return redirect(reverse('core:register'))
            except Exception as e:
                logger.error(f"Error resolving path: {e}")

        response = self.get_response(request)
        logger.info(f"Proceeding with response for {request.path}")
        return response
