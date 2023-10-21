from django.urls import path

from applicant import views

app_name = 'applicant'

urlpatterns = [
    path('list', views.ApplicantsView.as_view(), name='applicants_list'),
    path('suspend/<int:id>', views.ApplicantSuspendView.as_view(), name='applicant_suspend'),
    path('unsuspend/<int:id>', views.ApplicantUnsuspendView.as_view(), name='applicant_unsuspend'),

    path('sent-applications', views.SentApplicationsView.as_view(), name='sent_applications'),
]