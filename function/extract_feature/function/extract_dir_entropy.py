import pefile
from value.extract_feature.dir_entropy import directory_names

# dir 엔트로피 추출 
def ExtractDirEntropy(file_path, list_value):
    pe = pefile.PE(file_path)
    
    for directory_name in directory_names:
        full_directory_name = f"IMAGE_DIRECTORY_ENTRY_{directory_name}"

        directory_found = False
        for directory in pe.OPTIONAL_HEADER.DATA_DIRECTORY:
            if directory.name == full_directory_name:
                directory_found = True
                
                value = hasattr(pe, directory.name.replace("IMAGE_", ""))
                list_value.append(value)
                list_value.append(hex(directory.VirtualAddress))
                list_value.append(directory.Size)
                break
        
        if not directory_found:
            list_value.append(False) 
            list_value.append(None)   
            list_value.append(None)   
            print(f"Directory {full_directory_name} not found.")