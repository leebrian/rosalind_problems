#!/usr/local/bin/python

"""
Script for "Transcribing DNA into RNA" https://rosalind.info/problems/rna/

Replace all occurrences of 'T' with 'U'
Output transcribed string

"""

def main():

    with open('./data/in/02_rosalind_rna_dataset.txt','r') as file_in:
        contents = file_in.read()
        print(contents)

    transcribed = contents.replace('T','U')

    print(transcribed)

    with open('./data/out/02_rosalind_rna_solution.txt','w') as file_out:
        file_out.write(transcribed)

if __name__ == "__main__":
    main()
