#!/usr/bin/env python
# coding=utf-8

import argparse
import os
from docx2pdf import convert  # convert docx to pdf
import datetime

today = str(datetime.date.today())
print(today)

def createPdf(input_file, output_file):
    """this function creates a new pdf document 
    based on a specific docx document"""
    convert(f'{input_file}',f'{output_file}')
    if os.path.isfile(output_file):
        status = True
    else:
        status = False
    return status

def main(args):
    in_file = args.files_path + args.docx_filename
    out_file = args.files_path + args.pdf_filename
    result = createPdf(in_file, out_file)
    if result:
        print('File Created')
    else:
        print('Failure')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Convert MS Doc(x) file to PDF File')
    parser.add_argument('--inputfile', type=str, dest='docx_filename', help='Sample docx file name value', required=True)
    parser.add_argument('--outputfile', type=str, dest='pdf_filename', help='Sample pdf file name value', required=True)
    parser.add_argument('--path', type=str, dest='files_path', help='Path where files stored', default='./generator/docx2pdf/assets/')

    args = parser.parse_args()
    main(args)