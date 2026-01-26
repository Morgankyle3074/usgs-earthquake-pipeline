from pathlib import Path
import pandas as pd

RAW_PATH = Path("data/raw/earthquakes_raw.csv")
OUT_PATH = Path("data/processed/earthquakes_clean.csv")

def main():
    print(f"Reading raw data: {RAW_PATH}")
    df = pd.read_csv(RAW_PATH)

    print("Raw columns:", list(df.columns))
    print("Raw shape:", df.shape)

    # Standardize column names
    df.columns = [c.strip().lower().replace(" ", "_") for c in df.columns]

    # Convert timestamps
    if "time" in df.columns:
        df["time"] = pd.to_datetime(df["time"], errors="coerce", utc=True)
    if "updated" in df.columns:
        df["updated"] = pd.to_datetime(df["updated"], errors="coerce", utc=True)

    # Rename key columns (USGS CSV includes these)
    df = df.rename(columns={
        "id": "event_id",
        "mag": "magnitude",
        "place": "location",
        "type": "event_type",
        "longitude": "longitude",
        "latitude": "latitude",
        "depth": "depth_km",
        "sig": "significance",
    })

    # Keep only the columns we care about for analytics + BI
    keep_cols = [
        "event_id", "time", "updated",
        "magnitude", "magtype",
        "location", "event_type",
        "latitude", "longitude", "depth_km",
        "significance", "tsunami", "status",
        "url"
    ]
    df = df[[c for c in keep_cols if c in df.columns]]

    # Drop rows missing critical values
    df = df.dropna(subset=["event_id", "time", "magnitude", "latitude", "longitude"])

    # Force numeric types where appropriate
    for col in ["magnitude", "latitude", "longitude", "depth_km", "significance"]:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")

    # Tsunami should be 0/1
    if "tsunami" in df.columns:
        df["tsunami"] = pd.to_numeric(df["tsunami"], errors="coerce").fillna(0).astype(int)

    # Add simple date fields for BI filtering
    df["year"] = df["time"].dt.year
    df["month"] = df["time"].dt.to_period("M").astype(str)
    df["day"] = df["time"].dt.date

    # Remove duplicates
    df = df.drop_duplicates(subset=["event_id"])

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(OUT_PATH, index=False)

    print("Clean shape:", df.shape)
    print(f"Saved cleaned CSV to: {OUT_PATH.resolve()}")

if __name__ == "__main__":
    main()
