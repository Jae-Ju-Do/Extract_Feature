import pefile
import pandas as pd
from value.extract_feature.api_value import import_list

# import 라이브러리 개수 추출
def ImportDirectory(pe, list_value):
    value = [0] * len(import_list)
    try:
        for import_entry in pe.DIRECTORY_ENTRY_IMPORT:
            for import_name in import_entry.imports:
                if import_name.name.decode() in import_list:
                    index = import_list.index(import_name.name.decode())
                    value[index] += 1
    except:
        pass
    finally:
        list_value += value

# import 개수 추출
def ImportLen(pe, list_value):
    pe.parse_data_directories()
    import_len = 0
    for entry in pe.DIRECTORY_ENTRY_IMPORT:
        import_len += len(entry.imports)
    list_value.append(import_len)

# import 데이터 추출
def ExtractImport(file_path, list_value):
    pe = pefile.PE(file_path)
    ImportLen(pe, list_value)
    ImportDirectory(pe, list_value)