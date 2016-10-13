import getInformation as factual
import database as db

def createDB():
	sqlite_file = 'botRestaurants.db'
	conn, c = db.connect(sqlite_file)
	createTableKnowledge(c)
	createTableCollective(c)
	createTableExpert(c)
	db.close(conn)

def createTableKnowledge(c):
	table_name = 'knowledge'
	schema = 'id integer,name text,cuisine text,price text,rating real,payment_cashonly text,open_24hrs text,parking text,smoking text,meal_breakfast text,meal_lunch text,meal_dinner text,alcohol text,groups_goodfor text,accessible_wheelchair text'
	values = factual.filterTable(factual.chargeTable())
	db.create_table(c, table_name, schema)
	db.insert_value(c, table_name, values)
	showTable(c, table_name)

def createTableCollective(c):
	table_name = 'collective'
	schema = 'cuisine text,edad integer'
	db.create_table(c, table_name, schema)
	showTable(c, table_name)


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
	db.insert_value(c, table_name, values)
	showTable(c, table_name)


def showTable(c,table_name):
	#db.total_rows(c, table_name, True)
	#db.table_col_info(c, table_name, True)
	db.show_table(c, table_name, True)
	#db.consultCountNull(c, table_name, 'cuisine')
#alcohol text,kids_goodfor text,groups_goodfor text,accessible_wheelchair text,options_vegetarian text,options_vegan text,options_glutenfree text,options_organic text,options_healthy text,options_lowfat

createDB()