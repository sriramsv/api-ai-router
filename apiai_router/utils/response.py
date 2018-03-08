import json


class Response():
    def __init__(self, **response):

        for k,v in response.items():
            if isinstance(v,dict):
                self.__dict__[k] = Response(**v)
            else:
                self.__dict__[k] = v
    @property
    def speech(self):
        return self.result.fulfillment.speech

    def chatfuel_text(self):
        return json.dumps({"messages":[{"text":self.speech}]})
