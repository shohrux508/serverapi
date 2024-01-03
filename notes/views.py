from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from channels.layers import get_channel_layer
from . import models
from . import serializers
from asgiref.sync import async_to_sync


# Create your views here.


class NoteListViewAPI(generics.ListCreateAPIView):
    queryset = models.Note.objects.all()
    serializer_class = serializers.NoteSerializer


class NoteRetrieveUpdateDestroyViewAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Note.objects.all()
    serializer_class = serializers.NoteSerializer
    permission_classes = (IsAuthenticated,)


class NoteWebSocketView(APIView):
    def post(self, request, *args, **kwargs):
        message = request.data.get('message', '')
        channel_layer = get_channel_layer()

        # send message to websocket

        async_to_sync(channel_layer.group_send)(
            'notes_group',
            {
                'type': 'note.message',
                'message': message
            }
        )
        return Response({'status': 'success'})
