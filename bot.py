import pln
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler
import os
import re


def listener(bot, update):
	id = update.message.chat_id
	message = (update.message.text).lower()
	#print('ID: ' + str(id) + ' MENSAJE: ' + message)
	#if message.lower() 
	option = identifiedOptionConversation(id)
	writeConversation(str(id),"user: "+message)
	if option == 0: #se debe preguntar la edad de nuevo
		filterAge(message, bot, id)
	else:
		bot.sendMessage(chat_id=id, text="No entender")
	
 #   if message.lower() :
 #   else:
 #       bot.sendMessage(chat_id=update.message.chat_id, text='No entiendo')

def readLastMessageConversation(id): #retornar la ultima linea del archivo que tiene creado para el usuario
	return readLastLineConversation(str(id))[len(readLastLineConversation(str(id)))-1].lower().replace('bot: ','').replace(' ','').replace('\n','')

def identifiedOptionConversation(id): #retorna el identificador para cada 
	lastMessage=readLastMessageConversation(id)
	print(lastMessage)
	if lastMessage=='¿quéedadtienes?':
		return 0
	else:
		return 1

def isValidateAge(age):
	return True if age>=15 and age<=100 else False

def filterAge(message, bot, id):
	patron = re.compile('(?:\d*)?\d+')
	resultPln = pln.filterSignes(list(pln.clearEmptyWords(pln.separateText(message))))
	if(isOneDigit(resultPln)):
		value = int(resultPln[0])
		if(isValidateAge(value)):#es un rango de edad valido?
			#se debe asginar el valor difurso con este valor que es un solo digito     
			print('valor difuso para: '+str(value))
		else:
			message="¿Qué edad tienes?"
			bot.sendMessage(chat_id=id, text="¡Ops, tu edad no se encuentra en el rango de 15-100 años, ingresa tu edad correctamente!")
			bot.sendMessage(chat_id=id, text=message)
			writeConversation(str(id),"bot: "+message.lower())
	else:
		if(len(findDigits(resultPln))>0):#se verifica si si tiene digitos
			if(isOnlyDigits(resultPln)):#se verifica que solos ean digitos
				#se encontro mas de un numero por lo que se deberia notificar el usuario que digite d enuev
				message="¿Qué edad tienes?"
				bot.sendMessage(chat_id=id, text="¡Ops, cuando ingresas más de una cadena de números no puedo identificar tu edad, vuelve a intentarlo!")
				bot.sendMessage(chat_id=id, text=message)
				writeConversation(str(id),"bot: "+message.lower())
			else:#se extrae el primero valor digito de todos los texto
				print('digito encontrado')
				print(firstDigit(resultPln))
		else: 
			#no se esta reconociendo ningun digito pero esta palabra paso el pln
			print(resultPln)

def firstDigit(resultPln):
	for word in resultPln:
		if (word.isdigit()):
			return word
	return 'None'
def isOneDigit(resultPln):
	return (len(findDigits(resultPln)) ==1 and len(resultPln) == 1) 

def isOnlyDigits(resultPln):
	return (len(findDigits(resultPln)) ==len(resultPln)) 

def findDigits(resultPln):
	words = []
	for word in resultPln:
		if (word.isdigit()):
			words.append(word)
	return words

def start(bot, update):
	id = update.message.chat_id
	user = update.message.from_user
	message = '¿qué edad tienes?'
	bot.sendMessage(chat_id=update.message.chat_id, text='¡Hola '+user.first_name+'! Bienvenido al Sistema Recomendador de Restaurantes. Para empezar:')
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