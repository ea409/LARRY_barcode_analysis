import pandas as pd
import Bio.SeqIO as SeqIO
import difflib


def contains_fw(record):
    sequence = "ATGTCTggatccgatatcgccaccgtggctgaatgagactggtgtcgacctgtg"
    if (sequence.upper() in record.seq ):
        index = record.seq.find(sequence.upper())
        return record.seq[index-40:index]
    return None

def is_valid(bc):
    return bc[4:6]=='TG' and bc[10:12]=='CA' and bc[16:18]=='AC' and bc[22:24]=='GA' 

def get_clean_library(f, N_READS=5):
    library_clean = []
    for record in SeqIO.parse(f, "fastq"):
        fw = contains_fw(record)
        if fw is not None:
            if is_valid(fw): library_clean.append(str(fw))
    bcs = pd.DataFrame({"Barcodes": library_clean})
    cnts = bcs.Barcodes.value_counts()
    print("for file ", f,
      "\n number of barcodes: ",sum(cnts),
      "\n number of unique barcodes :", len(cnts),
      "\n number of barcodes meeting reads threshold:",sum(cnts>=N_READS) )
    cnts=cnts[cnts>=N_READS]
    cnts.index.rename("Sequence", inplace=True)
    return cnts.reset_index()

def map_barcodes(original_barcodes, test_sequences):
    real_barcodes = []
    for seq in  test_sequences:
        match = difflib.get_close_matches(seq, original_barcodes.Barcode, n=1)
        if len(match)==0: predictions.append(NA)
        else: real_barcodes.append(match[0])
    return real_barcodes
