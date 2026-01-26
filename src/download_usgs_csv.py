from pathlib import Path
import requests

# Option B dataset settings (cleaner + easier)
START_DATE = "2025-01-01"
END_DATE   = "2026-01-01"
MIN_MAG    = 4.5

OUT_PATH = Path("data/raw/earthquakes_raw.csv")

USGS_CSV_URL = (
    "https://earthquake.usgs.gov/fdsnws/event/1/query"
    f"?format=csv&starttime={START_DATE}&endtime={END_DATE}&minmagnitude={MIN_MAG}&orderby=time-asc"
)

def main():
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    print("Downloading:", USGS_CSV_URL)

    r = requests.get(USGS_CSV_URL, timeout=60)
    r.raise_for_status()

    OUT_PATH.write_bytes(r.content)
    print(f"Saved CSV to: {OUT_PATH.resolve()}")

if __name__ == "__main__":
    main()

