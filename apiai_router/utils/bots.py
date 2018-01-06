

class Bot():
    def __init__(self,name,token):
        self.name=name
        self._token=token

    def get_token(self):
        return self._token


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
