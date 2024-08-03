#!/bin/bash

# Define variables
DATABASE="/etc/pihole/gravity.db"
OUTPUT_FILE="/root/Blacklists/Adlists/adlists.txt"

# Check if the database file exists
if [ ! -f "$DATABASE" ]; then
    echo "Error: Database file $DATABASE does not exist."
    exit 1
fi

# Check if the output file directory exists
OUTPUT_DIR=$(dirname "$OUTPUT_FILE")
if [ ! -d "$OUTPUT_DIR" ]; then
    echo "Error: Output directory $OUTPUT_DIR does not exist."
    exit 1
fi

# Run the SQLite query and save the output to the file
sqlite3 "$DATABASE" "SELECT address FROM adlist;" > "$OUTPUT_FILE"

# Check if the operation was successful
if [ $? -eq 0 ]; then
    echo "Successfully updated $OUTPUT_FILE with adlist addresses."
else
    echo "Error: Failed to execute SQLite query or write to $OUTPUT_FILE."
    exit 1
fi

