import sqlite3
import csv

# connect to the database
db = sqlite3.connect("Notown.db")

cursor = db.cursor()

#delete the tables if they exist already
cursor.execute("DROP TABLE IF EXISTS Musicians")

# create the Musicians table
cursor.execute("CREATE TABLE if not exists Musicians (SSN string PRIMARY KEY, Name string, Str_type string, Street string, Num integer)")

# import data from the musician.csv file
with open('musician.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        cursor.execute("INSERT INTO Musicians VALUES (?, ?, ?, ?, ?)", (row['ssn'], row['name'], row['str_type'], row['street'], row['num']))


#delete the tables if they exist already
cursor.execute("DROP TABLE IF EXISTS Instruments")

# create the Instruments table
cursor.execute("CREATE TABLE if not exists Instruments (id integer PRIMARY KEY, Type string, Key string)")

# import data from the instrument.csv file
with open('instrument.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        cursor.execute("INSERT INTO Instruments VALUES (?, ?, ?)", (row['id'], row['type'], row['key']))


#delete the tables if they exist already
cursor.execute("DROP TABLE IF EXISTS Albums")

# create the Albums table
cursor.execute("CREATE TABLE if not exists Albums (name string, id integer PRIMARY KEY, date string, type string)")

# import data from the album.csv file
with open('album.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        cursor.execute("INSERT INTO Albums VALUES (?, ?, ?, ?)", (row['Name'], row['id'], row['date'], row['type']))


#delete the tables if they exist already
cursor.execute("DROP TABLE IF EXISTS Musician_Album")

# create the Musician_Album table
cursor.execute("CREATE TABLE if not exists Musician_Album (SSN string, album_id integer, FOREIGN KEY (SSN) REFERENCES Musicians(SSN), FOREIGN KEY (album_id) REFERENCES Albums(id))")

# import data from the Musician_Album.csv file
with open('musician-album.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        cursor.execute("INSERT INTO Musician_Album VALUES (?, ?)", (row['ssn'], row['album_id']))


#delete the tables if they exist already
cursor.execute("DROP TABLE IF EXISTS Album_Instrument")

# create the Album_Instrument table
cursor.execute("CREATE TABLE if not exists Album_Instrument (album_id integer, instrument_id integer, FOREIGN KEY (album_id) REFERENCES Albums(id), FOREIGN KEY (instrument_id) REFERENCES Instruments(id))")

# import data from the album-instrument.csv file
with open('album-instrument.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        cursor.execute("INSERT INTO Album_Instrument VALUES (?, ?)", (row['album_id'], row['instrument_id']))
cursor.connection.commit()
cursor.close()
