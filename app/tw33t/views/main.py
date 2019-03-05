from flask import g, Markup
from flask import (Blueprint, render_template, make_response, redirect, url_for, abort, request, Response)
from tw33t import app, socketio, twitterApi
from flask_socketio import SocketIO, emit, Namespace, join_room, leave_room, rooms
from functools import wraps
from flask import jsonify
import json, requests, datetime, sys, os, uuid, re, time

@app.route("/", methods=['GET'])
def index():
    return render_template('index.html')

@socketio.on('clentSendUserName', namespace='/searchTwitters')
def searchUserNameEventHandle(data):
    print('socket io get data: {}'.format(data))
    res = twitterApi.request('users/search', {'q': data, 'count': 5})
    
    if res.status_code == 200:
        for i in res.json():
            print(">>>>>>>>>>>>>>>>>>>>>>sever send result searching to client: {}\n\n".format(i))
            emit('foundUserEmit', i)
    else:
        # i have no what to do with else
        pass

    return


@app.after_request
def set_response_headers(response):
    # print("request end here: {}".format(request.sid))
    # LOGGER.debug('not caching data')
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response

'''

Introduce a "Get tweets" route for the client and log relevant info from each search into a file.

'''