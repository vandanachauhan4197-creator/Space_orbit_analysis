import pandas as pd
import requests
import os

def fetch_space_debris_data():
    """
    Fetches real-time orbital data for space debris from the CelesTrak API
    and saves the raw output into a CSV file for the analysis pipeline.
    """
    # URL for fetching IRIDIUM 33 debris data in standard OMM CSV format
    url = "https://celestrak.org/NORAD/elements/gp.php?GROUP=iridium-33-debris&FORMAT=CSV"
    
    print("Connecting to CelesTrak API to download live Space Debris data...")
    
    try:
        # Sending GET request to fetch live orbital data
        response = requests.get(url, timeout=15)
        response.raise_for_status()  # Check for HTTP request errors
        
        # Save the raw text content into a local CSV file
        raw_filename = "raw_space_debris.csv"
        with open(raw_filename, "w", encoding="utf-8") as file:
            file.write(response.text)
            
        print("Data successfully downloaded from API!")
        print(f"Raw dataset saved as '{raw_filename}'")
        
        # Load the newly created file into a Pandas DataFrame to verify its content
        df = pd.read_csv(raw_filename)
        
        print("\n--- DATA FETCH OVERVIEW ---")
        print(f"Total rows fetched (Debris items): {len(df)}")
        
        if len(df) == 0:
            print("Warning: The fetched dataset is empty. Please check the API endpoint or connection.")
            return
            
        print("\nFirst 3 rows of the fetched dataset:")
        print(df[['OBJECT_NAME', 'OBJECT_ID', 'EPOCH', 'MEAN_MOTION']].head(3))
        
    except requests.exceptions.RequestException as req_err:
        print(f"Network or API Error occurred: {req_err}")
    except KeyError as key_err:
        print(f"Column Mapping Error: Required columns are missing from the API response. Details: {key_err}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    fetch_space_debris_data()
      
