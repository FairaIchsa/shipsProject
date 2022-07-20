from django.urls import path, include

app_name = 'api'

urlpatterns = [
    path('node/', include('mainapp.api.node.urls', namespace='node')),
    path('resource/', include('mainapp.api.resource.urls', namespace='resource')),
]
