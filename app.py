from flask import Flask
from datetime import datetime
from flask import render_template
import re

app = Flask(__name__)


@app.route("/")
def home():
    return 'Hello, Flask!'


@app.route('/user/<name>')
def hello_there(name):
    # now = datetime.now()
    # formatted_now = now.strftime("%A, %d %B, %Y at %X")
    # # match_object = re.match("[a-zA-Z]+", name)

    # # if match_object:
    # #     clean_name = match_object.group(0)
    # # else:
    # #     clean_name = 'Firend'
    # content = '<strong>Hello there, ' + name+'!<strong> its '+formatted_now
    return render_template(
        "hello_there.html",
        name=name,
        date=datetime.now()
    )

    app.run(debug=True)
