# api-ai-router
Api.ai bot router


This is a bot router which is used to multiplex multiple bots created in [Dialogflow(api.ai)](https://dialogflow.com).

This provides a REST-API to hit several bots with their respective client tokens through a single interface.

## Installation:
 * clone this repo
 * edit the config.yaml to add your bot's name and client access token found in the [dialogflow.com](https://dialogflow.com). dashboard for your bot
 * run ```python run.py```
 
## Usage:
* The server exposes a REST-API at `<your_ip_address>/api/message/<botname>` and supports both GET and POST requests:
* The botname specified in the config.yaml file will be translated to an endpoint

``` GET REQUEST:

 curl localhost:8080/api/message/homeassistant?query="is my garage open?"
 
 {
  "id": "20a1474f-3288-4a60-a170-8f46b0e4fded",
  "timestamp": "2018-01-06T07:20:42.731Z",
  "lang": "en",
  "result": {
    "source": "agent",
    "resolvedQuery": "is my garage open",
    "action": "getDeviceStatus",
    "actionIncomplete": false,
    "parameters": {
      "device": "garage"
    },
    "contexts": [],
    "metadata": {
      "intentId": "99821a7f-8cc8-49ec-bd94-a5061ad07840",
      "webhookUsed": "true",
      "webhookForSlotFillingUsed": "false",
      "webhookResponseTime": 501,
      "intentName": "Device Status"
    },
    "fulfillment": {
      "speech": "Garage is currently closed",
      "messages": [
        {
          "type": 0,
          "speech": "Garage is currently closed"
        }
      ]
    },
    "score": 1.0
  },
  "alternateResult": {
    "source": "domains",
    "resolvedQuery": "is my garage open",
    "contexts": [],
    "metadata": {},
    "fulfillment": {
      "speech": "",
      "source": "agent"
    },
    "score": 1.0
  },
  
  "sessionId": "cf2c6c61068e4ef9a9babebb68115c09"
}
```


``` POST request
curl -X "POST" http://localhost:8080/api/message/tasker -d '{"query":"turn on bluetooth"}'

{
  "id": "5931194f-3481-4551-950b-7e21b91f39fb",
  "timestamp": "2018-01-06T07:24:03.558Z",
  "lang": "en",
  "result": {
    "source": "agent",
    "resolvedQuery": "",
    "action": "SwitchPeripheral",
    "actionIncomplete": false,
    "parameters": {
      "device": "garage"
    },
    "contexts": [],
    "metadata": {
      "intentId": "99821a7f-8cc8-49ec-bd94-a5061ad07840",
      "webhookUsed": "true",
      "webhookForSlotFillingUsed": "false",
      "webhookResponseTime": 477,
      "intentName": "SwitchPeripheral"
    },
    "fulfillment": {
      "speech": "Turning on Bluetooth",
      "messages": [
        {
          "type": 0,
          "speech": "Turning on Bluetooth"
        }
      ]
    },
    "score": 1.0
  },
  "sessionId": "c0f3b925dbf34aaa90e8cbabc3715bfe"
}
```
