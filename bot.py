import pln
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler
import os

def listener(bot, update):
	id = update.message.chat_id
	message = (update.message.text).lower()
	#print('ID: ' + str(id) + ' MENSAJE: ' + message)
	#if message.lower() 
	option = identifiedOptionConversation(id)
	writeConversation(str(id),"user: "+message)
	if option == 0: #la respuesta hecha por el bot fue la edad
		filterAge(message, bot, id)
	else:
		if option == 1:
			filterProfesion(message,bot,id)
		else:
			if option == 2:
				filterHourFood(message,bot,id)
			else:
				if option == 3:
					filterTypeFood(message,bot,id)
				else:
					if option == 4:
						filterCountriFood(message,bot,id)
					else:
						if option == 5:
							filterCashOnly(message,bot,id)
						else:
							if option == 6:
								filterDisability(message,bot,id)
							else:
								if option == 7:
									filterParking(message,bot,id)
								else:
									if option == 8:
										filterSmoking(message,bot,id)
									else:
										if option == 9:
											filterAlcohol(message,bot,id)
										else:
											if option == 10:
												filterWithFriends(message,bot,id)
											else:
												bot.sendMessage(chat_id=id, text="No entender")
def filterWithFriends(message,bot,id):
	resultPln = pln.filterSignes(list(pln.clearEmptyWords(pln.separateText(message))))
	print (resultPln)
	bot.sendMessage(chat_id=id, text="Ha terminado la conversacion, te recomiendo")
	writeConversation(str(id),"bot: "+message.lower())
def filterAlcohol(message,bot,id):
	resultPln = pln.filterSignes(list(pln.clearEmptyWords(pln.separateText(message))))
	print (resultPln)
	message="¿Vas con amigos?"
	bot.sendMessage(chat_id=id, text="Y como última pregunta:")
	bot.sendMessage(chat_id=id, text=message)
	writeConversation(str(id),"bot: "+message.lower())
def filterSmoking(message,bot,id):
	resultPln = pln.filterSignes(list(pln.clearEmptyWords(pln.separateText(message))))
	print (resultPln)
	message="¿Tienes pensado tomar alcohol hoy?"
	bot.sendMessage(chat_id=id, text=message)
	writeConversation(str(id),"bot: "+message.lower())

def filterParking(message,bot,id):
	resultPln = pln.filterSignes(list(pln.clearEmptyWords(pln.separateText(message))))
	print (resultPln)
	message="¿Fumas?"
	bot.sendMessage(chat_id=id, text=message)
	writeConversation(str(id),"bot: "+message.lower())

def filterDisability(message,bot,id): #acesso para personas con discapacidad
	resultPln = pln.filterSignes(list(pln.clearEmptyWords(pln.separateText(message))))
	print (resultPln)
	message="¿Necesitas estacionamiento?"
	bot.sendMessage(chat_id=id, text=message)
	writeConversation(str(id),"bot: "+message.lower())

def filterCashOnly(message,bot,id):
	resultPln = pln.filterSignes(list(pln.clearEmptyWords(pln.separateText(message))))
	print (resultPln)
	message="¿Tienes alguna discapacidad o vas en compañía de alguien en esta condición?"
	bot.sendMessage(chat_id=id, text="Para una mejor comodidad:")
	bot.sendMessage(chat_id=id, text=message)
	writeConversation(str(id),"bot: "+message.lower())

def filterCountriFood(message,bot,id):
	resultPln = pln.filterSignes(list(pln.clearEmptyWords(pln.separateText(message))))
	print (resultPln)
	message="¿Pagaras en efectivo o con algún tipo tarjeta?"
	bot.sendMessage(chat_id=id, text="Unas preguntas más:")
	bot.sendMessage(chat_id=id, text=message)
	writeConversation(str(id),"bot: "+message.lower())

def filterTypeFood(message,bot,id):
	resultPln = pln.filterSignes(list(pln.clearEmptyWords(pln.separateText(message))))
	print (resultPln)
	message="¿Disfrutas más la comida de algún país en especial?"
	bot.sendMessage(chat_id=id, text="¡Me antoje!")
	bot.sendMessage(chat_id=id, text=message)
	writeConversation(str(id),"bot: "+message.lower())

