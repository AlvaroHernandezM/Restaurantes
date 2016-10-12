import getInformation as factual
import database as db

sqlite_file = 'knowledge.db'
conn, c = db.connect(sqlite_file)
table_name = 'restaurants'
schema = 'id integer,name text,address text,neighborhood text,region text,tel integer,cuisine text,price text,rating real,payment_cashonly text,reservations text,hours text,open_24hrs text,attire text,parking text,smoking text,meal_breakfast text,meal_lunch text,meal_dinner text,meal_deliver text,meal_takeout text,meal_cater text,alcohol text,alcohol_bar text,alcohol_beer_wine text,alcohol_byob text,kids_goodfor text,kids_menu text,groups_goodfor text,accessible_wheelchair text,seating_outdoor text,wifi text,room_private text,options_vegetarian text,options_vegan text,options_glutenfree text,options_organic text,options_healthy text,options_lowfat text'
values = factual.filterTable(factual.chargeTable())
db.create_table(c, table_name, schema)
db.insert_value(c, table_name, values)
db.total_rows(c, table_name, True)
db.table_col_info(c, table_name, True)
db.show_table(c, table_name, True)
db.close(conn)