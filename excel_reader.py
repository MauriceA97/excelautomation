import pandas as pd
import numpy as np
import os
from pathlib import Path


def filter_by_email(df):
    return sort_by_name(df[df['Emails'].notna()]).fillna('')

def read_spreadsheet(row_start):
    excel_file = [file for file in os.listdir(Path.cwd()) if file.split('.')[-1] == 'xlsx'][0]
    df = pd.read_excel(excel_file, header=row_start-1)

    df['Name'] = df['Name'].str.upper() 
    return df_to_dict(filter_by_email(df)[['Name', 'Emails']])

def sort_by_name(df):
    return df.sort_values(by=['Name'], ascending=True)

def df_to_dict(df):
    return pd.Series(df.Emails.values,index=df.Name).to_dict()