# from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Mymodel
from .serializers import Myserializer

# Create your views here.

class Myview(APIView):
    def get(self,request):
        queryset=Mymodel.objects.all()
        serializer=Myserializer(queryset,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer=Myserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)
    
    def put(self,request,id):
        instance=self.get_object(id)
        serializer=Myserializer(instance,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,id):
        instance=self.get_object(id)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


