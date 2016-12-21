#!/usr/bin/python

def main():
    # The input is an N x M matrix of genotypes, with N individuals and M SNPs
    f = open('genotypes.txt', 'r')
    numLines = sum(1 for line in open('genotypes.txt'))
    lines = f.readlines()
    f.close()

    knownHaps = []
    for i in range(0, numLines):
        row = str(lines[i]).rstrip('\n')
        OneCnt = row.count('1')     # If there are X 1's in a row, then there will be
                                    # 2^X corresponding possible haplotypes for that row
        formStr = '0' + str(OneCnt) + 'b'   # Needed to change overallCnt to binary
        overallCnt = 0              # Contains the decimal representation of binCnt
        for j in range(0, (2 ** OneCnt)):
            cnt = 0
            lrow = list(row)
            binCnt = format(overallCnt, formStr)    # binCnt represents an array of numbers
                                                    # that all '1's have to be replaced by
            for k in range(0, len(row)):
                if (lrow[k] == '2'):
                    lrow[k] = '1'
                elif (lrow[k] == '1'):
                    lrow[k] = binCnt[cnt]   # replacing every '1' with its corresponding
                                            # number from the binCnt character array
                    cnt += 1
                else:
                    lrow[k] = '0'
            overallCnt += 1                 # binCnt will be incremented by 1 in binary
            knownHaps.append(''.join(lrow)) # knownHaps will contain all possible haplotypes
                                            # for the given genotypes
    # print '\n'.join(map(str, knownHaps))
    rawOutput = list(set(knownHaps))        # removes duplicates in knownHaps
    print '\n'.join(map(str, rawOutput))

if __name__ == "__main__":
    main()
