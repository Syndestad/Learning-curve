#!/usr/local/bin/r

################################
# File name: GC_calc.R
# R version 4.1.0
# Author: Synnøve Yndestad
# Date: 15.08.2021
# Description:
## This R-script will take a DNA sequence in FASTA format and
## -Compute the length and GC content of a DNA sequence while considering both uppercase and lowercase letters.
## -Show processing time.
## -Print output in terminal
################################



# Ask the user for an input and store it as a variable
# get a DNA sequence from a FASTA file:

cat("Please enter name of FASTA file:");
FASTA <- readLines("stdin",n=1);


# Set start time for processing time
start_time <- Sys.time()


# Read FASTA file, save as dna variable
dna = seqinr::read.fasta(FASTA, as.string = TRUE)

# fasta file is read as list, we really just want the first list.
# Subset the first element of the first list:
dna <- dna[[1]]



# Calculate Lenght by counting the number of characters in string
DNAlenght <- nchar(dna)

# Load required packages.
# Tidyverse is a set of packages that work well together including stringr needed for str_count()
# library(tidyverse)
# Count "c" + "C" in dna
no_c <- sum(stringr::str_count(dna, c("c", "C")))
# Count "g" + "G" in dna
no_g <- sum(stringr::str_count(dna,c("g", "G")))
# Count "n" + "N" in dna
no_n <- sum(stringr::str_count(dna,c("n", "N")))
# Calculate GC percentage without N or n bases
gc_percent <- ((no_c+no_g)*100/(DNAlenght-no_n))

# Attach descriptive string to output
OutputString = "%GC content without N bases is:"

# Print name of sequence:

attr(dna, "Annot")

# print output using strings, functions and variables
print(paste("The DNA sequence is", nchar(dna) ,"base pairs long with", no_n ,"number of N bases"), quote = FALSE)
# print gc_percent results rounded to 2 decimals by round()
print(c(OutputString,round(gc_percent,2)), quote = FALSE)

# Save time at end
end_time <- Sys.time()
# Print time elapsed from input
print(paste("---Calculated in", (end_time - start_time), "seconds ---" ), quote = FALSE)
