from function.extract_feature import ExtractFeatureDir

    
if __name__ == "__main__":
    dir = r"C:\Users\USER\Desktop\졸업작품\file\nomal"
    save = ExtractFeatureDir(dir)
    save_path = r"C:\Users\USER\Desktop\졸업작품\function\extract_feature\test.csv"
    save.to_csv(save_path, index=True, encoding='utf-8-sig')