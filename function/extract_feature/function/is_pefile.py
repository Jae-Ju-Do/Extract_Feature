import pefile
import pandas as pd

# pe 여부 판별
def IsPefile(file_path, list_value):
    try:
        pefile.PE(file_path)
        list_value.append(True)
    except Exception as e:
        print(e)
        list_value.append(False)