import os
from function.extract_feature import ExtractFeatureDir

if __name__ == "__main__":
    dir = input("특징을 추출할 파일이 있는 디렉토리 위치 : ")
    save_path = os.path.join(r"..\..\value\extract_csv", input("추출된 특징이 저장될 csv 이름 : ") + ".csv")

    save = ExtractFeatureDir(dir)
    save.to_csv(save_path, index=True, encoding='utf-8-sig')