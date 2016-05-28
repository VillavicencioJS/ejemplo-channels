# ejemplo-channels
Ejemplo de django channels para villadevs

Basado en https://blog.heroku.com/archives/2016/3/17/in_deep_with_django_channels_the_future_of_real_time_apps_in_django

## Como ejecutarlo:

### Cree un entorno virtual
`virtualenv <nombre>`

### Se activa el entorno virtual
`source <nombre>/bin/activate`

### Instale los requerimientos

`pip install -r requirements.txt`

### En una terminal o en background debe estar corriendo un server de redis
`redis-server`

### Se debe inicializar daphne para recibir peticiones http o conexiones y mensajes a través de websockets
`daphne villadevs.asgi:channel_layer --port 8888`

### Por último se inicia un worker para responder las peticiones puestas en el channel layer
`./manage.py runworker`


[Cualquier duda con gusto me encuentran en @soybackend :)](https://www.twitter.com/soybackend)
[O en el FanPage de la comunidad](https://www.facebook.com/villavicenciojs/)
