from flask import request
from flask import Flask

import bot
app = Flask(__name__)

@app.route('/parse', methods=['POST', 'GET'])
def parse():
    error = None
    q = request.args.get('q')
    return bot.response(q)
