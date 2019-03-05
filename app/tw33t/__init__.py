
from flask import Flask
import sys
from flask_socketio import SocketIO, emit, Namespace, join_room, leave_room, rooms
from TwitterAPI import TwitterAPI

app = Flask(__name__)
application = app

# Setup the app with the config.py file
app.config.from_object('config')
socketio = SocketIO(app)


consumer_key='zmkQPv0G6S4fKW3jXR9juM3TC'
consumer_secret='lgY19NPvCeDw1vowvtBEOvxykkUhfmuYVZ4VBf1dvOyBgfACCy'
access_token_key='2940190784-Phe9AsHsqvVhnoOuvUgWZn4lzZ3CIwNvDh4W4kF'
access_token_secret='9s2eBCKCI297hi4yF2BJoHZxZk9o2Yd20tJGU8RsO4I8N'

twitterApi = TwitterAPI(consumer_key, consumer_secret, access_token_key, access_token_secret)

from tw33t.views import main
