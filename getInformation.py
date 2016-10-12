from factual import Factual

def chargeTable():
	factual = Factual('CAwF4is1C94VkgCziGYxxdOXP419IJ3XVQ70JcZj', 'V22OLjDBfDjCdlJn52iQbKkA6NGDRYWKA3NBMK07')
	restaurants = factual.table('restaurants-us')
	return restaurants

def extractNeighborhood(neighborhoods):
	aux= ''
	for i,neighborhood in enumerate(neighborhoods):
			aux+=neighborhood+"-"
	return aux
def extractCuisine(cuisines):
	aux = ''
	for i,cuisine in enumerate(cuisines):
			aux+=cuisine+"-"
	return aux
def extractDay(hours, day):
	aux = ''
	for i,hour in enumerate(hours[day]):
		for result in hour:
			aux+='-'+result
#			print('Horas atención : '+result)
	aux+='*'
	return aux

def extractHours(hours):
	aux = ''
	for i,hour in enumerate(hours):
		aux+=hour
		aux+=extractDay(hours,hour)
		#print('Para el día: '+hour+' posicion '+str(i))
	return aux

#('name text,address text,neighborhood text[],region text,tel integer,cuisine text[],price text,rating real,payment_cashonly text,reservations text,hours text[][],open_24hrs text,attire text,parking text,smoking text,meal_breakfast text,meal_lunch text,meal_dinner text,meal_deliver text,meal_takeout text,meal_cater text,alcohol text,alcohol_bar text,alcohol_beer_wine text,alcohol_byob text,kids_goodfor text,kids_menu text,groups_goodfor text,accessible_wheelchair text,seating_outdoor text,wifi text,room_private text,options_vegetarian text,options_vegan text,options_glutenfree text,options_organic text,options_healthy text,options_lowfat text') 
#(text,text,text[],text,text,text[],text,real,text,text,text[][],text,text,text,text,text,text,text,text,text,text,text,text,text,text,text,text,text,text,text,text,text,text,text,text,text,text,text)


def filterTable(restaurants):
	data = restaurants.select('name,price,rating,payment_cashonly,open_24hrs,parking,smoking,meal_breakfast,meal_lunch,meal_dinner,alcohol,groups_goodfor,accessible_wheelchair').data()
	matriz= []
	for i, restaurant in enumerate(data):
		matriz.append([])
		matriz[i].append(i)
		matriz[i].append(restaurant['name']) if restaurant.get("name") != None else matriz[i].append('None')
		matriz[i].append(restaurant['price']) if restaurant.get("price") != None else matriz[i].append('None')
		matriz[i].append(restaurant['rating']) if restaurant.get("rating") != None else matriz[i].append('None')
		matriz[i].append(str(restaurant['payment_cashonly'])) if restaurant.get("payment_cashonly") != None else matriz[i].append('False')
		matriz[i].append(str(restaurant['open_24hrs'])) if restaurant.get("open_24hrs") != None else matriz[i].append('None')
		matriz[i].append(str(restaurant['parking'])) if restaurant.get("parking") != None else matriz[i].append('False')
		matriz[i].append(str(restaurant['smoking']))if restaurant.get("smoking") != None else matriz[i].append('False')
		matriz[i].append(str(restaurant['meal_breakfast'])) if restaurant.get("meal_breakfast") != None else matriz[i].append('False')
		matriz[i].append(str(restaurant['meal_lunch'])) if restaurant.get("meal_lunch") != None else matriz[i].append('False')
		matriz[i].append(str(restaurant['meal_dinner'])) if restaurant.get("meal_dinner") != None else matriz[i].append('False')
		matriz[i].append(str(restaurant['alcohol'])) if restaurant.get("alcohol") != None else matriz[i].append('False')
		matriz[i].append(str(restaurant['groups_goodfor'])) if restaurant.get("groups_goodfor") != None else matriz[i].append('False')
		matriz[i].append(str(restaurant['accessible_wheelchair'])) if restaurant.get("accessible_wheelchair") != None else matriz[i].append('False')
	return matriz