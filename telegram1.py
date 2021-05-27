
# -*- coding: utf-8 -*-
"""
Created on Thu May 27 13:10:13 2021

@author: shubh
"""
# -*- coding: utf-8 -*-
"""
Created on Wed May 26 13:18:10 2021

@author: shubh
"""
import chatbot
#import requests
import json


import random
greetings = ['hey', 'hello', 'hi', "it's great to see you", 'nice to see you', 'good to see you']
bye = ['Bye', 'Bye-Bye', 'Goodbye', 'Have a good day','Stop']
thank_you = ['thanks', 'thank you', 'thanks a bunch', 'thanks a lot.', 'thank you very much', 'thanks so much', 'thank you so much']
thank_response = ['You\'re welcome.' , 'No problem.', 'No worries.', ' My pleasure.' , 'It was the least I could do.', 'Glad to help.']
    # Example of how bot match the keyword from Greetings and reply accordingly
def bot_initialize(user_msg):
    flag=True
    while(flag==True):
        user_response = user_msg
        if(user_response not in bye):
            if(user_response == '/start'):
                bot_resp = """Hi, I'm Sova. I can tell you some info about covid""" 
                return bot_resp
            elif(user_response in thank_you):
                bot_resp = random.choice(thank_response)
                return bot_resp
            elif(user_response in greetings):
                bot_resp = random.choice(greetings) + ", What information you what related to Covid-19 in India"
                return bot_resp
            else:
                user_response = user_response.lower()
                bot_resp = chatbot.chatbot(user_response)
                #sent_tokens.remove(user_response)   # remove user question from sent_token that we added in sent_token in response() to find the Tf-Idf and cosine_similarity
                return bot_resp
        else:
            flag = False
            bot_resp = random.choice(bye)
            return bot_resp
class telegram_bot():
    def __init__(self):
        self.token = "1827438721:AAENDisATfkdVxDGu-TNN7c2-dSf-L5vAfQ"    #write your token here!
        self.url = f"https://api.telegram.org/bot{self.token}"
    def get_updates(self,offset=None):
            url = self.url+"/getUpdates?timeout=100"    # In 100 seconds if user input query then process that, use it as the read timeout from the server
            if offset:
                url = url+f"&offset={offset+1}"
            url_info = requests.get(url)
            return json.loads(url_info.content)
    def send_message(self,msg,chat_id):
            url = self.url + f"/sendMessage?chat_id={chat_id}&text={msg}"
            if msg is not None:
                requests.get(url)
#def grab_token(self):
        #return tokens
    
tbot = telegram_bot()
update_id = None
def make_reply(msg):     # user input will go here
  
    if msg is not None:
        reply = bot_initialize(msg)     # user input will start processing to bot_initialize function
    return reply
       
while True:
    print("...")
    updates = tbot.get_updates(offset=update_id)
    updates = updates['result']
    print(updates)
    
    if updates:
        for item in updates:
            print(item)
            update_id = item["update_id"]
            print(update_id)
            try:
                message = item["message"]["text"]
                print(message)
            except:
                message = None
            from_ = item["message"]["from"]["id"]
            print(from_)
        reply = make_reply(message)
        tbot.send_message(reply,from_)

#updates.pop()
