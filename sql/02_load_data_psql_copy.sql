TRUNCATE TABLE usgs.earthquakes;

-- Update path if your repo is in a different location
\copy usgs.earthquakes FROM 'C:/Users/Kyle/Documents/SQl Datasets/usgs-earthquake-pipeline/data/processed/earthquakes_clean_sanitized.csv' WITH (FORMAT csv, HEADER true);
