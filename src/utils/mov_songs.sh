#!/bin/bash

original_dir="/home/w15hy/music/"
new_dir="/run/user/1000/gvfs/mtp:host=OPPO_CPH2577_ORAEBMON7DTGX445/Внутренняя память/Music/"
outfile="/home/w15hy/projects/download_music/src/utils/pass.txt"

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
# rm "$outfile"
