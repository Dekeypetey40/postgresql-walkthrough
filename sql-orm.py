from sqlalchemy import (
    create_engine, Column, Float, ForeignKey, Integer, String
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# do instruction in chinook db
db = create_engine("postgresql:///chinook")
base = declarative_base()

# create a class based model for Artist table


class Artist(base):
    __tablename__ = "Artist"
    ArtistId = Column(Integer, primary_key=True)
    Name = Column(String)

# create a class based model for Album table


class Album(base):
    __tablename__ = "Album"
    AlbumId = Column(Integer, primary_key=True)
    Title = Column(String)
    ArtistId = Column("ArtistId", Integer, ForeignKey("Artist.ArtistId"))

# create a class based model for Track table


class Track(base):
    __tablename__ = "Track"
    TrackId = Column(Integer, primary_key=True)
    Name = Column(String)
    AlbumId = Column(Integer, ForeignKey("Album.AlbumId"))
    MediaTypeId = Column(Integer, primary_key=False)
    GenreId = Column(Integer, primary_key=False)
    Composer = Column(String)
    Milliseconds = Column(Integer, primary_key=False)
    Bytes = Column(Integer, primary_key=False)
    UnitPrice = Column(Float)


# instead of connecting directly to db we use
# sessionmaker to point to our engine (the db)
Session = sessionmaker(db)
# open actual session by calling the Session() subclass defined above
session = Session()

# creating database declarative_base subclass
base.metadata.create_all(db)

# Query 1 all records from artist table
# artists = session.query(Artist)
# for artist in artists:
# print(artist.ArtistId, artist.Name, sep=" | ")

# Query 2 just names
# artists = session.query(Artist)
# for artist in artists:
# print(artist.Name)

# Query 3 only name Queen
# artist = session.query(Artist).filter_by(Name="Queen").first()
# print(artist.ArtistId, artist.Name, sep= " | ")

# Query 4 only artist id 51
# artist = session.query(Artist).filter_by(ArtistId=51).first()
# print(artist.ArtistId, artist.Name, sep=" | ")

# Query 5 only albums with artistid 51
# albums = session.query(Album).filter_by(ArtistId=51)
# for album in albums:
# print(album.AlbumId, album.Title, album.ArtistId, sep=" | ")

# Query 6 select all tracks where composer is Queen from track table
tracks = session.query(Track).filter_by(Composer="Queen")
for track in tracks:
    print(
        track.TrackId,
        track.Name,
        track.AlbumId,
        track.Composer,
        sep=" | "
    )
