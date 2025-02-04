import pandas as pd
from label_adder import LableAdder

if __name__ == "__main__":
    data_label = pd.read_csv(r"C:\Users\USER\Desktop\졸업작품\data_file\label\data_label.csv")
    feature_data = pd.read_csv(r"C:\Users\USER\Desktop\졸업작품\function\extract_feature\test.csv")
    output_path = r"C:\Users\USER\Desktop\졸업작품\final_result.csv"
    LableAdder(data_label, feature_data, output_path)