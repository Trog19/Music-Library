from .models import Song
from .serializers import SongSerializer
from rest_framework.decorators import api_view  
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404






@api_view(['GET', 'POST'])
def song_list(request):
    if request.method == 'GET':
        song = Song.objects.all()
        serializer = SongSerializer(song, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = SongSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'PUT', 'DELETE', 'PATCH'])
def song_detail(request, pk):
    song = get_object_or_404(Song, pk=pk)
    if request.method == 'GET':
        serializer =SongSerializer(song)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    elif request.method == 'PUT':
        serializer = SongSerializer(song, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    elif request.method == 'DELETE':
        song.delete()
        return Response(status=status.HTTP_404_NOT_FOUND)
    elif request.method == 'PATCH':
        serializer = SongSerializer
