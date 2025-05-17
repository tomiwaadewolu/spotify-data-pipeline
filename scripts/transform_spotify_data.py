# scripts/transform_spotify_data.py

import os # for using os dependent functions
import pandas as pd # for data manipulation and analysis

# paths
RAW_DATA_PATH = "data/raw/spotify_raw_20250515_194612.csv"
PROCESSED_DATA_PATH = "data/processed/spotify_cleaned.csv"

# function to transform the data
def transform_data():
    # step 1: load raw data into a dataframe
    df = pd.read_csv(RAW_DATA_PATH, encoding='latin1')

    # step 2: clean the data
    # drop rows with missing values
    df_clean = df.dropna().copy()

    # rename selected rows to use snake_case (for consistency)
    df_clean.rename(columns={
        'Track': 'track',
        'Album Name': 'album_name',
        'Artist': 'artist',
        'Release Date': 'release_date',
        'ISRC': 'isrc',
        'All Time Rank': 'all_time_rank',
        'Track Score': 'track_score',
        'Spotify Streams': 'spotify_streams',
        'Spotify Playlist Count': 'spotify_playlist_count',
        'Spotify Playlist Reach': 'spotify_palylist_reach',
        'Spotify Popularity': 'spotify_popularity',
        'YouTube Views': 'youtube_views',
        'YouTube Likes': 'youtube_likes',
        'TikTok Posts': 'tiktok_posts',
        'TikTok Likes': 'tiktok_likes',
        'TikTok Views': 'tiktok_views',
        'YouTube Playlist Reach': 'youtube_playlist_reach',
        'Apple Music Playlist Count': 'apple_music_playlist_reach',
        'AirPlay Spins': 'airplay_spins',
        'SiriusXM Spins': 'siriusxm_spins',
        'Deezer Playlist Count': 'deezer_playlist_count',
        'Deezer Playlist Reach': 'deezer_playlist_reach',
        'Amazon Playlist Count': 'amazon_playlist_count',
        'Pandora Streams': 'pandora_streams',
        'Pandora Track Stations': 'pandora_track_stations',
        'Soundcloud Streams': 'soundcloud_streams',
        'Shazam Counts': 'shazam_counts',
        'TIDAL Popularity': 'tidal_popularity',
        'Explicit Track': 'explicit_track'
    }, inplace=True)

    # convert 'release_date' to datetime format
    if 'release_date' in df_clean.columns:
        df_clean['release_date'] = pd.to_datetime(df_clean['release_date'], errors='coerce')

    # remove duplicate rows from the data
    df_clean.drop_duplicates(inplace=True)

    # step 3: save the cleaned data
    # make sure the directory for processed data exists
    os.makedirs(os.path.dirname(PROCESSED_DATA_PATH), exist_ok=True)

    # save the cleaned datafram to a csv file without row indices
    df_clean.to_csv(PROCESSED_DATA_PATH, index=False)

    # print a confirmation message
    print(f"Cleaned data saved to {PROCESSED_DATA_PATH}")

# calling function in main
if __name__ == "__main__":
    transform_data()