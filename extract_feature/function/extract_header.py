import pefile
import pandas as pd

def ExtractHeaderToDf(header_obj, list_value):
    for field, offset in header_obj.__field_offsets__.items():
        value = getattr(header_obj, field)
        if isinstance(value, bytes): 
            value = ' '.join([f'{byte:02x}' for byte in value])
        elif isinstance(value, int):
            value = hex(value)
        list_value.append(value)


def ExtractHeader(file_path, list_value):
    pe = pefile.PE(file_path)

    headers = {
        "DOS_HEADER": pe.DOS_HEADER,
        "NT_HEADERS": pe.NT_HEADERS,
        "FILE_HEADER": pe.FILE_HEADER,
        "OPTIONAL_HEADER": pe.OPTIONAL_HEADER,
    }

    for header_name, header_obj in headers.items():
        ExtractHeaderToDf(header_obj, list_value)
