from rest_framework.viewsets import ModelViewSet

from .serializers import NodeListSerializer, NodeRetrieveSerializer

from mainapp.models.node_models import Node


class NodeModelViewSet(ModelViewSet):
    queryset = Node.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return NodeListSerializer
        elif self.action == 'retrieve':
            return NodeRetrieveSerializer
