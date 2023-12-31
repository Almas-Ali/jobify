from django.urls import path

from core import views

app_name = 'core'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('search/', views.SearchView.as_view(), name='search'),

    path('job/<slug:slug>/', views.JobDetailView.as_view(), name='job_detail'),
    path('apply/<slug:slug>/', views.ApplyView.as_view(), name='apply'),

    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('profile/edit/', views.ProfileEditView.as_view(), name='edit_profile'),

    path('settings/', views.SettingsView.as_view(), name='settings'),
    path('settings/profile/', views.ProfileSettingsView.as_view(), name='profile_settings'),
    path('settings/password/', views.PasswordChangeView.as_view(), name='change_password'),
    path('settings/privacy/', views.PrivacySettingsView.as_view(), name='privacy_settings'),
]