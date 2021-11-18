"""
Excel file to fasta.txt file conversion

Following excel formats are acceptable: xls, xlsx, xlsm, xlsb, odf, ods,odt
path == A full (absolute) path to the excel file
org_col == name of columns (a list [] of strings or one string if only one column present) containing the organism info (Genus, Species etc.)
sequence_col == a name of a column (as a string) containing the sequence
sheet == name of the excel sheet
file_name == chosen name for the fasta file

"""

import numpy
import pandas as pd
import os
from pathlib import Path

#excel file(xls, xlsx, xlsm, xlsb, odf, ods,odt) to fasta
    def excel_to_fasta(path, org_col, sequence_col, sheet, file_name):
        seq_path = str(Path.home()) + str('/results')
        path = path
        sequence_col = list(sequence_col.split(",")) #always only one element list
        sheet = sheet
        file_name = file_name
        if isinstance(org_col, list):
            org_col = (org_col)
        else:
            org_col = (list(org_col.split(",")))
        
        
    #we need to merge columns from org_col (if there is more than one)
        try:
                columns = org_col + sequence_col
                excel_df = pd.read_excel(path, sheet_name= sheet, usecols= columns, header = 0)
                excel_df['id'] = '>' + excel_df[org_col].apply(lambda x:'_'.join(x), axis=1) + '\n'
                excel_df['id'] = excel_df['id'].str.replace(" ","")
                id_col = excel_df.pop('id')
                excel_df.insert(0, 'id', id_col)
                excel_df = excel_df.drop(labels = org_col, axis = 'columns')
                
                #dataframe to array
                numpy_array = excel_df.to_numpy()
                file_name = file_name + '.fa'
                results_path= str(os.path.join(seq_path, file_name))
                
                #save file as txt
                np.savetxt(fname = results_path, X = numpy_array, delimiter = ' ', fmt='%s')
                return print(file_name + " " + "has been saved in" + " " + results_path)

        except (KeyError, ValueError):
            print("The column names provided must be correct and case sensitive")
            sys.exit(0)
        except Exception as e:
            print(e)



