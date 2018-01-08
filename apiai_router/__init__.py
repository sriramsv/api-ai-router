import yaml
import flask
import sys,os
from utils.bots import BotEnsemble,Bot
from utils.join import  Join
from utils.result import json2obj
import apiai
import json,yaml
from flask import Flask,request,jsonify,Response,Session

botensemble=BotEnsemble()
joinObj=Join()
app = Flask(__name__)

CONFIG="config.yaml"
def read_config():

    with open(CONFIG, 'r') as ymlfile:
        cfg = yaml.load(ymlfile)
    if not "bots" in cfg.keys():
        sys.exit("No bots found")

    for b in cfg['bots']:
        bot=Bot(b['name'].lower(),b['client_access_token'])
        botensemble.addBot(bot)

    if "join" in cfg:
        joind=cfg['join']
        try:
            api_key=joind['api_key']
        except:
            sys.exit("Cant find join api_key")
        joinObj.api_key=api_key

        for d in joind['devices']:
            try:
                joinObj.addDevice(d['name'],d['device_id'])
            except KeyError:
                sys.exit("Join device name or ID missing")



def api_ai_request(bot,query):
    token=bot.get_token()
    ai = apiai.ApiAI(token)
    request = ai.text_request()
    request.query = query
    response = request.getresponse()
    r=response.read()
    rbj=json2obj(r)
    joinObj.sendMessage("phone",rbj)
    return r


@app.route('/',methods=['GET'])
def index():
    return "Api AI router"

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
    app.run(host="0.0.0.0",port=int(os.getenv('PORT')))
