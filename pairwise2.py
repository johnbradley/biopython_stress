from Bio import pairwise2
import itertools
from sys import argv

#seq1 = "ABCBCD"
#seq2 = "BC"
#aln = pairwise2.align.globalxx(seq1,seq2)
#print aln

#cnt = 0
#for opt in itertools.permutations('AABBCCDDEE', 5):
#    cnt += 1
#print cnt
#range = 
#for i in range(ord('A'), ord('C') + 1):
#    print unichr(i)
letters = "ACDEFGHIKL"
#           1234567890
def make_str(num, width):
    format_str = "{0:0" + str(width) + "d}"
    nums = [int(c) for c in format_str.format(num)]
    return ''.join([letters[val] for val in nums])

#for opt in itertools.permutations('ABC', 1):
#    print opt

filename = argv[1]
width = int(argv[2])
with open(filename, "w") as outfile:
    for i in range(10 ** width):
        seq1 = make_str(i, width)
        for j in range(10 ** width):
            seq2 = make_str(j, width)
            aln = pairwise2.align.globalxx(seq1,seq2)
            outfile.write(str(aln) + "\n")
