import warnings
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Creating our example data
company_data = {
    "Companies": ['Starfield Enterprise', 'Sandersand Consultants', 'Spearsmann', 'GreenTech', 'Vegna Mining Company'],
    "Total Revenue": [400000000, 800000000, 200000000, 400000000, 900000000],
    "Hiring Budget": [250000, 100000000, 170000, 599000, 105000000]
}

df = pd.DataFrame(company_data)

# Splitting the data into training and testing sets
x = df['Total Revenue'].values.reshape(-1, 1)
y = df['Hiring Budget'].values

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# Here I am creating a Linear Regression model
lr_model = LinearRegression()

# Fit the model to the training data
lr_model.fit(x_train, y_train)

# Making predictions on the test data
y_prediction = lr_model.predict(x_test)

# Suppress all warnings
warnings.filterwarnings("ignore")

# Evaluate our model
mse = mean_squared_error(y_test, y_prediction)
r2 = r2_score(y_test, y_prediction)

# Print the results
print(f"Mean Squared Error: {mse}")
print(f"R-squared: {r2}")

# Predicting the hiring budget of our companies
hiring_budget = [[599000]]
predicted_hiring_budget = lr_model.predict(hiring_budget)
print(f"Predicted Hiring Budget for GreenTech: {predicted_hiring_budget[0]}")

# visualization
plt.figure(figsize=(10, 6))

# Scatter Plot of our original data
plt.scatter(x, y, color='blue', label='Current Budget')

# Plot the regression Line
plt.plot(x_test, y_prediction, color='red', linewidth=2, label='Regression Line')

# Plot the prediction for the new country
plt.scatter(hiring_budget,predicted_hiring_budget, color='green',marker='s',s=100,label='Predicted Hiring Budget for '
                                                                                        'GreenTech')

plt.title("Hiring Budget Prediction")
plt.xlabel("Total Revenue")
plt.ylabel("Hiring Budget")
plt.legend()
plt.grid(True)
plt.show()

