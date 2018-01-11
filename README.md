# genbank_to_fasta 


Extract protein fasta from Genbank files

# Usage

```bash
$ python genbank_to_faa.py --help
usage: genbank_to_faa.py [-h] [--qualifier [QUALIFIER]] [genbank] [protein_fasta]

Extract protein fasta from Genbank files

positional arguments:
  genbank               input genbank file (default: STDIN)
  protein_fasta         output fasta file (default: STDOUT)

optional arguments:
  -h, --help            show this help message and exit
  --qualifier [QUALIFIER]
                        Genbank qualifier used for the fasta header (default: label)
```