#!/usr/bin/python

def match(ambGen, knownHap):
    mapped = 1
    i = 0
    while i < len(ambGen):
        if ambGen[i] == '2' and knownHap[i] != '1':
            mapped = 0
        if ambGen[i] == '0' and knownHap[i] != '0':
            mapped = 0
        i += 1
    return mapped

def main():

    # The input is an N x M matrix of genotypes, with N individuals and M SNPs
    f = open('genotypes.txt', 'r')
    numLines = sum(1 for line in open('genotypes.txt'))
    lines = f.readlines()
    f.close()

    arrHaps=[0]*(2 * numLines)  # Array containing 2N x M matrix, given N individuals
                                # and M SNPs in the genotype reads.
    knownHaps = []  # Array of known haplotypes. Will get haplotypes
                    # appended at each round.
    ambGens = []    # Ambiguous genotypes after first round
    ambPos = []     # Positions of ambiguous genotypes

    # First, any unambiguous genotypes (not containing any 1's) will be
    # translated to haplotypes and stored in the array arrHaps.
    for i in range(0, numLines):
        row = str(lines[i]).rstrip('\n')
        if '1' not in row:
            lrow = list(row)
            for j in range(0, len(row)):
                if (lrow[j] == '2'):
                    lrow[j] = '1'
            row = ''.join(lrow)
            knownHaps.append(row)
            arrHaps[2*i] = row
            arrHaps[(2*i)+1] = row
        else:
            # Ambiguous haplotypes and their positions will be now stored
            # into their respective arrays.
            ambGens.append(row)
            ambPos.append(2*i)

    knownHaps = list(set(knownHaps))    # removes duplicates from knownHaps
    complements = []    # If a known haplotype is compatible with an ambiguous
                        # genotype, the new haplotype to solve the genotype (the complement)
                        # will be calculated and stored into this array.
    k = 0
    while k < len(knownHaps):
        knownHap = str(knownHaps[k])
        i = 0
        while i < len(ambGens):
            ambGen = str(ambGens[i])
            complement = ''
            # The match function tells us if a known haplotype has a
            # complement that can result in solving the genotype
            if (match(ambGen, knownHap) == 1):
                pos = int(ambPos[i])
                if arrHaps[pos] == 0:
                    arrHaps[pos] = knownHap
                for j in range(0, len(ambGen)):
                    if (ambGen[j] == '2' and knownHap[j] == '1'):
                        complement += '1'
                    elif (ambGen[j] == '1' and knownHap[j] == '0'):
                        complement += '1'
                    elif (ambGen[j] == '1' and knownHap[j] == '1'):
                        complement += '0'
                    else:
                        complement += '0'
                if arrHaps[pos+1] == 0:
                    arrHaps[pos+1] = complement
                if complement not in knownHaps:
                    complements.append(complement)
                    complements = list(set(complements))    # removes duplicates
            if (k == len(knownHaps)-1 and i == len(ambGens)-1 and 0 in arrHaps):
                knownHaps = knownHaps + complements
            i += 1
        k += 1
    # print '\n'.join(map(str, arrHaps))

    # The output is the 2N x M array of haplotypes
    # with all duplicates removed.
    rawOutput = list(set(arrHaps))
    print '\n'.join(map(str, rawOutput))

if __name__ == "__main__":
    main()
