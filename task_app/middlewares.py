from django.shortcuts import redirect
from django.urls import reverse
from django.conf import settings

def login_required_middleware(get_response):
    # One-time configuration and initialization.
    exempt_urls = [reverse(url) for url in settings.EXEMPT_URLS]
    def middleware(request):
        # Skip processing if the user is already authenticated
        if not request.user.is_authenticated:
            # Check if the requested URL is in the exempt list
            if request.path not in exempt_urls:
                return redirect(settings.LOGIN_URL)
        response = get_response(request)
        return response
    return middleware