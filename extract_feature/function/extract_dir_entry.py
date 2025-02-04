import pefile

def ExtractDirEntry(file_path, list_value):
    pe = pefile.PE(file_path)
    for directory in pe.OPTIONAL_HEADER.DATA_DIRECTORY:
        value = False
        if hasattr(pe, directory.name.replace("IMAGE_", "")):
             value = True
        list_value.append(value)        
        list_value.append(hex(directory.VirtualAddress))        
        list_value.append(directory.Size)        