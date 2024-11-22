import psycopg2

# connect to the database
connection = psycopg2.connect(database="cjinook")

# built the cursor object of the database
cursor = connection.cursor()

# 1 - select all records from "Artist" table
# cursor.execute('SELECT * FROM "Artist"')

# 2- select only records in "Name" column from "Artist" table
# cursor.execute('SELECT "Name" FROM "Artist"')

#3 - select "Queen" record in "Name" column from "Artist" table
# cursor.execute('SELECT * FROM "Artist" WHERE "Name" = %s', ["Queen"])

# 4 - select "ArtistId" #51 from the "Artist" table
# cursor.execute('SELECT * FROM "Artist" WHERE "ArtistId" = %s', [51])

# 5 - select only the albums with "ArtistId" #51 on the "Album" table
# cursor.execute('SELECT * FROM "Album" WHERE "ArtistId" = %s', [51])

# 6 - select all track where the composer is "Queen"
cursor.execute('SELECT * FROM "Track" WHERE "Composer" = %s', ["Karol Szymanowski"])

# 7
# cursor.execute('SELECT * FROM "Track"')

# fetch/retrive the results (multiply)
# results = cursor.fetchall()

# fetch/retrive the result (single)
results = cursor.fetchone()

# close connection
connection.close()

# print results
for result in results:
    print(result)