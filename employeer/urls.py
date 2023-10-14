from django.urls import path

from employeer import views

app_name = 'employeer'

urlpatterns = [
    # path('', views.index, name='index'),
    # path('employeer/add/', views.add_employeer, name='add_employeer'),
    # path('employeer/view/<int:pk>', views.view_employeer, name='view_employeer'),
    # path('employeer/edit/<int:pk>', views.edit_employeer, name='edit_employeer'),
    # path('employeer/delete/<int:pk>', views.delete_employeer, name='delete_employeer'),
    
    # Companies routes
    path('create-company/', views.CreateCompanyView.as_view(), name='create_company'),
    path('companies/', views.CompaniesView.as_view(), name='companies'),
    
    # Jobs routes
    path('jobs/', views.JobsView.as_view(), name='jobs'),
    path('add-job/', views.AddJobView.as_view(), name='add_job'),
    path('locations/', views.LocationsView.as_view(), name='locations'),
    path('tags/', views.TagsView.as_view(), name='tags'),
]