import os
os.system('pip install flask')
import flask
import threading
app = flask.Flask(__name__)

def trd():
    global app
    
    app.run(host="0.0.0.0", port=8080)
    print('thread')

@app.route("/")
def index():

    ip_address = flask.request.remote_addr
    return ip_address
    
#td = threading.Thread(target = trd)
#td.start()
app.run(host="0.0.0.0", port=8080)