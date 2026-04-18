"""
Project: Student Success Predictor
Author: Seid Damtew
Algorithm: Linear Regression
Description: This model analyzes the relationship between study time 
             and academic results to predict performance.
"""

import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# 1. Prepare the dataset (Independent and Dependent variables)
# x = Study time in hours, y = Student result percentage

x = np.array([[1], [2], [3], [4], [5], [6]])
y = np.array([10, 20, 30, 42, 50, 60]) 
model = LinearRegression()
model.fit(x, y)

# 2. Initialize and train the Linear Regression model
model = LinearRegression()
model.fit(x, y)

# 3. Make a prediction for a specific value (e.g., 3 hours of study)
hours_to_predict = 7
prediction = model.predict([[hours_to_predict]])

# 4. Evaluate the model performance using R-squared score
y_pred = model.predict(x)
accuracy = r2_score(y, y_pred)

# 5. Display the results
print(f"--- Linear Regression Results ---")
print(f"Predicted result for {hours_to_predict} hours: {prediction[0]:.2f}%")
print(f"Model Accuracy (R-squared): {accuracy:.2f}")
