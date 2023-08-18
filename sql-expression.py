from sqlalchemy import (
    create_engine, Table, Column, Float, ForeignKey, Integer, String, MetaData
)

# executing instructions from db
db = create_engine("postgresql:///chinook")

meta = MetaData(db)

# create Artist variable
artist_table = Table(
    "Artist", meta,
    Column("ArtistId", Integer, primary_key=True),
    Column("Name", String)
)

# Create variable for album
album_table = Table(
    "Album", meta,
    Column("AlbumId", Integer, primary_key=True),
    Column("Title", String),
    Column("ArtistId", Integer, ForeignKey("artist_table.ArtistId"))
)

# Creating track variable
track_table = Table(
    "Track", meta,
    Column("TrackId", Integer, primary_key=True),
    Column("Name", String),
    Column("AlbumId", Integer, ForeignKey("album_table.AlbumId")),
    Column("MediaTypeId", Integer, primary_key=False),
    Column("GenreId", Integer, primary_key=False),
    Column("Composer", String),
    Column("Milliseconds", Integer),
    Column("Bytes", Integer),
    Column("UnitPrice", Float),
)

# make connection
with db.connect() as connection:

    # Query 1 all records from artist table
    # select_query = artist_table.select()

    # Query 2 just names
    # select_query = artist_table.select().with_only_columns([artist_table.c.Name])

    # Query 3 only name
    # select_query = artist_table.select().where(
    # artist_table.c.Name == "Queen")

    # Query 4 only artist id 51
    # select_query = artist_table.select().where(
    # artist_table.c.ArtistId == 51)

    # Query 5 only albums with artistid 51
    # select_query = album_table.select().where(album_table.c.ArtistId == 51)

    # Query 6 select all tracks where composer is Queen from track table
    select_query = track_table.select().where(track_table.c.Composer == "Queen")

    results = connection.execute(select_query)
    for result in results:
        print(result)
