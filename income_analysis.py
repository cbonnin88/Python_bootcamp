import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

#%%
income_data = pd.read_csv("income_evaluation.csv")
print(income_data)

#%%
print(income_data.head)
print("The data row count is : {}".format(income_data.shape[0]))
print(income_data.columns)

#%%
oldest_employee = income_data.iloc[income_data["age"].idxmax()]
print(oldest_employee)

#%%
youngest_employee = income_data.iloc[income_data["age"].idxmin()]
print(youngest_employee)

#%%
print(income_data[' workclass'].value_counts().sort_values(ascending=False))
print(income_data[' income'].value_counts().sort_values(ascending=True))

#%%
# Income Levels
matplotlib.rc("figure", figsize=(20, 10))

income_data[' income'].value_counts().plot(kind="bar")
plt.title("Income Level Counts")
plt.show()

#%%
# Education Levels
print(income_data[' education'].value_counts())

income_data[' education'].value_counts().plot(kind="bar")
plt.title("Education Level Counts")
plt.show()

#%%
# Sex :
sex_labels = income_data[' sex'].unique()
plt.pie(income_data[' sex'].value_counts(),labels = sex_labels)
plt.show()

#%%
# Marital Status:
marital_status_labels = income_data[' marital-status'].unique()
plt.pie(income_data[' marital-status'].value_counts(), labels=marital_status_labels)
plt.show()
#%%
data = income_data[
    ['age', ' workclass', ' education', ' marital-status', ' occupation', ' hours-per-week', ' native-country',
     ' income']]
data.columns = [
    ['age', ' workclass', ' education', ' marital-status', ' occupation', ' hours-per-week', ' native-country',
     ' income']]

data.head()

#%%
print(data.isna().sum())
print(data.duplicated().sum())

#%%
data.drop_duplicates(inplace=True)
print(data.duplicated().sum())

