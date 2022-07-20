from rest_framework.viewsets import ModelViewSet

from .serializers import ResourceListSerializer, ResourceCreateSerializer

from mainapp.models.resource_models import Resource


class ResourceModelViewSet(ModelViewSet):
    queryset = Resource.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return ResourceListSerializer
        elif self.action == 'create':
            return ResourceCreateSerializer
