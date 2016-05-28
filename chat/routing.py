# consumer que trae channels para archivos estaticos
from channels.staticfiles import StaticFilesConsumer
from . import consumers

channel_routing = {
    # archivos staticos
    'http.request': StaticFilesConsumer(),

    # mensajes websocket ejecutados por los consumidores de django:
    'websocket.connect': consumers.ws_connect,
    'websocket.receive': consumers.ws_receive,
    'websocket.disconnect': consumers.ws_disconnect,
}
