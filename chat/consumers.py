import re
import json
import logging
from channels import Group
from channels.sessions import channel_session
from .models import Room

log = logging.getLogger(__name__)


# agrega persistencia de sesiones a los canales (para que pertenezcan a salas)
@channel_session
def ws_connect(message):
    print message['path']

    prefix, label = message['path'].decode('ascii').strip('/').split('/')
    room = Room.objects.get(label=label)
    log.debug(
        'chat connect room=%s client=%s:%s',
        room.label,
        message['client'][0],
        message['client'][1]
    )

    print message.reply_channel

    Group(
        'chat-'+label,
        channel_layer=message.channel_layer
    ).add(message.reply_channel)

    # agregamos la sala a la que pertenece a manera de sesion
    message.channel_session['room'] = room.label


@channel_session
def ws_receive(message):
    label = message.channel_session['room']
    room = Room.objects.get(label=label)

    data = json.loads(message['text'])

    if data:
        log.debug(
            'chat message room=%s handle=%s message=%s',
            room.label,
            data['handle'],
            data['message']
        )

        m = room.messages.create(**data)

        Group(
            'chat-'+label,
            channel_layer=message.channel_layer
        ).send({'text': json.dumps(m.as_dict())})


@channel_session
def ws_disconnect(message):
    label = message.channel_session['room']
    room = Room.objects.get(label=label)
    Group(
        'chat-'+label,
        channel_layer=message.channel_layer
    ).discard(message.reply_channel)
