from telegram.ext import Updater, MessageHandler, Filters, CommandHandler
import os

def listener(bot, update):
    id = update.message.chat_id
    message = update.message.text
    #print('ID: ' + str(id) + ' MENSAJE: ' + message)
    #if message.lower() 
    print(readLastLineConversation(str(id))[len(readLastLineConversation(str(id)))-1].replace('user: ',''))

    writeConversation(str(id),"user: "+message+"\n")
 #   if message.lower() :
 #   else:
 #       bot.sendMessage(chat_id=update.message.chat_id, text='No entiendo')


def start(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text='Hola')
    bot.sendMessage(chat_id=update.message.chat_id, text='¿Cuál es tu edad?')

def writeConversation(id,message):
    file = open(id, 'a')
    file.write(message)
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