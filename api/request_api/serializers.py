from rest_framework import serializers
from .models import Requests,Headers,Body

class HeaderSerializer(serializers.ModelSerializer):
    class Meta:
        model= Headers
        fields= ['id','key','value']
    def create(self, validated_data):
        request_id = self.context['request_id']
        header=Headers.objects.create(**validated_data)
        request=Requests.objects.get(id=request_id)
        request.headers.add(header)
        return header

class BodySerializer(serializers.ModelSerializer):
    class Meta:
        model= Body
        fields= ['id','key','value']
    def create(self, validated_data):
        request_id = self.context['request_id']
        body=Body.objects.create(**validated_data)
        request=Requests.objects.get(id=request_id)
        request.bodies.add(body)
        return body
class RequestsSerializer(serializers.ModelSerializer):
    headers=HeaderSerializer(many=True,read_only=True)
    bodies=BodySerializer(many=True,read_only=True)
    class Meta:
        model = Requests
        fields = ['id','url','headers','bodies']