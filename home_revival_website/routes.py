from flask import *

#----------------------#
# App Setup and Config #
#----------------------#
app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.config['SECRET_KEY'] = 'correcthorsebatterystaple'

@app.route("/")
def index():
    return(render_template("index.html"))