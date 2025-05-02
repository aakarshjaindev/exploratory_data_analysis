def load_data(file_path):
    import pandas as pd
    # Load the dataset from the specified file path
    data = pd.read_csv(file_path)
    return data

def preprocess_data(data):
    # Perform data cleaning and transformation
    # Example: Handling missing values, encoding categorical variables, etc.
    
    # Drop rows with missing values
    data = data.dropna()
    
    # Example transformation: Convert categorical columns to dummy variables
    data = pd.get_dummies(data, drop_first=True)
    
    return data