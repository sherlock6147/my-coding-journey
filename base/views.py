from django.shortcuts import render
from development.models import Project,ProjectTag
# Create your views here.
def home(request):
    if request.user.is_staff:
        recent_projects = Project.objects.order_by("started_on")[:3]
    else:
        recent_projects = Project.objects.filter(public=True).order_by("started_on")[:3]
    recent_tags = []
    for project in recent_projects:
        tags = ProjectTag.objects.filter(project=project)
        for tag in tags:
            recent_tags.append(tag)
    context = {}
    context['recent_projects'] = recent_projects
    context['recent_tags'] = recent_tags
    print(context)
    return render(request,'base/index.html',context)