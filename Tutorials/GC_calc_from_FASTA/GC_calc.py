##! /Users/syndestad/opt/anaconda3/bin/python

"""
File name: GC_calc.py
Python version: 3.8.3
Author: Synnøve Yndestad
Date: 15.08.2021
Description:
This python program will take a DNA sequance in FASTA format as input and
 -Compute the length and GC content of a DNA sequence while considering both uppercase and lowercase letters.
 -Show processing time.
 -Print output in terminal
"""

# make executable in terminal by "chmod a+x nameOfFile.py"

# Ask the user for an input and store it as a variable
#get DNA sequence:
Input_fasta_file = input("Please enter name of FASTA file:")

# import time module
import time
# Set start time for processing time
start_time = time.time()


# Make a function that reads FASTA line by line
def readFASTA(FASTAfile):               # Define function and argument
    content = []                        # Place to put the data
    with open(FASTAfile, "r") as file:  # read only
        for line in file:
            line = line.strip()         # remove n\ and white spaces
            content.append(line)        # add each line as it is read
    return content

# Use the function to read FASTA
dna = readFASTA(Input_fasta_file)
# Save the first row as input file name
name = dna[0]
# Join all elements to one, exclude first row with name
dna = "".join(dna[1:])
# We now have readable data!



# Count C’s + c's in DNA sequence
no_c=dna.count('c')+dna.count('C')
# Count G’s + c's in DNA sequence
no_g=dna.count('g')+dna.count('G')
# Count  N's+n's in DNA sequence
no_n=dna.count('n')+dna.count('N')
# get the length of the DNA sequence
dna_len=len(dna)
# compute gc percentage - N bases
gc_perc=(no_c+no_g)*100.0/(dna_len-no_n)
# Print the name if input sequence
print(name)

# print output using strings, functions  and variables.
print("The DNA sequence is", len(dna), "baseparis long with", no_n, "number of N bases")

#  Print output text using %% to print a % symbol
#  Formatting strings; %%, %-operator separating formatting string and the value to replace the placeholder
#  Formatting string example: %5.2f
#                   % =indicates that a format follows
#                   5 = total number of digits
#                   2 = number of digits following the .
#                   f = letter indicating the type of the value to format
#                       f is fixed point
# Print GC content rounded by 2 decimals
print("The DNA sequence’s GC content is %.2f %%" % gc_perc)

# Print processing time in seconds
print("---Calculated in  %s seconds ---" % (time.time() - start_time))
