#!/bin/sh
while true; do

  file_name="Please Enter Your Name File:"
  # shellcheck disable=SC2162
  read file_name
  # shellcheck disable=SC2039
  if [[ -f "$file_name"  ]] ; then
  tail -10 "$file_name"
  else
    echo "Error"
    fi
done
