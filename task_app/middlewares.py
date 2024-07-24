from django.shortcuts import redirect, render
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

def invalid_url_middleware(get_response):
    def middleware(request):
        response = get_response(request)
        if response.status_code == 404:
            return render(request,'404.html',status = 404)
        return response
    return middleware

