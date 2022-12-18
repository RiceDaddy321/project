0: Ensure that all of the files that were included in the zip file are present in the same directory
before continuing.
0.5: Navigate to the folder where you extracted the files to.
1: Run task.py with the command `python task.py`, which will create the database,
and it will drop the table with the same name in the database if it exists
2: For a summary run `python summary.py`, which prints the summary into the terminal
3: update.py needs to be ran in the following format: 
`python update.py --[add][del] --table [tablename] --record "Comma,Separated,values"
4: Follow this format for each of the tables when doing any operations with them with update.py
[table]:[attributes]
Musicians: SSN, Name, Str_type, Street, Num
Instruments: id, Type, Key
Albums: name, id, date, type
Musician_Album: SSN, album_id
Album_Instrument: album_id, instrument_id

*If the files don't run try running the commands with `python3` instead of `python`.
Otherwise try to reinstall python and adding python's binary to the path environment variable on your machine.