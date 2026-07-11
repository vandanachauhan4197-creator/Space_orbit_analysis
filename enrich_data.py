import pandas as pd
import numpy as np
import os

def enrich_orbital_data():
    """
    Cleans raw satellite data and performs feature engineering to calculate
    orbital altitude, categorize orbit zones, and compute a collision risk score.
    """
    raw_filename = "raw_space_debris.csv"
    output_filename = "space_debris_enriched.csv"
    
    print(" Starting Data Cleaning & Feature Engineering pipeline...")
    
    # Check if the raw data file exists before proceeding
    if not os.path.exists(raw_filename):
        print(f" Error: '{raw_filename}' not found! Please run 'fetch_data.py' first.")
        return

    try:
        # Load the raw dataset
        df = pd.read_csv(raw_filename)
        
        # 1. Data Cleaning: Drop rows with missing critical orbital parameters
        critical_columns = ['MEAN_MOTION', 'ECCENTRICITY', 'INCLINATION']
        df = df.dropna(subset=critical_columns)
        
        # 2. Astrodynamics Constants
        EARTH_MU = 398600.4418  # Earth's standard gravitational parameter (km^3/s^2)
        EARTH_RADIUS = 6378.137  # Earth's equatorial radius (km)
        SECONDS_IN_DAY = 86400
        
        # 3. Feature Engineering: Calculate Orbital Altitude (KM) using Kepler's Third Law
        # Convert Mean Motion (revolutions per day) to Orbital Period (seconds)
        df['Period_Sec'] = SECONDS_IN_DAY / df['MEAN_MOTION']
        
        # Apply Kepler's formula to find the Semi-Major Axis (a)
        df['Semi_Major_Axis'] = (EARTH_MU * (df['Period_Sec'] / (2 * np.pi))**2)**(1/3)
        
        # Altitude = Semi-Major Axis - Earth's Radius
        df['Altitude_KM'] = (df['Semi_Major_Axis'] - EARTH_RADIUS).round(2)
        
        # 4. Feature Engineering: Orbit Categorization (LEO, MEO, GEO)
        def classify_orbit_zone(altitude):
            if altitude < 2000:
                return "LEO (Low Earth Orbit)"
            elif altitude <= 35000:
                return "MEO (Medium Earth Orbit)"
            else:
                return "GEO (Geostationary Orbit)"
                
        df['Orbit_Zone'] = df['Altitude_KM'].apply(classify_orbit_zone)
        
        # 5. Feature Engineering: Statistical Collision Risk Score (Scale 1-100)
        # Higher operational speed (Mean Motion) in congested zones equals higher danger
        max_mm = df['MEAN_MOTION'].max()
        min_mm = df['MEAN_MOTION'].min()
        
        # Normalize the Mean Motion values into a 1-100 score distribution
        if max_mm != min_mm:
            df['Collision_Risk_Score'] = (((df['MEAN_MOTION'] - min_mm) / (max_mm - min_mm)) * 100).round(2)
        else:
            df['Collision_Risk_Score'] = 50.0  # Default fallback if variance is zero
            
        # 6. Data Filtering: Select only relevant columns for visualization/dashboarding
        final_features = [
            'OBJECT_NAME', 'OBJECT_ID', 'EPOCH', 'INCLINATION', 
            'ECCENTRICITY', 'MEAN_MOTION', 'Altitude_KM', 
            'Orbit_Zone', 'Collision_Risk_Score'
        ]
        df_final = df[final_features]
        
        # Save the enriched dataset to a new CSV file
        df_final.to_csv(output_filename, index=False)
        
        print(" Data transformation and feature engineering complete!")
        print(f" Processed dataset successfully saved as '{output_filename}'")
        
        # Display a quick structural overview of the processed data
        print("\n--- ENRICHED DATASET PREVIEW ---")
        print(df_final[['OBJECT_NAME', 'Altitude_KM', 'Orbit_Zone', 'Collision_Risk_Score']].head(3))
        
    except Exception as e:
        print(f" An error occurred during processing: {e}")

if __name__ == "__main__":
    enrich_orbital_data()
    
