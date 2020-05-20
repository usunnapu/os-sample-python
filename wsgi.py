from flask import Flask, request, url_for, redirect, render_template
import requests

application = Flask(__name__)


def generate_query_example_url(language):
    url = 'http://nginx.app.svc.cluster.local/ms1_query?language={}'.format(language)
    print('generated url: {}'.format(url))
    return url

def display(response):
    print('response: {}'.format(response.text))

@application.route("/")
def hello():
    return f"<h1>External User Facing Nginx WebServer</h1>"

@application.route('/language', methods=["POST", "GET"])
def login():
    if request.method == "POST":
        language = request.form.get('language')
        url = generate_query_example_url(language)
        response = requests.get(url)
        display(response)
        return f"<h1> IT WORKS </h1>"
    else:
        return render_template("language.html")

if __name__ == "__main__":
    application.run(debug=True, port=5000)
