from development.models import Project, ProjectTag
from django.http.response import HttpResponse
from django.shortcuts import render,get_object_or_404
from .models import *

# Create your views here.
def projects(request):
    if request.user.is_staff:
        project_list = Project.objects.order_by("started_on")[:3]
    else:
        project_list = Project.objects.filter(public=True).order_by("started_on")[:3]
    project_tags = []
    for project in project_list:
        tags = ProjectTag.objects.filter(project=project)
        for tag in tags:
            project_tags.append(tag)
    context = {}
    context['project_list'] = project_list
    context['project_tags'] = project_tags
    print(context)
    return render(request,'development/projects.html',context)

def project_view(request,project_id):
    project = get_object_or_404(Project,id=project_id)
    context = {}
    context['project'] = project
    return render(request,'development/project_view.html',context)