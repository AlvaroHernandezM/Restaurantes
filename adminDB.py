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
	#print('columnas'+columns.replace('(','').replace(')',''))
	db.insert_value(c,table_name,columns,values)
	showTable(c,table_name,columns.replace('(','').replace(')',''))
	db.close(conn)

def createTableUsers(c):
	table_name = 'users'
	schema = 'id integer,edad integer,profesion integer'
	db.create_table(c, table_name, schema)
	showTable(c, table_name,'*')

def createTableKnowledge(c):
	table_name = 'knowledge'
	schema = 'id integer,name text,cuisine text,price text,rating real,meal_breakfast text,meal_lunch text,meal_dinner text,alcohol text,groups_goodfor text,accessible_wheelchair text'
	values = factual.filterTable(factual.chargeTable())
	db.create_table(c, table_name, schema)
	db.insert_values(c, table_name, values)
	showTable(c, table_name,'*')

def createTableCollective(c):
	table_name = 'collective'
	schema = 'edad integer, cuisine1 real, cuisine2 real, cuisine3 real, cuisine4 real, cuisine5 real, cuisine6 real, cuisine7 real, cuisine8 real, cuisine9 real, cuisine10 real, cuisine11 real'
	db.create_table(c, table_name, schema)
	showTable(c, table_name,'*')


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
	showTable(c, table_name,'*')


def showTable(c,table_name, columns):
	#db.total_rows(c, table_name, True)
	#db.table_col_info(c, table_name, True)
	db.show_table(c, table_name, True, columns)
	#db.consultCountNull(c, table_name, 'cuisine')
	#alcohol text,kids_goodfor text,groups_goodfor text,accessible_wheelchair text,options_vegetarian text,options_vegan text,options_glutenfree text,options_organic text,options_healthy text,options_lowfat

#createDB()