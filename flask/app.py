from flask import Flask
import socket

app = Flask(__name__)

@app.route('/')
def hello_world():
    return f"nginx --> flask CONTAINER ID: {socket.gethostname()}"
    # return "Hello, app.py"

if __name__ == "__main__":
   app.run(host="0.0.0.0", debug = True, port = 5000)
   