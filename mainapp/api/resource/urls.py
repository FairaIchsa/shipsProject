from django.urls import path

from .api_views import ResourceModelViewSet


app_name = 'resource'

urlpatterns = [
    path('all/', ResourceModelViewSet.as_view({'get': 'list'}), name='all'),
    path('get_by_id/<int:pk>', ResourceModelViewSet.as_view({'get': 'retrieve'}), name='by-id'),
    path('create/', ResourceModelViewSet.as_view({'post': 'create'}), name='create')
]
