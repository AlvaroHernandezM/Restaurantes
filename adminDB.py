import getInformation as factual
import database as db

def createDB():
	sqlite_file = 'botRestaurants.db'
	conn, c = db.connect(sqlite_file)
	try:
		createTableKnowledge(c)
		createTableCollective(c)
		createTableExpert(c)
		createTableUsers(c)
	except:
		pass
	db.close(conn)

def insertValue(columns,table_name,values):
	sqlite_file = 'botRestaurants.db'
	conn, c = db.connect(sqlite_file)
	db.insert_value(c,table_name,columns,values)
	db.close(conn)

def getRangeAge(value):
	sqlite_file = 'botRestaurants.db'
	table_name = 'users'
	parameter = 'id'
	conn, c = db.connect(sqlite_file)
	data = db.consult(c, table_name, parameter, value)
	db.close(conn)
	return data[0][2]

def getRangePrice(value1, value2):
	sqlite_file = 'botRestaurants.db'
	table_name = 'expert'
	parameter1 = 'profesion'
	parameter2 = 'edad'
	conn, c = db.connect(sqlite_file)
	data = db.consult2(c, table_name, parameter1, value1, parameter2, value2)
	db.close(conn)
	return data[0][0]

def getRestaurantsPrice(value):
	sqlite_file = 'botRestaurants.db'
	table_name = 'knowledge'
	parameter = 'price'
	conn, c = db.connect(sqlite_file)
	try:
		dropRestaurantsView()
	except:
		pass
	db.createViewRestaurants(c, table_name, parameter, value)
	data = db.consult(c, table_name, parameter, value)
	db.close(conn)
	return data

def getRestaurants(parameter, value):
	sqlite_file = 'botRestaurants.db'
	table_name = 'restaurants_view'
	conn, c = db.connect(sqlite_file)
	db.updateViewRestaurants(c, parameter, value)
	data = db.show_table(c, table_name, False, '*')
	db.close(conn)
	return data

def dropRestaurantsView():
	sqlite_file = 'botRestaurants.db'
	conn, c = db.connect(sqlite_file)
	viewName = 'restaurants_view'
	db.dropView(c, viewName)
	db.close(conn)

def createTableUsers(c):
	table_name = 'users'
	schema = 'id integer, edad integer, rangoEdad integer, profesion text, rangoProfesion integer'
	db.create_table(c, table_name, schema)
	#showTable(c, table_name,'*')

def createTableKnowledge(c):
	table_name = 'knowledge'
	schema = 'id integer,name text,cuisine text,price text,rating real,meal_breakfast text,meal_lunch text,meal_dinner text,alcohol text,groups_goodfor text,accessible_wheelchair text'
	values = factual.filterTable(factual.chargeTable())
	db.create_table(c, table_name, schema)
	db.insert_values(c, table_name, values)
	#showTable(c, table_name,'*')

def createTableCollective(c):
	table_name = 'collective'
	schema = 'edad integer, cuisine1 real, cuisine2 real, cuisine3 real, cuisine4 real, cuisine5 real, cuisine6 real, cuisine7 real, cuisine8 real, cuisine9 real, cuisine10 real, cuisine11 real'
	db.create_table(c, table_name, schema)
	#showTable(c, table_name,'*')


def createTableExpert(c):
	table_name = 'expert'
	schema = 'precio integer,profesion integer,edad integer'
	values = [[3,1,1],
			[4,1,2],
			[5,1,3],
			[2,2,1],
			[3,2,2],
			[4,2,3],
			[2,3,1],
			[3,3,2],
			[4,3,3],
			[1,4,1],
			[3,4,2],
			[3,4,3],
			[1,5,1],
			[1,5,2],
			[1,5,3]
			]
	db.create_table(c, table_name, schema)
	db.insert_values(c, table_name, values)
	#showTable(c, table_name,'*')


def showTableRestaurants():
	sqlite_file = 'botRestaurants.db'
	table_name = 'restaurants_view'
	conn, c = db.connect(sqlite_file)
	columns = '*'
	#db.total_rows(c, table_name, True)
	#db.table_col_info(c, table_name, True)
	return db.show_table(c, table_name, False, columns)
def showTable(c,table_name, columns):
	#db.total_rows(c, table_name, True)
	#db.table_col_info(c, table_name, True)
	db.show_table(c, table_name, True, columns)
	#db.consultCountNull(c, table_name, 'cuisine')
	#alcohol text,kids_goodfor text,groups_goodfor text,accessible_wheelchair text,options_vegetarian text,options_vegan text,options_glutenfree text,options_organic text,options_healthy text,options_lowfat

#print(showTableRestaurants())

