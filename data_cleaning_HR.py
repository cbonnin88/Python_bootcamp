import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

# Load our Dataset
hr_data = pd.read_csv("HR_data.csv")

# Explore data and identify missing values, outliers, etc
print("Original Data: ")
print(hr_data.head())

# Define the preprocessing steps for the numerical and categorical features
numeric_features = hr_data.select_dtypes(include=["int64", "float64"]).columns
numeric_transformer = Pipeline(steps=[("imputer", SimpleImputer(strategy="mean")),
                                      ("scaler", StandardScaler())])

categorical_features = hr_data.select_dtypes(include=["object"]).columns
categorical_transformers = Pipeline(
    steps=[("imputer", SimpleImputer(strategy="most_frequent")),
           ("onehot", OneHotEncoder(drop="first"))])  # Added
# drop "first" parameter

# Combine preprocessing steps for numerical and categorical features
preprocessor = ColumnTransformer(transformers=[("num", numeric_transformer, numeric_features),
                                               ("cat", categorical_transformers, categorical_features)])

# Apply preprocessing steps to the data
hr_data_cleaned = preprocessor.fit_transform(hr_data)

# Convert the cleaned data back to a Data Frame
cleaned_columns = numeric_features.to_list() + preprocessor.named_transformers_["cat"]["onehot"] \
    .get_feature_names_out(categorical_features).tolist()

hr_data_cleaned = pd.DataFrame(hr_data_cleaned, columns=cleaned_columns)

# display the clean data
print("\nCleaned Data: ")
print(hr_data_cleaned.head())
