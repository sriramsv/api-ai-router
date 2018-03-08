import yaml
import flask
import sys,os
from utils.bots import BotEnsemble,Bot,ApiAi
from utils import getTokens

import json,yaml
from flask import Flask,request,jsonify,Response,Session

botensemble=BotEnsemble()
apiai=ApiAi(botensemble)
app = Flask(__name__)

def read_config():
    bots=getTokens()
    if not bots:
        exit(-1)
    for b,t in bots.items():
        bot=Bot(b.lower(),t)
        apiai.bots.addBot(bot)

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
    r=apiai.make_request(botname,query)
    return r.chatfuel_text()

def main():
    read_config()
    app.run(host="0.0.0.0",port=int(os.getenv('PORT')))
