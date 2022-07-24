from rest_framework import serializers

from mainapp.models.port_models import Node


class NodeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Node
        fields = ['id', 'name', 'coordinates']


class NodeRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Node
        fields = ['id', 'name', 'coordinates', 'offers', 'ships', 'icebreakers',
                  'sea_start_for', 'land_start_for', 'sea_end_for', 'land_end_for']
