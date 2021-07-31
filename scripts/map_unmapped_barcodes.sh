#!/bin/sh
#PBS -lwalltime=72:00:00
#PBS -lselect=1:ncpus=20:mem=240gb


cd /rds/general/user/ealjibur/home/LARRY_whitelist_v2

module load anaconda3/personal

teresa_folder="/rds/general/user/ealjibur/projects/lms-merkenshlager-analysis/live/Ediem/Teresa/"

for virus in "Virus1" "Virus2" "Virus3" "Virus4" "Virus5" "Virus6"

do 

python unmapped_barcodes.py $teresa_folder${virus}.csv ${teresa_folder}barcode_list.csv $teresa_folder${virus}_unmapped.csv 

done 