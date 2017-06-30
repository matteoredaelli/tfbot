from flask import request
from flask import Flask
import json
import bot

app = Flask(__name__)

@app.route('/parse', methods=['POST', 'GET'])
def parse():
    error = None
    result = {
        "entities": [], 
        "intent": "", 
        "intent_ranking": [], 
        "text": ""
        }
        
    text = request.args.get('q')
    if text:
        intent = bot.response_intent(text)
        result["intent"] = intent
        result["text"] = text
    return json.dumps(result)
