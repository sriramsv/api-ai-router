import yaml
import flask
import sys
from utils.bots import BotEnsemble,Bot
from utils import random_generator
import apiai
import json,yaml
from flask import Flask,request,jsonify,Response,Session

botensemble=BotEnsemble()
app = Flask(__name__)

CONFIG="config.yaml"
def read_config():

    with open(CONFIG, 'r') as ymlfile:
        cfg = yaml.load(ymlfile)

    for b in cfg['bots']:
        bot=Bot(b['name'].lower(),b['client_access_token'])
        botensemble.addBot(bot)

def api_ai_request(bot,query):
    token=bot.get_token()
    ai = apiai.ApiAI(token)
    request = ai.text_request()
    request.query = query
    response = request.getresponse()
    if not response:
        return None
    return response.read()


@app.route('/api/message/<botname>',methods=['POST','GET'])
def router(botname):
    if request.method=='GET':
        query=request.args.get('query','')
    elif request.method=='POST':
        if not request.is_json:
            return Response(500,"Json expected")
        query=request.get_json()["query"]
    if not botensemble.isBot(botname):
        return Response(404,"Bot Not found")
    bot=botensemble.getBot(botname)
    return api_ai_request(bot,query)

def main():
    read_config()
    app.run(host="0.0.0.0",port=8080)
