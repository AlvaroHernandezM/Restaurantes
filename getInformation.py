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
	data = restaurants.select('name,address,neighborhood,region,tel,cuisine,price,rating,payment_cashonly,reservations,hours,open_24hrs,attire,parking,smoking,meal_breakfast,meal_lunch,meal_dinner,meal_deliver,meal_takeout,meal_cater,alcohol,alcohol_bar,alcohol_beer_wine,alcohol_byob,kids_goodfor,kids_menu,groups_goodfor,accessible_wheelchair,seating_outdoor,wifi,room_private,options_vegetarian,options_vegan,options_glutenfree,options_organic,options_healthy,options_lowfat').data()
	matriz= []
	for i, restaurant in enumerate(data):
		matriz.append([])
		matriz[i].append(restaurant['name']) if restaurant.get("name") != None else matriz[i].append('None')
		matriz[i].append(restaurant['address']) if restaurant.get("address") != None else matriz[i].append('None')
		matriz[i].append(extractNeighborhood(restaurant['neighborhood'])) if restaurant.get("neighborhood") != None else matriz[i].append('None')
		matriz[i].append(restaurant['region']) if restaurant.get("region") != None else matriz[i].append('None')
		matriz[i].append(restaurant['tel']) if restaurant.get("tel") != None else matriz[i].append('None')
		matriz[i].append(extractCuisine(restaurant['cuisine'])) if restaurant.get("cuisine") != None else matriz[i].append('None')
		matriz[i].append(restaurant['price']) if restaurant.get("price") != None else matriz[i].append('None')
		matriz[i].append(restaurant['rating']) if restaurant.get("rating") != None else matriz[i].append('None')
		matriz[i].append(str(restaurant['payment_cashonly'])) if restaurant.get("payment_cashonly") != None else	matriz[i].append('None')
		matriz[i].append(str(restaurant['reservations'])) if restaurant.get("reservations") != None else matriz[i].append('None')
		matriz[i].append(extractHours(restaurant['hours'])) if restaurant.get("hours") != None else matriz[i].append('None')
		matriz[i].append(str(restaurant['open_24hrs'])) if restaurant.get("open_24hrs") != None else matriz[i].append('None')
		matriz[i].append(restaurant['attire']) if restaurant.get("attire") != None else matriz[i].append('None')
		matriz[i].append(str(restaurant['parking'])) if restaurant.get("parking") != None else matriz[i].append('None')
		matriz[i].append(str(restaurant['smoking']))if restaurant.get("smoking") != None else matriz[i].append('None')
		matriz[i].append(str(restaurant['meal_breakfast'])) if restaurant.get("meal_breakfast") != None else matriz[i].append('None')
		matriz[i].append(str(restaurant['meal_lunch'])) if restaurant.get("meal_lunch") != None else matriz[i].append('None')
		matriz[i].append(str(restaurant['meal_dinner'])) if restaurant.get("meal_dinner") != None else matriz[i].append('None')
		matriz[i].append(str(restaurant['meal_deliver'])) if restaurant.get("meal_deliver") != None else	matriz[i].append('None')
		matriz[i].append(str(restaurant['meal_takeout'])) if restaurant.get("meal_takeout") != None else	matriz[i].append('None')
		matriz[i].append(str(restaurant['meal_cater'])) if restaurant.get("meal_cater") != None else	matriz[i].append('None')
		matriz[i].append(str(restaurant['alcohol'])) if restaurant.get("alcohol") != None else matriz[i].append('None')
		matriz[i].append(str(restaurant['alcohol_bar'])) if restaurant.get("alcohol_bar") != None else matriz[i].append('None')
		matriz[i].append(str(restaurant['alcohol_beer_wine'])) if restaurant.get("alcohol_beer_wine") != None else matriz[i].append('None')
		matriz[i].append(str(restaurant['alcohol_byob'])) if restaurant.get("alcohol_byob") != None else matriz[i].append('None')
		matriz[i].append(str(restaurant['kids_goodfor'])) if restaurant.get("kids_goodfor") != None else matriz[i].append('None')
		matriz[i].append(str(restaurant['kids_menu'])) if restaurant.get("kids_menu") != None else matriz[i].append('None')
		matriz[i].append(str(restaurant['groups_goodfor'])) if restaurant.get("groups_goodfor") != None else matriz[i].append('None')
		matriz[i].append(str(restaurant['accessible_wheelchair'])) if restaurant.get("accessible_wheelchair") != None else matriz[i].append('None')
		matriz[i].append(str(restaurant['seating_outdoor'])) if restaurant.get("seating_outdoor") != None else matriz[i].append('None')
		matriz[i].append(str(restaurant['wifi'])) if restaurant.get("wifi") != None else matriz[i].append('None')
		matriz[i].append(str(restaurant['room_private'])) if restaurant.get("room_private") != None else matriz[i].append('None')
		matriz[i].append(str(restaurant['options_vegetarian'])) if restaurant.get("options_vegetarian") != None 	else matriz[i].append('None')
		matriz[i].append(str(restaurant['options_vegan'])) if restaurant.get("options_vegan") != None else matriz[i].append('None')
		matriz[i].append(str(restaurant['options_glutenfree'])) if restaurant.get("options_glutenfree") != None else matriz[i].append('None')
		matriz[i].append(str(restaurant['options_organic'])) if restaurant.get("options_organic") != None else matriz[i].append('None')
		matriz[i].append(str(restaurant['options_healthy'])) if restaurant.get("options_healthy") != None else matriz[i].append('None')
		matriz[i].append(str(restaurant['options_lowfat'])) if restaurant.get("options_lowfat") != None else matriz[i].append('None')
	return matriz