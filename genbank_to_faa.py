
from Bio import SeqIO
import sys, os
import argparse

def convert_genbank_to_faa( gbk_filename, faa_filename, qualifier='label') :
    for seq_record in SeqIO.parse(gbk_filename, "genbank") :
        for seq_feature in seq_record.features :
            if seq_feature.type=="CDS" andx 'translation' in seq_feature.qualifiers and len(seq_feature.qualifiers['translation'])==1:
                    faa_filename.write(">%s_%s from %s\n%s\n" % (
                        os.path.basename(gbk_filename.name).split('.')[0],
                        seq_feature.qualifiers[qualifier][0],
                        seq_record.name,
                        seq_feature.qualifiers['translation'][0]))

    faa_filename.close()
    gbk_filename.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Extract protein fasta from Genbank files')
    parser.add_argument('genbank', nargs='?', type=argparse.FileType('r'), default = sys.stdin, help='input genbank file (default: STDIN)')
    parser.add_argument('protein_fasta', nargs='?', type=argparse.FileType('w'), default=sys.stdout, help='output fasta file (default: STDOUT)')
    parser.add_argument('--qualifier', nargs='?', default='label', help='Genbank qualifier used for the fasta header (default: label)' )
    args = parser.parse_args()
    convert_genbank_to_faa( args.genbank, args.protein_fasta, args.qualifier )
