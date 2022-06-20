from operator import truediv
from django.shortcuts import render
from .models import Song
from .serializers import SongSerializer
from rest_framework.views import APIView  
from rest_framework.response import Response
from rest_framework import status



class SongList(APIView):

        def get(self, request):
            song = Song.objects.all()
            serializer = SongSerializer(song, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK) #make 200_success

        def post(self, request):
            serializer = SongSerializer(data=request.data)
            if serializer.is_valid( ):
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        def put