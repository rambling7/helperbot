from flask import Flask, request
import telegram
import config
import commands

app = Flask(__name__)
app.debug = True

global bot 
bot = telegram.Bot(token=config.TOKEN)
 
#   Set webhook for connection 
@app.route('/set_webhook', methods=['POST', 'GET']) 
def set_webhook():
  webhook = bot.setWebhook('https://%s:%s/%s' % (config.URL, config.PORT, config.TOKEN), certificate=open(config.CERT, 'rb')) 
  if webhook:
    return "webhook setup ok" 
  else: 
    return "webhook setup failed"  
 
#   Processing
@app.route('/%s' % config.TOKEN, methods=['POST', 'GET']) 
def webhook_handler():
  if request.method == "POST": 
    update = telegram.Update.de_json(request.get_json(force=True), bot)
   
    chat_id = update.message.chat.id 
    cmd = update.message.text
    func = commands.comm_arr.get(cmd.split()[0].lower())
    if func:
      bot.send_message(chat_id=chat_id, text=func())
    else:
      bot.send_message(chat_id=chat_id, text='Не понял')
  
  return 'processing' 
  
@app.route('/', methods=['POST', 'GET']) 
def testing():
  
  
  
  return 0



