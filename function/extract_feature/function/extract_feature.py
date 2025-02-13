from .is_pefile import IsPefile
from .extract_header import ExtractHeader
from .extract_section import ExtractSection
from .extract_dir_entropy import ExtractDirEntropy
from .extract_export import ExtractExport
from .extract_import import ExtractImport
from .extract_dll import ExtractDll
from .extract_byte_entropy import ExtractByteEntropy

from value.extract_feature.total_value import total_value

import os
import pandas as pd

# 파일의 특징 추출
def ExtractFeatureFile(dir, name):
    df = pd.DataFrame(columns=['Key', 'Value'])
    list_value = []
    list_value.append(name)
    file_path = os.path.join(dir, name)
    IsPefile(file_path, list_value)
    if list_value[1]:
        try:
            ExtractHeader(file_path, list_value)
        except Exception as e:
            list_value[2:60] = [0] * 58
            print(f"추출 오류(ExtractHeader): {e}")

        try:
            ExtractSection(file_path, list_value)
        except Exception as e:
            list_value[60:300] = [0] * 240 
            print(f"추출 오류(ExtractSection): {e}")

        try:
            ExtractDirEntropy(file_path, list_value)
        except Exception as e:
            list_value[300:348] = [0] * 48 
            print(f"추출 오류(ExtractDirEntropy): {e}")
        
        try:
            ExtractExport(file_path, list_value)
        except Exception as e:
            list_value[348:349] = [0] * 1
            print(f"추출 오류(ExtractExport): {e}")

        try:
            ExtractImport(file_path, list_value)
        except Exception as e:
            list_value[349:759] = [0] * 410
            print(f"추출 오류(ExtractImport): {e}")

        try:
            ExtractDll(file_path, list_value)
        except Exception as e:
            list_value[759:818] = [0] * 59
            print(f"추출 오류(ExtractDll): {e}")
        
        try:
            ExtractByteEntropy(file_path, list_value)
        except Exception as e:
            list_value[818:882] = [0] * 64 
            print(f"추출 오류(ExtractByteEntropy): {e}")
    else:
        list_value[2:] = [0] * (len(total_value) - 2)
        print("추출(IsPefile): pe 파일이 아닙니다.")

    data_dict = {'Key': total_value[:len(list_value)], 'Value': list_value}
    df = pd.DataFrame(data_dict)

    df = df.set_index('Key').T 
    return df


# 디렉토리의 내부 파일 접근 후 파일 특징 추출
def ExtractFeatureDir(dir):
    all_data = []
    number = 0
    for file_name in os.listdir(dir):
        if file_name.endswith(".exe") or file_name.endswith(".dll") or (file_name.endswith(".vir")):
            number += 1
            print(f"{number} || {file_name}") 
            file_data = ExtractFeatureFile(dir, file_name)
            all_data.append(file_data)  

    combined_df = pd.concat(all_data, ignore_index=True)
    return combined_df
