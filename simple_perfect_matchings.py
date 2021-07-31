import pandas as pd
import Bio.SeqIO as SeqIO
import larry_functions
import difflib
import argparse


parser = argparse.ArgumentParser(description='Larry barcode imperfect matches')
parser.add_argument('f1',  type=str,
                    help='path to fastq for R1')
parser.add_argument('f2',  type=str,
                    help='path to fastq for R2')
parser.add_argument("orginal_barcode_location", type=str,
        help="the locations of the orginal barcodes")
parser.add_argument("save_loc", type=str,
        help="output save file location")

args = parser.parse_args()

barcodes_unique1 = larry_functions.get_clean_library(args.f1, N_READS=nreads)
barcodes_unique2 = larry_functions.get_clean_library(args.f2, N_READS=nreads)
original_barcodes = pd.read_csv(args.orginal_barcode_location)


barcodes_unique1.insert(2, "Exact_matches", np.isin( barcodes_unique1.Sequence, original_barcodes.Barcode), True)
barcodes_unique2.insert(2, "Exact_matches",np.isin( barcodes_unique2.Sequence, original_barcodes.Barcode), True)


Virus1 = barcodes_unique1.merge(barcodes_unique2, on="Sequence", how="outer", suffixes=('_R1', '_R2'))
Virus1 = Virus1.merge(original_barcodes, how="left", left_on="Sequence", right_on="Barcode")
Virus1.to_csv(args.save_loc+".csv", index=False)