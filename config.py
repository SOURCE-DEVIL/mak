from pyrogram import Client,filters
import redis
from pyromod import listen
import re , requests
r = redis.Redis(
    host="127.0.0.1",
    port=6379,
    charset="utf-8",
    decode_responses=True
    )


api_id = 15296051
api_hash = "4c3e35efa89e4a71172e986f80f57c7b"
token = '7548462461:AAHmwt2LZB85WB9R15E37g4bXaUoD84pNYc'
sudo_ids = [7284348194,6914754656]
sudo_id = 6914754656
bot_id = re.findall('[0-9]+', token)[0]

plugins = dict(root="plugins")
                 
def Owner(msg):
  if (msg.from_user.id in sudo_ids) or (msg.from_user.id == bot_id) :
    ok = True
  else :
    ok = False
  return ok

def check_ch(id) :
  ch = 'revorb0t'
  js = requests.get(f"https://api.telegram.org/bot{token}/getChatMember?chat_id=@{ch}&user_id="+str(id)).json()
  if js['ok'] == False :
      res = "no"
  else :
      res = js['result']['status']
  if res == 'no' :
      return False
  elif res == 'kicked' or res == 'left' :
      return False
  else :
      return True

app = Client(str(bot_id), bot_token=token, api_id = api_id, api_hash = api_hash,plugins=plugins)