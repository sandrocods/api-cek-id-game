import sys
import os

# Add the top-level directory (api-cek-id-game) to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask import Flask, render_template
from datetime import datetime
from api.apiCheckIdGame import apiCheckIdGame

app = Flask(__name__, template_folder='views', static_folder='views')


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


app.register_blueprint(apiCheckIdGame, url_prefix='/api')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
