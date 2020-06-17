#!/bin/bash

## this script will allow you to download the datasets-tool at ncbi and allow you to 
## retrieve specified ftp datasets

## download the datasets tool on mac (replace mac with linux-amd64 in the link below if working in linux)
curl -o datasets 'https://ftp.ncbi.nlm.nih.gov/pub/datasets/command-line/LATEST/mac/datasets'

##grant permission to execute tool (add installation path to BASH profile if necessary)
chmod +x datasets

## Example get genomic and transcript sequences for the cow RefSeq genome (replace with genome assembly accession)
./datasets download assembly GCF_002263795.1 --include-rna --filename cow_sequences.zip

##Download a compact package, also known as an unresolved bag, containing data reports and file locations for set of RefSeq genomes, then retrieve the data when needed using rehydrate

##Download compact package containing data reports and file locations for specified taxon id
./datasets download assembly tax-id 9443 --refseq --unresolved --filename primates_refseq_unresolved.zip
##unzip
unzip primates_refseq_unresolved.zip
## rehydrate to retrieve genomes
./datasets rehydrate --filename

##use './dataset --help' for more options

##end
