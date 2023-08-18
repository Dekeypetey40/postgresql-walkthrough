import psycopg2

connection = psycopg2.connect(database="chinook")

cursor = connection.cursor()

# Query 1 - select all artists from table
# cursor.execute('SELECT * FROM "Artist"')

# Query 2
# cursor.execute('SELECT "Name" FROM "Artist"')

# Query3 look for Queen
# cursor.execute('SELECT * FROM "Artist" WHERE "Name" =%s', ["Queen"])

# Query4
# cursor.execute('SELECT * FROM "Artist" WHERE "ArtistId" = %s', [51])

# Query 5
# cursor.execute('SELECT * FROM "Album" WHERE "ArtistId" = %s', [51])

# Query 6
cursor.execute('SELECT * FROM "Track" WHERE "Composer" = %s', ["Queen"])

results = cursor.fetchall()

# results = cursor.fetchone()

connection.close()

for result in results:
    print(result)
