#!/bin/bash
file_patch=$(find . -type f -name '*.mp3' | shuf -n 1)
Elisa "$file_patch"

if [ -f "$file_patch" ]; then
  # shellcheck disable=SC2162
  read -p "Rate the song between 1 to 10 " songrate
  exho "$file_patch" >>file_patch.txt

  avg=$ awk '{ total += $1; count++ } END { print total/count }' file_patch.txt
  awk '{$2=$2 "$avg"}1' "$file_patch".txt

else
  touch "$file_patch".txt

  # shellcheck disable=SC2034
  # shellcheck disable=SC2162
  read -p "Rate the song between 1 to 10 " songrate
  exho "$file_patch" >>songpath.txt
  avg=$ awk '{ total += $1; count++ } END { print total/count }' file_patch.txt
  awk '{$2=$2 "$avg"}1' "$file_patch".txt
fi
