from django.shortcuts import render
from django.http import HttpResponse
from .models import TopProjects
import json

# Create your views here.
def index(request): 
    projects_history_list = []
    last_24_hours_projects = TopProjects.objects.order_by('-date_updated')[:23]
    for row in last_24_hours_projects:
        instance = {'json': json.loads(row.projects_json), 'date': row.date_updated}
        projects_history_list.append(instance)
    context = {'top_projects': projects_history_list}
    print(projects_history_list)
    return render(request, 'top_projects/index.html', context=context)

    
