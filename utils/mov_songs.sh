#!/bin/bash

original_dir=""
new_dir=""
outfile=""

{
    ls -1 "$original_dir"
    ls -1 "$new_dir"
} > "$outfile"

sort -o "$outfile"{,}
uniq -u "$outfile" > tmp.txt
cat tmp.txt > "$outfile"
rm ./tmp.txt

while IFS="" read -r p || [ -n "$p" ]
do
 cp "$original_dir$p" "$new_dir$p"
done < "$outfile"
