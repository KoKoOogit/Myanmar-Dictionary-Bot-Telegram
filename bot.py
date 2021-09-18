import requests
from bs4 import BeautifulSoup
import telebot
import os

TOKEN = os.environ["TOKEN"]

bot = telebot.TeleBot(TOKEN)

def getMeaning(word):
    url = f"https://www.myordbok.com/definition?q={word}"
    webpage = requests.get(url)
    soup = BeautifulSoup(webpage.content,"html.parser")
    formatted = """"""
    try:
        meaningList = soup.find("div",class_="meaning")
        pos = meaningList.find_all("div",class_="pos")
        for i in pos:
            letter_type = i.find_all("h2")[0].getText()
            formatted += f"\n {letter_type} \n\n"
            text = i.find_all("p")
            for elem in text:
                myanmar_meaning = elem.getText()
                formatted += f"{myanmar_meaning}"       
    except:
        formatted = "Can't Find your words" 

    return formatted

@bot.message_handler(commands=['start','codingwithkko'])
def say_welcome(message):
    bot.reply_to(message,"Hello Welcome")

def type_some_word(message):
    return True

@bot.message_handler(func=type_some_word)
def get_meaning(message):
    bot.send_message(message.chat.id,getMeaning(message.text))

bot.polling()    