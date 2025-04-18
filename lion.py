import os
from pathlib import Path

# Get the user's Downloads folder (works on Windows, macOS, Linux)
downloads_path = Path.home() / "Downloads"

# Get a list of items in the Downloads folder
try:
    items = os.listdir(downloads_path)
except FileNotFoundError:
    print(f"Could not find the Downloads folder at: {downloads_path}")
    items = []

# Define output file path
output_file = Path(__file__).parent / "downloads_list.txt"

# Write the list to the output file
with open(output_file, "w", encoding="utf-8") as f:
    for item in items:
        f.write(f"{item}\n")

print(f"List of downloads saved to {output_file}")
