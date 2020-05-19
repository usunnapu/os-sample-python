from flask import Flask, request

application = Flask(__name__)

@application.route("/")
def hello():
    return "Hello this is MS2!"

@application.route('/query_example')
def query_example():
    language = request.args.get('language')
    print('language is: {}'.format(language))
    return 'MS2 -> MS1: {}'.format(language)

if __name__ == "__main__":
    application.run(debug=True)
