import pandas as pd

file_path = 'project/train.csv'
data = pd.read_csv(file_path)

def is_integer(value):
    try:
        int(value)
        return True
    except ValueError:
        return False

for index, row in data.iterrows():
    age = row['Age']
    gender = row['Gender']
    
    if not is_integer(age) and is_integer(gender):
        data.at[index, 'Age'] = gender
        data.at[index, 'Gender'] = age

data['Age'] = pd.to_numeric(data['Age'], errors='coerce')

corrected_file_path = 'project/corrected_train.csv'
data.to_csv(corrected_file_path, index=False)

corrected_file_path