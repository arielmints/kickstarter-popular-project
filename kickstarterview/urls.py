from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('projects/', include('top_projects.urls')),
    path('admin/', admin.site.urls),
]