from django.urls import path,include
from . import views

app_name = 'development'

urlpatterns = [
    path('',views.projects,name="projects"),
    path('<int:project_id>/',views.project_view,name="project_view"),
]