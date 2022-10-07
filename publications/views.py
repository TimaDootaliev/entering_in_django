"""  
views.py - отвечает за отображение/создание/удаление/обновление данных и определение логики их доступности
"""
from rest_framework.decorators import api_view
from .models import Publication
from .serializers import PublicationSerializer
from rest_framework.response import Response

"""  
GET
PUT/PATCH
DELETE
POST
"""
@api_view(['GET'])
def list_of_publications(request):
    queryset = Publication.objects.all() 
    # SELECT * FROM publication; [pub1, pub2, pub3]
    serializer = PublicationSerializer(queryset, many=True)
    return Response(serializer.data) # возвращает HTTP ответ
