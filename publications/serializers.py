from rest_framework import serializers
from .models import Publication

class PublicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publication
        # fields = '__all__'
        fields = (
            'id', 
            'title', 
            'text', 
            'created_at', 
            'updated_at', 
            'user')
        # exclude = ('user') - исключает из выборки указанные поля, нельзя применять вместе с fields