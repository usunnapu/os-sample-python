from flask import Flask, request, url_for, redirect, render_template
import requests
import socket

application = Flask(__name__)


def send_message_to_vran(msg):
    conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print('establishing connect to vran service url port 80')
    conn.connect(('vran.app.svc.cluster.local',80))
    print('connected to vran service url port 80')
    conn.sendall(msg.encode())
    print('sent msg: {}'.format(msg))
    conn.close()

@application.route("/")
def hello():
    return "Hello This is User Input Home Page"

@application.route('/language', methods=["POST", "GET"])
def language():
    if request.method == "POST":
        language = request.form.get('language')
        send_message_to_vran(language)
        return f"<h1> IT WORKS </h1>"
    else:
        return render_template("language.html")

if __name__ == "__main__":
    application.run(debug=True, port=5000)
