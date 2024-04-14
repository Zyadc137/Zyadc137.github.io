
from flask import *
import os



application = Flask(__name__)


@application.route("/")
@application.route("/home")
def home():
    return render_template('home.html')

@application.route("/another/")
def another():
    return render_template('another.html')

@application.route("/hd/")
def hd():
    image_filenames = [f for f in os.listdir('static/images/high/') if os.path.isfile(os.path.join('static/images/high', f))]
    return render_template('high.html', image_filenames=image_filenames)


@application.route("/low/")
def low():
    image_filenames = [f for f in os.listdir('static/images/low/') if os.path.isfile(os.path.join('static/images/low', f))]
    return render_template('low.html', image_filenames=image_filenames)


if __name__ == '__main__':
    application.run(debug=True)

