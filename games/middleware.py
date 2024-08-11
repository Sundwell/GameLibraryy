from django.shortcuts import redirect
from django.urls import reverse
import logging

logger = logging.getLogger(__name__)


class LoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        logger.info(f"Path: {request.path}, Authenticated: {request.user.is_authenticated}")
        if not request.user.is_authenticated:
            if request.path not in [reverse('core:login'), reverse('core:register')]:
                logger.info(f"Redirecting to register page from {request.path}")
                return redirect(reverse('core:register'))
        response = self.get_response(request)
        logger.info(f"Proceeding with response for {request.path}")
        return response
