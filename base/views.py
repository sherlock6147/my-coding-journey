from django.shortcuts import render
from development.models import Project,ProjectTag
# Create your views here.
def home(request):
    if request.user.is_staff:
        recent_projects = Project.objects.order_by("started_on")[:3]
    else:
        recent_projects = Project.objects.filter(public=True).order_by("started_on")[:3]
    context = {}
    context['recent_projects'] = recent_projects
    print(context)
    return render(request,'base/index.html',context)

def about(request):
    return render(request,'base/about.html')

def contact(request):
    return render(request,'base/contact.html')