import pandas as pd

#change these as needed
file_path = 'project/val.csv'
corrected_file_path = 'project/corrected_val.csv'

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

data.to_csv(corrected_file_path, index=False)

corrected_file_path