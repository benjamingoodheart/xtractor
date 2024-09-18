"""
Extractor package for programmatically extracting pdfs from csv's
"""
__version__= 0.1

import sys
import os
import pdfplumber
import pandas as pd
import tqdm

class Xtractor:
    """
    Class to extract tables from a pdf file and write to a csv
    """
    def __init__(self,pdf_path:str)-> None:
        if self.validate_path(pdf_path) is True:
            self.pdf_path = pdf_path
            self.output = "out/all_cleaned.csv"
        else:
            raise FileNotFoundError("File does not exist")
        
    def run_extractor(self, *drop_first_row: bool) -> None:
        """
        Main process method. Optionally takes a bool to 
        drop the first row or not
        """
        with pdfplumber.open(self.pdf_path) as pdf:
            pages = pdf.pages
            data = []
            for _ in tqdm.tqdm(range(len(pages)), desc="Extracting Table"): # for progress bar
                for page in pages:
                    table = page.extract_table(table_settings={})
                    for row in table:
                        data.append(row) # quicker to append to array and then make a dataframe from that 
                df = pd.DataFrame(data, columns=data[0])
                if drop_first_row:
                    df = self.drop_first_row(df) #may have to adjust depending on data
               
                df.to_csv(self.output)
    
    def set_output(self, path: str) -> None:
        """_summary_

        Args:
            path (str): _description_
        """
        self.output = path

    def validate_path(self,path: str):

        return os.path.exists(path)
    
    def drop_first_row(self, df:pd.DataFrame) -> pd.DataFrame:
        """
        Utility class to drop the first row of a DataFrame

        Args:
            df (pd.DataFrame): _description_

        Returns:
            pd.DataFrame: _description_
        """
        return df.drop([0])
        

if __name__ == "__main__":
    if(len(sys.argv) == 2 or len(sys.argv) == 3):
        try:
            if len(sys.argv) == 3:
                xtractor = Xtractor(sys.argv[1])
                if sys.argv[2] == "--dfr":
                    xtractor.run_extractor(True)
                else:
                    xtractor.run_extractor()
            else:
                xtractor = Xtractor(sys.argv[1])
                xtractor.run_extractor()
        except ValueError as e:
            print("Error: ", e)
    elif(len(sys.argv) > 3):
        raise ValueError('Extractor only accepts two argument <path> --dfr ')
    else:
        raise ValueError('No Path specified for the pdf! Run python3 extractor.py <pdf/path>')
