from flask import Flask, request

application = Flask(__name__)

@application.route("/")
def hello():
    return "Hello this is MS1!"

@application.route('/ms1_query')
def ms1_query():
    language = request.args.get('language')
    print('language is: {}'.format(language))
    return 'PYUSER -> MS1: {}'.format(language)

if __name__ == "__main__":
    application.run(debug=True)
