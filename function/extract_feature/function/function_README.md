# function

`function`는 extract_feature에 사용되는 함수를 저장한 디렉토리입니다.

## 목록
### 1. extract_feature.py
`extract_feature.py`는 PE 파일의 특징을 추출하는 함수입니다.

2 ~ 10의 함수를 이용해 PE 파일의 특징을 추출합니다.

### 2. is_pefile.py
`is_pefile.py`는 파일이 PE 파일인지 확인하는 함수입니다.

### 3. calclulate_entropy.py
`calclulate_entropy.py`는 주어진 데이터의 엔트로피를 계산하는 함수입니다.

### 4. extract_byte_entropy.py
`extract_byte_entropy.py`는 PE 파일의 바이트 데이터를 분석해 엔트로피 히스토그램을 생성하고, 히스토그램을 특징으로 추출하는 함수입니다.

### 5. extract_dir_entry.py
`extract_dir_entry.py`는 PE 파일의 데이터 디렉터리 엔트로피 정보를 추출하는 함수입니다.

### 6. extract_dll.py
`extract_dll.py`는 PE 파일에서 DLL(동적 링크 라이브러리) 정보를 추출하는 함수입니다.

### 7. extract_export.py
`extract_export.py`는 PE 파일에서 export 심볼의 수를 추출하는 함수입니다.

### 8. extract_header.py
`extract_header.py`는 PE 파일에서 특정 헤더 정보를 추출하는 함수입니다.

### 9. extract_import.py
`extract_import.py`는 PE 파일에서 import 총개수와 import된 라이브러리의 개수를 추출하는 함수입니다.

### 10. extract_section.py
`extract_section.py`는 PE 파일에서 섹션 데이터를 추출하는 함수입니다.