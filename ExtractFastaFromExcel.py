"""
Excel file to fasta.txt file conversion

Following excel formats are acceptable: xls, xlsx, xlsm, xlsb, odf, ods,odt
path == A full path to the excel file
org_col == name of columns (in a list [] format or string if only one column present) containing the organism info (Genus, Species etc.)
sequence_col == a name of a column (as a string) containing the sequence
sheet == name of the excel sheet
file_name == chosen name for the fasta file

"""

import numpy as np
import pandas as pd
import os
import openpyxl

def excel_to_fasta(self, path, org_col, sequence_col, sheet, file_name):
    self.path = path
    self.sequence_col = list(sequence_col.split(",")) #always only one element list
    self.sheet = sheet
    self.file_name = file_name
 
#in case more than one org_col is provided:
    if isinstance(org_col, list):
        self.org_col = org_col
    else:
        self.org_col = list(org_col.split(","))
 #need to merge columns from org_col (if there is more than one)
     try:
        self.columns = self.org_col + self.sequence_col
        excel_df = pd.read_excel(self.path, sheet_name= self.sheet, usecols= self.columns, header = 0)
        excel_df['id'] = '>' + excel_df[self.org_col].apply(lambda x:'_'.join(x), axis=1)
        excel_df['id'] = excel_df['id'].str.replace(" ","")
        id_col = excel_df.pop('id')
        excel_df.insert(0, 'id', id_col)
        excel_df = excel_df.drop(self.org_col,1)

        #dataframe to array
        numpy_array = excel_df.to_numpy()
        file_name = self.file_name + '.txt'

        #save file as txt
        np.savetxt(fname = str(os.path.join(seq_path, file_name)), X = numpy_array, delimiter = ' ', fmt='%s')
        return file_name + " " + "has been saved in the ""files"" folder"

    except (KeyError, ValueError) as error:
        return "The column names provided must be correct and case sensitive"
        
