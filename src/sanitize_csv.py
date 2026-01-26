import pathlib
import re

src = pathlib.Path("data/processed/earthquakes_clean.csv")
dst = pathlib.Path("data/processed/earthquakes_clean_sanitized.csv")

# Read bytes, decode with cp1252 so we can interpret the Windows byte 0x81,
# then strip control characters and write clean UTF-8.
raw = src.read_bytes()
text = raw.decode("cp1252", errors="replace")

# Remove ASCII control chars except: tab (\x09), newline (\x0A), carriage return (\x0D)
text = re.sub(r"[\x00-\x08\x0B\x0C\x0E-\x1F\x7F-\x9F]", "", text)

dst.write_text(text, encoding="utf-8", newline="")
print(f"Wrote sanitized file: {dst}")
