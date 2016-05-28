from django.shortcuts import render
from .models import Room


def chat_room(request, label):
    # si no existe la sala con el nombre proporcionado, se crea.
    room, created = Room.objects.get_or_create(label=label)

    # mostramos los ultimos 50 mensajes
    messages = reversed(room.messages.order_by('timestamp')[:50])

    return render(request, "index.html", {
        'room': room,
        'messages': messages,
    })
