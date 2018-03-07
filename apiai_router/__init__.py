import yaml
import flask
import sys,os
from utils.bots import BotEnsemble,Bot
import apiai
import json,yaml
from flask import Flask,request,jsonify,Response,Session

botensemble=BotEnsemble()

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


def api_ai_request(bot,query):
    token=bot.get_token()
    ai = apiai.ApiAI(token)
    request = ai.text_request()
    request.query = query
    response = request.getresponse()
    r=response.read()
    return frame_response(json.loads(r)["result"]["fulfillment"]["speech"])

def frame_response(msg):
    d=json.loads({"messages": [{"text": ""}]})
    d["messages"][0]["text"]=msg
    return d
@app.route('/',methods=['GET'])
def index():
    return "Api AI router"

@app.route('/api/message/<botname>',methods=['POST','GET'])
def router(botname):
    if request.method=='GET':
        query=request.args.get('query','')
    elif request.method=='POST':
        if not request.is_json:
            return Response(400,"Invalid Request")
        query=request.get_json()["query"]

    if not query:
        return Response(400,"Invalid request")
    if not botensemble.isBot(botname):
        return Response(404,"Bot Not found")
    bot=botensemble.getBot(botname)
    
    return api_ai_request(bot,query)

def main():
    read_config()
    app.run(host="0.0.0.0",port=int(os.getenv('PORT')))
