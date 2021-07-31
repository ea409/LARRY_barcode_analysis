import pandas as pd
import difflib
import argparse
import larry_functions


parser = argparse.ArgumentParser(description='Larry barcode imperfect matches')
parser.add_argument('virus_path',  type=str,
                    help='pandas csv file containing the counts')
parser.add_argument("orginal_barcode_location", type=str,
        help="the locations of the orginal barcodes")
parser.add_argument("save_loc", type=str,
        help="output save file location")

args = parser.parse_args()

Virus1 = pd.read_csv(args.virus_path)
original_barcodes = pd.read_csv(args.orginal_barcode_location)

unmapped_barcodes = Virus1[Virus1.Barcode.isna()].copy()

Clostest_mapping = larry_functions.map_barcodes(original_barcodes, unmapped_barcodes.Sequence )

unmapped_barcodes["closest_mappings"] = Clostest_mapping
unmapped_barcodes.to_csv(args.save_loc, index=False)