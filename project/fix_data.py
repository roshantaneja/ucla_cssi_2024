import pandas as pd

# Load the CSV file
file_path = '/mnt/data/train.csv'
data = pd.read_csv(file_path)

# Function to check if a value can be converted to an integer
def is_integer(value):
    try:
        int(value)
        return True
    except ValueError:
        return False

# Detect and correct issues in Age and Gender columns
for index, row in data.iterrows():
    age = row['Age']
    gender = row['Gender']
    
    if not is_integer(age) and is_integer(gender):
        # Swap values if age is not an integer but gender is
        data.at[index, 'Age'] = gender
        data.at[index, 'Gender'] = age

# Convert Age column to numeric
data['Age'] = pd.to_numeric(data['Age'], errors='coerce')

# Display the corrected dataframe
import ace_tools as tools; tools.display_dataframe_to_user(name="Corrected Data", dataframe=data)

# Save the corrected dataframe to a new CSV file
corrected_file_path = '/mnt/data/corrected_train.csv'
data.to_csv(corrected_file_path, index=False)

corrected_file_path