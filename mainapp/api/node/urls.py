from django.urls import path

from .api_views import NodeModelViewSet


app_name = 'node'

urlpatterns = [
    path('all/', NodeModelViewSet.as_view({'get': 'list'}), name='all'),
    path('get_by_id/<int:pk>', NodeModelViewSet.as_view({'get': 'retrieve'}), name='by-id')
]
