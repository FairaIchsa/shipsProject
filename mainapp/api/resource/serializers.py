from rest_framework import serializers

from mainapp.models.resource_models import Resource


class ResourceListSerializer(serializers.ModelSerializer):
    type = serializers.SerializerMethodField()

    class Meta:
        model = Resource
        fields = ['id', 'name', 'type']

    def get_type(self, obj):
        return obj.get_type_display()


class ResourceCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resource
        fields = ['id', 'name', 'type']
