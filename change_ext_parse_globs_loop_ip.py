#!/usr/bin/env python 

#following will change file kraken fastq report extension to .txt
# this part of the code works
#import os,sys
#folder = 'report_to_text_to_csv/subfolder/'
#for filename in os.listdir(folder):
       #infilename = os.path.join(folder,filename)
#       if not os.path.isfile(infilename): continue
#       oldbase = os.path.splitext(filename)
#       newname = infilename.replace('.report', '.txt')
#       output = os.rename(infilename, newname)
       
# following will parse the text files to csv       
# this part of the code works
import csv
import glob
import os
import pandas as pd

directory = "/Users/ShwetaPipaliya/Desktop/report_to_text_to_csv/subfolder/:"
output = "/Users/ShwetaPipaliya/Desktop/report_to_text_to_csv/subfolder/:"

txt_files = os.path.join(directory, '*.txt')

for txt_file in glob.glob(txt_files):
    with open(txt_file, "r+") as input_file:
        in_txt = csv.reader(input_file)
        filename = os.path.splitext(os.path.basename(txt_file)) + '.csv'

        with open(os.path.join(output, filename), 'w+') as output_file:
            out_csv = csv.writer(open(output_file, 'w'))
            out_csv.writerows(in_txt, index=False, encoding='utf-8-sig')
            out_csv.writerows(in_txt)
            writer.writeheader()
#following will compile all csv files into single combined csv spreadsheet
#import os
#import glob
#import pandas as pd
#os.chdir("/Users/ShwetaPipaliya/Desktop/report_to_text_to_csv/subfolder/:")

#extension = 'csv'
#all_filenames = [i for i in glob.glob('*.{}'.format(extension))]

#combine all files in the list
#combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames])
#export to csv
#combined_csv.to_csv("combined_csv.csv", index=False, encoding='utf-8-sig')

##End