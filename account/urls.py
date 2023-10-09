from django.urls import path

from account.views import SigninView, SignupView, SignoutView

app_name = 'account'

urlpatterns = [
    path('signin/', SigninView.as_view(), name='signin'),
    path('signout/', SignoutView.as_view(), name='signout'),
    path('signup', SignupView.as_view(), name='signup'),
]