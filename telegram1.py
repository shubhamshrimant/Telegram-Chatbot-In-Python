
# -*- coding: utf-8 -*-
"""
Created on Thu May 27 13:10:13 2021

@author: shubh
"""
import os
from flask import Flask, request
import telegram,re
global bot
global TOKEN
import chatbot


bot_token = "1885790205:AAHO4QELFu-ABa4CsJkcyU1B8k0clKy0Qc4"
bot_user_name = "Co_Helper_Bot"
URL = "https://telegramchatbot109.herokuapp.com/"
TOKEN = bot_token
bot = telegram.Bot(token=TOKEN)

import random
greetings = ['hey', 'hello', 'hi', "it's great to see you", 'nice to see you', 'good to see you']
bye = ['Bye', 'Bye-Bye', 'Goodbye', 'Have a good day','Stop']
thank_you = ['thanks', 'thank you', 'thanks a bunch', 'thanks a lot.', 'thank you very much', 'thanks so much', 'thank you so much']
thank_response = ['You\'re welcome.' , 'No problem.', 'No worries.', ' My pleasure.' , 'It was the least I could do.', 'Glad to help.']
app = Flask(__name__)

@app.route('/{}'.format(TOKEN), methods=['POST'])
def respond():
   # retrieve the message in JSON and then transform it to Telegram object
   update = telegram.Update.de_json(request.get_json(force=True), bot)

   chat_id = update.message.chat.id
   msg_id = update.message.message_id

   # Telegram understands UTF-8, so encode text for unicode compatibility
   text = update.message.text.encode('utf-8').decode()
   # for debugging purposes only
   print("got text message :", text)
   # the first time you chat with the bot AKA the welcoming message
   if text == "/start":
       # print the welcoming message
       bot_welcome = """
       Hi, I'm Sova. I can tell you some info about covid"""
       # send the welcoming message
       bot.sendMessage(chat_id=chat_id, text=bot_welcome, reply_to_message_id=msg_id)


   else:
       answer=chatbot.chatbot(text)
       bot.sendMessage(chat_id=chat_id, text=answer, reply_to_message_id=msg_id)

   return 'ok'

@app.route('/set_webhook', methods=['GET', 'POST'])
def set_webhook():
   s = bot.setWebhook('{URL}{HOOK}'.format(URL=URL, HOOK=TOKEN))
   if s:
       return "webhook setup ok"
   else:
       return "webhook setup failed"

@app.route('/')
def index():
   return '.'


if __name__ == '__main__':
   port = int(os.environ.get("PORT", 33507))
   app.run(host='0.0.0.0',port=port,threaded=True)
