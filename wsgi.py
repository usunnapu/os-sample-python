from flask import Flask, request, url_for, redirect, render_template
import requests

application = Flask(__name__)


def generate_query_example_url(language):
    url = 'http://100.82.38.31:6001/query_example?language={}'.format(language)
    return url

def display(response):
    print('response: {}'.format(response.text))

@application.route("/")
def hello():
    return "Hello This is MS1!"

@application.route('/language', methods=["POST", "GET"])
def login():
    if request.method == "POST":
        language = request.form.get('language')
        url = generate_query_example_url(language)
        response = requests.get(url)
        display(response)
        return redirect(url_for("language", lang=language))
    else:
        return render_template("language.html")

@application.route("/<lang>")
def language(lang):
    return f"<h1>{lang}</h1>"

if __name__ == "__main__":
    app.run(debug=True, port=5000)
