from .is_pefile import IsPefile
from .extract_header import ExtractHeader
from .extract_section import ExtractSection
from .extract_dir_entry import ExtractDirEntry
from .extract_export import ExtractExport
from .extract_import import ExtractImport
from .extract_dll import ExtractDll
from .extract_byte_entropy import ExtractByteEntropy

from value.total_value import total_value
import os
import pandas as pd

def ExtractFeatureFile(dir, name):
    df = pd.DataFrame(columns=['Key', 'Value'])
    list_value = []
    list_value.append(name)
    file_path = os.path.join(dir, name)
    IsPefile(file_path, list_value)
    if list_value[1]:
        try:
            ExtractHeader(file_path, list_value)
            ExtractSection(file_path, list_value)
            ExtractDirEntry(file_path, list_value)
            ExtractExport(file_path, list_value)
            ExtractImport(file_path, list_value)
            ExtractDll(file_path, list_value)
            ExtractByteEntropy(file_path, list_value)
        except Exception as e:
            list_value[2:] = [0] * (len(total_value) - 2)
    else:
        list_value[2:] = [0] * (len(total_value) - 2)

    data_dict = {'Key': total_value[:len(list_value)], 'Value': list_value}
    df = pd.DataFrame(data_dict)

    df = df.set_index('Key').T 

    return df

def ExtractFeatureDir(dir):
    all_data = []
    number = 0
    for file_name in os.listdir(dir):
        if file_name.endswith(".exe") or file_name.endswith(".dll") or (file_name.endswith(".vir")):
            number += 1
            print(f"{number} || {file_name}") 
            file_data = ExtractFeatureFile(dir, file_name)
            all_data.append(file_data)  
            if number == 1000:
                break

    combined_df = pd.concat(all_data, ignore_index=True)
    return combined_df
