from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from LibraryAPI.notes.consumers import NoteWebSocketConsumer, NoteConsumer


application = ProtocolTypeRouter({
    'websocket': URLRouter(
        [
            path('ws/notes/', NoteConsumer.as_asgi()),
            path('ws/notes/group/', NoteWebSocketConsumer.as_asgi()),
        ]
    )
})