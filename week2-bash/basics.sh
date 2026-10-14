   #!/bin/bash

   # Variables
   name="santa"
   today=$(date +%Y-%m-%d)
   echo "Hello $name, today is $today"

   # Arguments: the first thing typed after the script name
   folder=$1
   echo "You gave me the folder: $folder"

   # Condition: does the folder exist?
   if [ -d "$folder" ]; then
       echo "Folder exists"
   else
       echo "Folder not found"
   fi

   # Loop: list each item in the folder
   for item in "$folder"/*; do
       echo "Found: $item"
   done
