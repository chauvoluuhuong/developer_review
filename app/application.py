from tw33t import app, socketio

#Development
#application.run(host='0.0.0.0', threaded=True, port=5000, debug=True)

#Deployment to production or staging
if __name__ == "__main__":
	socketio.run(app ,debug=True, host='0.0.0.0')
