import pefile
from .calculate_entropy import CalculateEntropy
from value.section_value import section_list, section_object

def ExtractSectionToDf(section_save, section_object, section_check, list_value):
    value = []
    if section_check:
        for key in section_object:
            if hasattr(section_save, key):
                value.append(hex(getattr(section_save, key)))
            else:
                value.append(0)
        section_data = section_save.get_data()
        entropy = CalculateEntropy(section_data)
        value.append(entropy)
    else:
        for key in section_object:
            value.append(0)
        value.append(0)
    list_value += value

def ExtractSection(file_path, list_value):
    pe = pefile.PE(file_path)

    for section_name in section_list:
        section_check = False
        section_save = None
        for section in pe.sections:
            if section.Name.decode().rstrip('\x00') == section_name:
                section_check = True
                section_save = section
        ExtractSectionToDf(section_save, section_object, section_check, list_value)
