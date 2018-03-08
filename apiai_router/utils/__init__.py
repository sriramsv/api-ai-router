
import random,string
import yaml
import requests
import apiai_router.config as config
def random_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))


def getTokens():
    url=config.JSON_BIN_URL+"/api_ai_router"
    headers={"authorization":"token {}".format(config.DB_TOKEN)}
    r=requests.get(url,headers=headers)
    if r.status_code!=200:
        return None
    print r.json()
    return r.json()
