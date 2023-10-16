from rest_framework.decorators import api_view
from rest_framework.generics import ListCreateAPIView
from rest_framework.viewsets import ModelViewSet
from .serializers import RequestsSerializer,HeaderSerializer,BodySerializer
from .models import Requests,Headers,Body
# Create your views here.

class RequestViewSet(ModelViewSet):
    queryset=Requests.objects.filter(is_deleted=False)
    serializer_class=RequestsSerializer

class HeaderViewSet(ModelViewSet):
    serializer_class=HeaderSerializer
    def get_queryset(self):
            return Headers.objects.filter(is_deleted=False)

    def get_serializer_context(self):
            return {'request_id': self.kwargs['request_pk']}

class BodyViewSet(ModelViewSet):
    serializer_class=BodySerializer
    def get_queryset(self):
            return Body.objects.filter(is_deleted=False)

    def get_serializer_context(self):
            return {'request_id': self.kwargs['request_pk']}