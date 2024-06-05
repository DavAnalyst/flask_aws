from flask import Flask

application = Flask(__name__)

@application.route('/')
def hellow_world():
    return 'hellow mundoo'

if __name__  == "__main__":
    application.run(debug=True)