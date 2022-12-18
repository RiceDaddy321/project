import sqlite3

# connect to the database
db = sqlite3.connect("Notown.db")
cursor = db.cursor()

print('--------------------')
print('------Summary-------')
print('--------------------')


# A total number of musicians and a list of musicians.-----------
# Get the total number of musicians and a list of musicians
statement = "SELECT COUNT(DISTINCT Name) as count FROM Musicians"
res = cursor.execute(statement)
print('Number of total musicians: ' + str(res.fetchone()[0]))
print('------Musicians------')
statement = "SELECT DISTINCT(Name) FROM Musicians ORDER BY Name ASC"
res = cursor.execute(statement)
for row in res : print(row[0])
print('--------------------\n')

# A total number of albums and a list of albums recorded at Notown----
# Get the total number of albums and a list of albums recorded at Notown
statement = "SELECT COUNT(DISTINCT name) as count FROM Albums"
res = cursor.execute(statement)
print('Number of total Albums: ' + str(res.fetchone()[0]))
print('------Albums------')
statement = "SELECT DISTINCT(name) FROM Albums ORDER BY name ASC"
res = cursor.execute(statement)
for row in res : print(row[0])
print('--------------------\n')

# A total number of instruments and a list of instruments at Notown.----
# Get the total number of instruments and a list of instruments at Notown
statement = "SELECT COUNT(DISTINCT Type) as count FROM Instruments"
res = cursor.execute(statement)
print('Number of total Instruments: ' + str(res.fetchone()[0]))
print('------Instruments------')
statement = "SELECT DISTINCT(Type) FROM Instruments ORDER BY Type ASC"
res = cursor.execute(statement)
for row in res : print(row[0])
print('--------------------\n')

# A table consists of the name of musicians and the total number of albums written by them.
res = cursor.execute("""
SELECT Musicians.Name, COUNT(Musician_Album.album_id) AS num_albums
FROM Musicians
INNER JOIN Musician_Album ON Musicians.SSN = Musician_Album.SSN
GROUP BY Musicians.Name
""")
print('--------------------')
print('-Albums per musician-')
print('--------------------')
for row in res : print(str(row[0]) + " made " + str(row[1]) + " albums")
print('--------------------\n')
