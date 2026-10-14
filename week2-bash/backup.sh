#!/bin/bash

source_dir=$1
backup_dir=~/backups
log_file=~/backups/backup.log
timestamp=$(date +%Y-%m-%d_%H-%M-%S)

# Stop if no folder was given
if [ -z "$source_dir" ]; then
    echo "Usage: ./backup.sh <folder>"
    exit 1
fi

# Stop if the folder does not exist
if [ ! -d "$source_dir" ]; then
    echo "Error: $source_dir not found"
    exit 1
fi

mkdir -p "$backup_dir"
archive="$backup_dir/backup_$timestamp.tar.gz"

# Create the archive and log the result
if tar -czf "$archive" "$source_dir"; then
    echo "$timestamp SUCCESS: $source_dir -> $archive" >> "$log_file"
    echo "Backup complete"
else
    echo "$timestamp FAILED: $source_dir" >> "$log_file"
    echo "Backup failed"
    exit 1
fi
