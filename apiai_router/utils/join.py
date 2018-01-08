import requests

class Join():
    def __init__(self,api_key=None):
        self.devices={}
        self.base_url="https://joinjoaomgcd.appspot.com"
        self.api_key=api_key

    def addDevice(self,deviceName,deviceId):
        self.devices[deviceName]=deviceId

    def craftMessage(self,resultobj):
        if not resultobj:
            return None
        action=resultobj.action
        k=resultobj.parameters._asdict()
        k=sorted(k.items())
        for p in k:
            action+="=:="+p[1]
        return action

    def sendMessage(self,device_name,resultobj):
        msg=self.craftMessage(resultobj.result)
        if not msg:
            return None
        try:
            deviceId=self.devices[device_name]
        except KeyError:
            raise DeviceNotFoundError
        url="{}/_ah/api/messaging/v1/sendPush?text={}&deviceId={}&apikey={}".format(self.base_url,msg,deviceId,self.api_key)
        r=requests.get(url)
        if r.status_code!=200:
            return None
        return 0
