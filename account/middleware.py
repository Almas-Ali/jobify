from django.shortcuts import redirect
from django.urls import reverse_lazy


class RestrictSignInSignUpMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated and \
            request.path in [reverse_lazy('account:signin'), 
                             reverse_lazy('account:signup')]:
            # If the user is authenticated, redirect to the dashboard or any other desired page.
            return redirect(reverse_lazy('core:dashboard'))
        return self.get_response(request)
