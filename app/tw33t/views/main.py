from flask import g, Markup
from flask import (Blueprint, render_template, make_response, redirect, url_for, abort, request, Response)
from tw33t import app, socketio, twitterApi
from flask_socketio import SocketIO, emit, Namespace, join_room, leave_room, rooms
from functools import wraps
from flask import jsonify
import json, requests, datetime, sys, os, uuid, re, time
import logging
import os

def setup_logger(log_file, name, formatter = logging.Formatter('%(message)s') ,level=logging.INFO):
    """Function setup as many loggers as you want"""
    handler = logging.FileHandler(log_file)
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)
    return logger

formatter = logging.Formatter('%(asctime)s---%(message)s')
logFile = os.path.join('log','log.log')

if not os.path.isdir('log'):
    os.mkdir('log')

LOGGER = setup_logger(name='test_server', formatter=formatter, log_file=os.path.join('log','log.log'), level=logging.DEBUG)

@app.route("/", methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/get_tweets', methods=['GET'])
def getTweets():
    screenName = request.args.get('screen_name')
    print("screenName: {}".format(screenName))
    _tweets  = twitterApi.request('statuses/user_timeline', {'screen_name':screenName, 'count':'3'})
    
    return render_template('get_tweets.html', _tweets=_tweets)

@socketio.on('clentSendUserName', namespace='/searchTwitters')
def searchUserNameEventHandle(data):
    print('socket io get data: {}'.format(data))
    LOGGER.debug('search: {}'.format(data))
    res = twitterApi.request('users/search', {'q': data, 'count': 5})
    
    if res.status_code == 200:
        for i in res.json():
            print(">>>>>>>>>>>>>>>>>>>>>>sever send result searching to client: {}\n\n".format(i))
            emit('foundUserEmit', i)
    else:
        # i don't know what to do with else
        pass
    return


'''

Introduce a "Get tweets" route for the client and log relevant info from each search into a file.

'''