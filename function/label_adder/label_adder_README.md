# label_adder

`label_adder`는 Extract_Feature에서 뽑은 csv에 **라벨을 추가**하는 함수입니다. 

이 함수는 머신 러닝 모델 학습에 필요한 라벨을 csv 데이터에 추가할 때 유용합니다.

## 실행
### 실행 방법
```cmd
python main.py
```
### 실행 화면
```cmd
C:\Users\USER\Desktop\jaejudo\Extract_Feature> set PYTHONPATH=C:\Users\USER\Desktop\jaejudo\Extract_Feature
C:\Users\USER\Desktop\jaejudo\Extract_Feature> python main.py
라벨이 저장된 csv 위치 입력 : C:\Users\USER\Desktop\jaejudo\Extract_Feature\value\extract_csv
추출된 특징이 저장된 csv 위치 입력 : C:\Users\USER\Desktop\jaejudo\Extract_Feature\value\extract_label_csv\label.csv
특징과 라벨이 합쳐진 결과 저장할 csv 위치 입력 : C:\Users\USER\Desktop\jaejudo\Extract_Feature\value\extract_csv
```

## 목록
### 1. function
`function`는 label_adder에 사용되는 함수를 저장한 디렉토리입니다.

자세한 설명은 [여기를 클릭하여 function 내 함수 설명을 확인하세요](./function/function_README.md).
