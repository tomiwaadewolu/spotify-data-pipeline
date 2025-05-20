# scripts/models.py

from sqlalchemy import Column, Integer, String, Float, Boolean, Date # for getting data types for table
from sqlalchemy.ext.declarative import declarative_base # for creating a base class

Base = declarative_base() # getting base class for the ORM models

# defining a model class for the table
class spotify_song(Base):
    __tablename__ = 'spotify_songs'

    id = Column(Integer, primary_key=True, autoincrement=True)
    track = Column(String)
    album_name = Column(String)
    artist = Column(String)
    release_date = Column(Date)
    isrc = Column(String)
    all_time_rank = Column(Integer)
    track_score = Column(Float)
    spotify_streams = Column(Float)
    spotify_playlist_count = Column(Integer)
    spotify_playlist_reach = Column(Float)
    spotify_popularity = Column(Integer)
    youtube_views = Column(Float)
    youtube_likes = Column(Float)
    tiktok_posts = Column(Float)
    tiktok_likes = Column(Float)
    tiktok_views = Column(Float)
    youtube_playlist_reach = Column(Float)
    apple_music_playlist_reach = Column(Float)
    airplay_spins = Column(Float)
    siriusxm_spins = Column(Float)
    deezer_playlist_count = Column(Integer)
    deezer_playlist_reach = Column(Float)
    amazon_playlist_count = Column(Integer)
    pandora_streams = Column(Float)
    pandora_track_stations = Column(Float)
    soundcloud_streams = Column(Float)
    shazam_counts = Column(Float)
    tidal_popularity = Column(Float)
    explicit_track = Column(Boolean)