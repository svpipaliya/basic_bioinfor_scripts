#!/usr/bin/env python 

#following will change file kraken fastq report extension to .txt
# this part of the code works
import os,sys
folder = 'report_to_text_to_csv/subfolder/'
for filename in os.listdir(folder):
       infilename = os.path.join(folder,filename)
       if not os.path.isfile(infilename): continue
       oldbase = os.path.splitext(filename)
       newname = infilename.replace('.report', '.txt')
       output = os.rename(infilename, newname)

#following will convert resulting textfiles to csv
import pandas as pd
import csv

txt_file = r"/Users/ShwetaPipaliya/Desktop/report_to_text_to_csv/subfolder/SRR3177947.fastq.txt"
csv_file = r"/Users/ShwetaPipaliya/Desktop/report_to_text_to_csv/subfolder/SRR3177947.csv"
in_txt = csv.reader(open(txt_file, "r"), delimiter = '\t')
out_csv = csv.writer(open(csv_file, 'w'))

out_csv.writerows(in_txt)

txt_file_1 = r"/Users/ShwetaPipaliya/Desktop/report_to_text_to_csv/subfolder/SRR3178010.fastq.txt"
csv_file_1 = r"/Users/ShwetaPipaliya/Desktop/report_to_text_to_csv/subfolder/SRR3178010.csv"
in_txt_1 = csv.reader(open(txt_file_1, "r"), delimiter = '\t')
out_csv_1 = csv.writer(open(csv_file_1, 'w'))

out_csv_1.writerows(in_txt_1)

#following will compile all produced csv files into single combined excel spreadsheet
import os
import glob
import pandas as pd
os.chdir("/Users/ShwetaPipaliya/Desktop/report_to_text_to_csv/subfolder/")

extension = 'csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]

#combine all files in the list
combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames])
#export to csv
combined_csv.to_csv("combined_csv.csv", index=False, encoding='utf-8-sig')

##End