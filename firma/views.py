from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from .models import *
from .serializer import *
from rest_framework.response import Response
# @api_view(['GET', 'POST', 'DELETE'])
class Mahsulot_view(APIView):
    def get(self,request):
        user=Mahsulot.objects.all()
        serializer=MahsulotSerializer(user,many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MahsulotSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request):
        count = Mahsulot.objects.all().delete()
        return Response({'message': '{} Ma\'lumot o\'chirildi!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
    
    def patch(self,request):
        serializer = MahsulotSerializer(request.user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED) 
        return Response(status=status.HTTP_400_BAD_REQUEST) 
 

    
class Ishturi(APIView):
    
    def get(self,request):
        user=Ishturi_or_Bolim.objects.all()
        serializer=Ishturi_or_BolimSerializer(user,many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = Ishturi_or_BolimSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request):
        count = Ishturi_or_Bolim.objects.all().delete()
        return Response({'message': '{} Tutorials were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)

# Create your views here.
