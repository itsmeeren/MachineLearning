import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Load data from pickle file
with open('your_data.pkl', 'rb') as f:
    data = pickle.load(f)

# Assuming your data is in the format of X (features) and y (target)
X = data['X']
y = data['y']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and fit the model
model = LogisticRegression()
model.fit(X_train, y_train)

# Make predictions on the testing set
y_pred = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

# Optionally, you can save the trained model for later use
# with open('logistic_regression_model.pkl', 'wb') as f:
#     pickle.dump(model, f)