def filterProfesion(message, bot, id):
	resultPln = pln.filterSignes(list(pln.clearEmptyWords(pln.separateText(message))))
	print (resultPln)
	message="¿Quieres desayuno, almuerzo o cena?"
	bot.sendMessage(chat_id=id, text="¡Muy buena profesión!, para tener más certeza:")
	bot.sendMessage(chat_id=id, text=message)
	writeConversation(str(id),"bot: "+message.lower())

def filterHourFood(message, bot, id):
	resultPln = pln.filterSignes(list(pln.clearEmptyWords(pln.separateText(message))))
	print (resultPln)
	message="¿Cuál es el tipo de comida que más te gusta?"
	bot.sendMessage(chat_id=id, text="Ahora dime:")
	bot.sendMessage(chat_id=id, text=message)
	writeConversation(str(id),"bot: "+message.lower())

def readLastMessageConversation(id): #retornar la ultima linea del archivo que tiene creado para el usuario
	return readLastLineConversation(str(id))[len(readLastLineConversation(str(id)))-1].lower().replace('bot: ','').replace(' ','').replace('\n','')



def isValidateAge(age):
	return True if age>=15 and age<=100 else False

def filterAge(message, bot, id):
	resultPln = pln.filterSignes(list(pln.clearEmptyWords(pln.separateText(message))))
	if(isOneDigit(resultPln)):
		value = int(resultPln[0])
		if(isValidateAge(value)):#es un rango de edad valido?
			#se debe asginar el valor difurso con este valor que es un solo digito     
			print('falta hallar valor difuso para: '+str(value))
			#se continua con la conversación porque ya tomo el valor difuso
			message="¿Cuál es tu profesión o qué haces a diario?"
			bot.sendMessage(chat_id=id, text="¡Que bien! y cuentame:")
			bot.sendMessage(chat_id=id, text=message)
			writeConversation(str(id),"bot: "+message.lower())
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
				value = int(firstDigit(resultPln))
				print('falta hallar valor difuso para: '+str(value))
				#se continua con la conversación porque ya tomo el valor difuso
				message="¿Cuál es tu profesión o qué haces a diario?"
				bot.sendMessage(chat_id=id, text="¡Que bien! y cuentame:")
				bot.sendMessage(chat_id=id, text=message)
				writeConversation(str(id),"bot: "+message.lower())
		else: 
			#no se esta reconociendo ningun digito pero esta palabra paso el pln
			#print(resultPln)
			message="¿Qué edad tienes?"
			bot.sendMessage(chat_id=id, text="¡Ops, lo siento pero aún no se reconoce la fecha por texto, ingresa tu edad como un número!")
			bot.sendMessage(chat_id=id, text=message)
			writeConversation(str(id),"bot: "+message.lower())

def firstDigit(resultPln):
	for word in resultPln:
		if (word.isdigit()):
			return word
	return 'None'
def isOneDigit(resultPln):
	return len(findDigits(resultPln)) ==1 and len(resultPln) == 1

def isOnlyDigits(resultPln):
	return len(findDigits(resultPln))==len(resultPln)

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

def identifiedOptionConversation(id): #retorna el identificador para cada 
	lastMessage=readLastMessageConversation(id)
	print(lastMessage)
	if lastMessage=='¿quéedadtienes?':
		return 0
	else:
		if lastMessage =='¿cuálestuprofesiónoquéhacesadiario?':
			return 1
		else:
			if lastMessage =='¿quieresdesayuno,almuerzoocena?':
				return 2
			else:
				if lastMessage =='¿cuáleseltipodecomidaquemástegusta?':
					return 3
				else:
					if lastMessage =='¿disfrutasmáslacomidadealgúnpaísenespecial?':
						return 4
					else:
						if lastMessage =='¿pagarasenefectivooconalgúntipotarjeta?':
							return 5
						else:
							if lastMessage =='¿tienesalgunadiscapacidadovasencompañíadealguienenestacondición?':
								return 6
							else:
								if lastMessage =='¿necesitasestacionamiento?':
									return 7
								else:
									if lastMessage =='¿fumas?':
										return 8
									else:
										if lastMessage =='¿tienespensadotomaralcoholhoy?':
											return 9
										else:
											if lastMessage =='¿vasconamigos?':
												return 10
											else:
												return 11	

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