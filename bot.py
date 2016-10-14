import pln
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler
import os
import re


def listener(bot, update):
    id = update.message.chat_id
    message = update.message.text
    #print('ID: ' + str(id) + ' MENSAJE: ' + message)
    #if message.lower() 
    
    if (readLastMessageConversation(id) == '¿cuálestuedad?'):
        filterAge(message.lower())
    else :
        bot.sendMessage(chat_id=id, text="No entender")
    writeConversation(str(id),"user: "+message)
 #   if message.lower() :
 #   else:
 #       bot.sendMessage(chat_id=update.message.chat_id, text='No entiendo')

def readLastMessageConversation(id):
    return readLastLineConversation(str(id))[len(readLastLineConversation(str(id)))-1].lower().replace('bot: ','').replace(' ','').replace('\n','')
     

def filterAge(message):
    patron = re.compile('(?:\d*)?\d+')
    resultPln = pln.filterSignes(list(pln.clearEmptyWords(pln.separateText(message))))
    print('resultado: '+resultPln)
    if((len(resultPln)) ==1):
        if(resultPln[0].isdigit()): #es un digito , se debe asignar el valor diguso

        else: #verificar que este en la lista de letras numeros

    else:
        #pendiente




def start(bot, update):
    id = update.message.chat_id
    user = update.message.from_user
    message = '¿Cuál es tu edad?'
    bot.sendMessage(chat_id=update.message.chat_id, text='Hola, '+user.first_name+", me alegra saludarte.")
    bot.sendMessage(chat_id=update.message.chat_id, text=message)
    writeConversation(str(id),"bot: "+message)

def writeConversation(id,message):
    file = open(id, 'a')
    file.write(message+'\n')
    file.close()

def readLastLineConversation(id):
    file = open(id, 'r') 
    data = file.readlines()
    file.close()
    return data

def main():
    updater = Updater('205961193:AAE4XZ9K6VcdfnzM7DvTuI1JsIF_SVKQ_Fo')
    dispatcher = updater.dispatcher
    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)
    listener_handler = MessageHandler([Filters.text], listener)
    dispatcher.add_handler(listener_handler)
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()