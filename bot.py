from telegram.ext import Updater, MessageHandler, Filters, CommandHandler
import os

#Estados de animo
triste = ['triste', 'deprimido', 'afligido', 'apenado', 'entristecido', 'apesadumbrado', 'atribulado', 'pesaroso', 'mohíno', 'mustio', 'taciturno', 'compungido', 'lloroso', 'cariacontecido']
feliz = ['feliz', 'bien', 'dichoso', 'contento', 'satisfecho', 'alegre', 'boyante', 'próspero', 'afortunado', 'ufano', 'radiante', 'bienaventurado']
enamorado = ['enamorado', 'seducido', 'prendado', 'chalado', 'pretendiente', 'cortejador', 'galán', 'amado', 'colado', 'encelado', 'flechado', 'rendido', 'afectuoso', 'cariñoso', 'amartelado', 'amoroso']
aburrido = ['aburrido', 'desganado', 'hastiado', 'inapetente', 'cansado', 'desanimado', 'fastidiado', 'harto', 'mamado']
molesto = ['puto','molesto', 'mal', 'fastidioso', 'incómodo', 'incomodo', 'enojado', 'pesado', 'latoso', 'engorroso', 'trabajoso', 'desagradable', 'inoportuno']
pensativo = ['pensativo', 'absorto', 'reflexivo', 'abstraído', 'abstraido', 'preocupado']



generos = {}

generos['vallenato'] = {}
generos['vallenato'] = ({
    'triste' : 'https://www.youtube.com/watch?v=4czHAzh5xbk',
    'feliz' : 'https://www.youtube.com/watch?v=tS34TijiFiM',
    'enamorado' : 'https://www.youtube.com/watch?v=DR6ED6lvkb4',
    'aburrido' : 'https://www.youtube.com/watch?v=plNpwHuFgcg',
    'molesto' : 'https://www.youtube.com/watch?v=_Bh-6rWoRm4',
    'pensativo' : 'https://www.youtube.com/watch?v=34K2dYw_od8'
    })

generos['pop'] = {}
generos['pop'] = ({
    'triste' : 'https://www.youtube.com/watch?v=iErljjjqT5c',
    'feliz' : 'https://www.youtube.com/watch?v=gDWNLEB28iQ',
    'enamorado' : 'https://www.youtube.com/watch?v=lsbqH5bJURc',
    'aburrido' : 'https://www.youtube.com/watch?v=_55XQiq6yr4',
    'molesto' : 'https://www.youtube.com/watch?v=LgI2zJ3Ft0U',
    'pensativo' : 'https://www.youtube.com/watch?v=Wy4giA4e21M'
    })

generos['salsa'] = {}
generos['salsa'] = ({
    'triste' : 'https://www.youtube.com/watch?v=sUurtHFVFUA',
    'feliz' : 'https://www.youtube.com/watch?v=uN0rmmreopE',
    'enamorado' : 'https://www.youtube.com/watch?v=3VmoZrxXbmg',
    'aburrido' : 'https://www.youtube.com/watch?v=TxRWQHCSmUg',
    'molesto' : 'https://www.youtube.com/watch?v=Tsqt-0fE78c',
    'pensativo' : 'https://www.youtube.com/watch?v=7kbjKCj-rMQ'
    })

generos['rock'] = {}
generos['rock'] = ({
    'triste' : 'https://www.youtube.com/watch?v=VlMEGBsw6j8',
    'feliz' : 'https://www.youtube.com/watch?v=XPpTgCho5ZA',
    'enamorado' : 'https://www.youtube.com/watch?v=09R8_2nJtjg',
    'aburrido' : 'https://www.youtube.com/watch?v=plNpwHuFgcg',
    'molesto' : 'https://www.youtube.com/watch?v=iEPTlhBmwRg',
    'pensativo' : 'https://www.youtube.com/watch?v=NmugSMBh_iI'
    })



def listener(bot, update):
    id = update.message.chat_id
    message = update.message.text
    print('ID: ' + str(id) + ' MENSAJE: ' + message)

    if message.lower() in triste:
        bot.sendMessage(chat_id=update.message.chat_id, text='Lo mejor es desahogarse')
        bot.sendMessage(chat_id=update.message.chat_id, text='Deberias escuchar algo, ¿Qué genero te gusta más?')
        file('triste')
    elif message.lower() in feliz:
        bot.sendMessage(chat_id=update.message.chat_id, text='Tenemos que celebrar')
        bot.sendMessage(chat_id=update.message.chat_id, text='Deberias escuchar algo, ¿Qué genero te gusta más?')
        file('feliz')
    elif message.lower() in enamorado:
        bot.sendMessage(chat_id=update.message.chat_id, text='Uyyyyyyyy')
        bot.sendMessage(chat_id=update.message.chat_id, text='Deberias escuchar algo, ¿Qué genero te gusta más?')
        file('enamorado')
    elif message.lower() in aburrido:
        bot.sendMessage(chat_id=update.message.chat_id, text='Tenemos que hacer algo. Vamo a bailar')
        bot.sendMessage(chat_id=update.message.chat_id, text='Deberias escuchar algo, ¿Qué genero te gusta más?')
        file('aburrido')
    elif message.lower() in molesto:
        bot.sendMessage(chat_id=update.message.chat_id, text='Piensa en otra cosa')
        bot.sendMessage(chat_id=update.message.chat_id, text='Deberias escuchar algo, ¿Qué genero te gusta más?')
        file('molesto')
    elif message.lower() in pensativo:
        bot.sendMessage(chat_id=update.message.chat_id, text='Tienes que aclarar tu mente')
        bot.sendMessage(chat_id=update.message.chat_id, text='Deberias escuchar algo, ¿Qué genero te gusta más?')
        file('pensativo')
    elif message.lower() in generos:
        bot.sendMessage(chat_id=update.message.chat_id, text='Escucha esta canción')
        bot.sendMessage(chat_id=update.message.chat_id, text=generos[message.lower()].get(file('')))
    else:
        bot.sendMessage(chat_id=update.message.chat_id, text='No entiendo')


def start(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text='Hola')
    bot.sendMessage(chat_id=update.message.chat_id, text='¿Como estas?')

def file(state):
    if state == '':
        file = open('estado', 'r') 
        data = file.read()
        file.close()
        return data
    else:
        file = open('estado', 'w')
        file.write(state)
        file.close()

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