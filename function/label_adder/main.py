import pandas as pd
from function.label_adder import LableAdder

if __name__ == "__main__":
    label = pd.read_csv(input("라벨이 저장된 csv 위치 입력 : "))
    feature_data = pd.read_csv(input("추출된 특징이 저장된 csv 위치 입력 : "))
    output_path = input("특징과 라벨이 합쳐진 결과 저장할 csv 위치 입력 : ")
    LableAdder(label, feature_data, output_path)