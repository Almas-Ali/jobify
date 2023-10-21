from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.auth import login

from account.forms import SignUpForm


class SigninView(LoginView):
    template_name = 'account/signin.html'
    redirect_authenticated_user = True
    # if we are loged in and try to access login page then it will redirect to dashboard
    
    
    def get_success_url(self):
        return reverse_lazy('core:home')
    
    def form_valid(self, form):
        messages.success(self.request, 'Logged in successfully')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Invalid Email or password')
        return super().form_invalid(form)
    

class SignoutView(LogoutView):
    next_page = reverse_lazy('core:home')



class SignupView(CreateView):
    model = get_user_model()
    template_name = 'account/signup.html'
    form_class = SignUpForm
    success_url = reverse_lazy('core:dashboard')
    success_message = 'Account created successfully'
    redirect_authenticated_user = True

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        return response

    def form_invalid(self, form):
        if form.errors:
            for field in form:
                for error in field.errors:
                    messages.error(self.request, error)
        return super().form_invalid(form)
    