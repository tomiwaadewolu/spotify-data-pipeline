# scripts/extract_spotify_data.py

import os # for using os dependent functions
import shutil # for copying and moving files and directories
from datetime import datetime # for working with dates and times

# paths
SOURCE_FILE = "data/most_streamed_spotify_songs_2024.csv"
DEST_DIR = "data/raw"
LOG_FILE = "logs/extract_log.txt"

# function to extract the data
def extract_data():
    # create destination directort if not already existing
    os.makedirs(DEST_DIR, exist_ok=True)

    # generate a unique filename with a timestamp
    filename = f"spotify_raw_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"

    # combine the destination directory path with the filename
    destination_path = os.path.join(DEST_DIR, filename)

    # copy the source CSV file to the destination path
    shutil.copy2(SOURCE_FILE, destination_path)

    # open the log file in append mode and log the extraction with a timestamp
    with open(LOG_FILE, "a") as log:
        log.write(f"[{datetime.now()}] Extracted data to {destination_path}\n")

    # print a confirmation message
    print(f"Data copied to {destination_path}")

# calling function in main
if __name__ == "__main__":
    extract_data()