import pandas as pd

# label과 feature를 합치는 함수
def LableAdder(data_label, feature_data, output_path):
    result = pd.merge(feature_data, data_label, on='file_name', how='left')

    print(result)
    result.to_csv(output_path, index=False)
    