import pefile
import pandas as pd

def IsPefile(file_path, list_value):
    try:
        pefile.PE(file_path)
        list_value.append(True)
    except Exception as e:
        print(e)
        list_value.append(False)