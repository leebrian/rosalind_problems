#!/usr/local/bin/python

"""
Script for "Counting DNA Nucleotides" https://rosalind.info/problems/dna/

Checking for how many instances of each character A/C/G/T exist within a string.
Output four ints, one for each char

"""

def main():

    with open('./data/in/01_rosalind_dna_dataset.txt','r') as file_in:
        contents = file_in.read()
        print(contents)

    symbols = ['A','C','G','T']
    counts = []

    for symbol in symbols:
        counts.append(contents.count(symbol))

    counts_as_string_no_brackets = ' '.join(map(str,counts))

    print(counts_as_string_no_brackets)

    with open('./data/out/01_rosalind_dna_solution.txt','w') as file_out:
        file_out.write(counts_as_string_no_brackets)

if __name__ == "__main__":
    main()
