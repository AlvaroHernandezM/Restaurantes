import sqlite3

# Conexion Base de datos
def connect(sqlite_file):
    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()
    return conn, c

# Cierra y guarda los cambios en la BD
def close(conn):
    conn.commit()
    conn.close()

# Crea una tabla
def create_table(c, table_name, schema):
    c.execute('''CREATE TABLE {0} ({1});'''.format(table_name, schema))

# Se obtiene la informacion de las columnas
def table_col_info(c, table_name, print_out):
    c.execute('PRAGMA TABLE_INFO({})'.format(table_name))
    info = c.fetchall()
    if print_out:
        print("\nColumn Info:\nID, Name, Type, NotNull, DefaultVal, PrimaryKey")
        for col in info:
            print(col)
    return info

# Se obtiene el numero de columnas por tabla
def total_rows(c, table_name, print_out):
    c.execute('SELECT COUNT(*) FROM {}'.format(table_name))
    count = c.fetchall()
    if print_out:
        print('\nTotal rows: {}'.format(count[0][0]))
    return count[0][0]

# Se inserta una nueva tupla en la tabla
def insert_values(c, table_name, values):
    for row in values:
        c.execute('INSERT INTO {0} VALUES {1}'.format(table_name, str(row).replace('[', '(').replace(']', ')')))

def insert_value(c,table_name,columns,values):
    if  len(consult(c, table_name, 'id', values[0])) > 0:
        for x in range(len(values)):
            column = columns.replace('(','').replace(')','').split(', ')[x]
            #print('UPDATE {0} SET {1} = {2} WHERE id = {3}'.format(table_name, column, values[x], values[0]))
            c.execute('UPDATE {0} SET {1} = "{2}" WHERE id = {3}'.format(table_name, column, values[x], values[0]))
    else:
        c.execute('INSERT INTO {0} {1} VALUES {2}'.format(table_name,columns,str(values).replace('[', '(').replace(']', ')')))

#def insert_age(c,table_name,columns,values):
#    c.execute('INSERT OR IGNORE INTO {0} {1} VALUES {2}'.format(table_name,columns,str(values).replace('[', '(').replace(']', ')')))
#    c.execute('UPDATE {0} SET '.format(table_name,columns,str(values).replace('[', '(').replace(']', ')')))
# Se obtiene los datos almacenados en la tabla
def show_table(c, table_name, print_out, columns):
    data = []
    for row in c.execute('SELECT {1} FROM {0}'.format(table_name,columns)):
        data.append(row)
        if print_out:
            print(row)
    return data

def createViewRestaurants(c, table_name, parameter, value):
    c.execute("CREATE VIEW restaurants_view AS SELECT * FROM {0} WHERE {1} = {2}".format(table_name, parameter, value))

def dropView(c, view_name):
    try:
        c.execute('DROP VIEW {0}'.format(view_name))
    except:
        pass

def consult(c, table_name, parameter, value):
    data = []
    for row in c.execute("SELECT * FROM {0} WHERE {1} = {2}".format(table_name, parameter, value)):
        data.append(row)
    return data

def consult2(c, table_name, parameter1, value1, parameter2, value2):
    data = []
    for row in c.execute("SELECT * FROM {0} WHERE {1} = {2} AND {3} = {4}".format(table_name, parameter1, value1, parameter2, value2)):
        data.append(row)
    return data