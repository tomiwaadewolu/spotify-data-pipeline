# scripts/load_spotify_data.py

import pandas as pd # for data manipulation and analysis
from sqlalchemy.exc import IntegrityError # for error handling
from scripts.db import SessionLocal
from scripts.models import Base, spotify_song
from sqlalchemy import create_engine
from scripts.db import engine


# function to load the data to postgresql
def load_data():
    # create tables if not already created
    Base.metadata.create_all(bind=engine)

    # read the cleaned csv file into a pandas dataframe
    df = pd.read_csv("data/processed/spotify_cleaned.csv")
    print(f"Loaded {len(df)} rows")
    print(df.head())

    # convert to explicit_track to boolean
    df['explicit_track'] = df['explicit_track'].astype(bool)

    # convert df rows to ORM objects
    records = []
    for _, row in df.iterrows():
        record = spotify_song(
            track=row['track'],
            album_name=row['album_name'],
            artist=row['artist'],
            release_date=row['release_date'],
            isrc=row['isrc'],
            all_time_rank=row['all_time_rank'],
            track_score=row['track_score'],
            spotify_streams=row['spotify_streams'],
            spotify_playlist_count=row['spotify_playlist_count'],
            spotify_playlist_reach=row['spotify_playlist_reach'],
            spotify_popularity=row['spotify_popularity'],
            youtube_views=row['youtube_views'],
            youtube_likes=row['youtube_likes'],
            tiktok_posts=row['tiktok_posts'],
            tiktok_likes=row['tiktok_likes'],
            tiktok_views=row['tiktok_views'],
            youtube_playlist_reach=row['youtube_playlist_reach'],
            apple_music_playlist_reach=row['apple_music_playlist_reach'],
            airplay_spins=row['airplay_spins'],
            siriusxm_spins=row['siriusxm_spins'],
            deezer_playlist_count=row['deezer_playlist_count'],
            deezer_playlist_reach=row['deezer_playlist_reach'],
            amazon_playlist_count=row['amazon_playlist_count'],
            pandora_streams=row['pandora_streams'],
            pandora_track_stations=row['pandora_track_stations'],
            soundcloud_streams=row['soundcloud_streams'],
            shazam_counts=row['shazam_counts'],
            tidal_popularity=row['tidal_popularity'],
            explicit_track=row['explicit_track']
        )
        records.append(record)

    # insert data into the database
    session = SessionLocal()
    try:
        # delete all existing rows before insert
        session.query(spotify_song).delete()
        session.commit()

        session.bulk_save_objects(records)
        session.commit()
        print(f"Successfully inserted {len(records)} rows into 'spotify_songs'")
    except IntegrityError as e:
        session.rollback()
        print("Integrity Error:", e)
    finally:
        session.close()

# calling function in main
if __name__ == "__main__":
    load_data()