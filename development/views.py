from development.models import Project, ProjectTag
from django.http.response import HttpResponse
from django.shortcuts import render,get_object_or_404
from .models import *

# Create your views here.
def projects(request):
    if(request.user.is_staff):
        project_list = Project.objects.all()
    else:
        project_list = Project.objects.filter(public=True)
    project_dic_list= []
    for project in project_list:
        dictionary = {}
        dictionary['project'] = project
        dictionary['tags'] = ProjectTag.objects.filter(project=project)
        project_dic_list.append(dictionary)
    context = {}
    context['project_dic_list'] = project_dic_list
    print(context)
    return render(request,'development/projects.html',context)

def project_view(request,project_id):
    project = get_object_or_404(Project,id=project_id)
    context = {}
    context['project'] = project
    return render(request,'development/project_view.html',context)