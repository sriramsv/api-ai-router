import apiai,json
from response import Response
class Bot():
    def __init__(self,name,token):
        self.name=name
        self.client=ai=apiai.ApiAI(token)


class BotEnsemble():
    def __init__(self):
        self.bots={}

    def addBot(self,bot):
        self.bots[bot.name]=bot

    def isBot(self,botname):
        return botname in self.bots

    def getBot(self,botname):
        try:
            bot=self.bots[botname]
            return bot
        except:
            return None


class ApiAi():
    def __init__(self,bots):
        self.bots=bots

    def make_request(self,botname,query):
        bot=self.bots.getBot(botname)
        request = bot.client.text_request()
        request.query = query
        response = request.getresponse()
        r=Response(**json.loads(response.read()))
        return r
