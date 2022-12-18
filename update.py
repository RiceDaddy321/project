import argparse
import sqlite3

parser = argparse.ArgumentParser()
db = sqlite3.connect("Notown.db")
cursor = db.cursor()

# possible arguments
parser.add_argument("--add", action="store_true", help="Add a row to the database")
parser.add_argument("--del", action="store_true", help="del a row from the database")
parser.add_argument('--table',type=str,help='the target table in the database')
parser.add_argument("--record",type=str, help="Comma seperated values to insert into the database")

args = parser.parse_args()
my_args = vars(args)

if not my_args['record']:
    parser.error("You forgot the '--record' argument!")

values = my_args['record'].split(',')

if not my_args['add'] and not my_args['del'] or my_args['add'] and my_args['del'] :
    parser.error("You need to specify if you are adding (--add) or deleting (--del) a record!")

if not my_args['table']:
    parser.error("You need to specify a table (--table) to do an operation with!")

if my_args['add']:
    statement = "INSERT INTO " + my_args['table'] + " VALUES("
    for value in values:
        statement += "?,"

    statement = statement[:-1] + ")"
    # Add a row to the database
    try:
        cursor.execute(statement,values)
        if cursor.rowcount == 0:
            print("No rows were added.")
        else:
            print("{} rows were added.".format(cursor.rowcount))
    except sqlite3.Error as e:
        print("You made a mistake:", e.args[0])
    
elif my_args['del']:
    res = cursor.execute("select * from "+ my_args['table'] + " where 0=1")

    columns = res.description

    statement = "DELETE FROM " + my_args['table'] + " WHERE "

    for i in range(len(columns)):
        statement += columns[i][0] + '=' +"'"+ str(values[i] +"'")
        if i != len(columns)-1:
            statement += " AND "

    # del a row from the database
    try:
        cursor.execute(statement)
        if cursor.rowcount == 0:
            print("No rows were deleted.")
        else:
            print("{} rows were deleted.".format(cursor.rowcount))
    except sqlite3.Error as e:
        print("You made a mistake:", e.args[0])


db.commit()
db.close()