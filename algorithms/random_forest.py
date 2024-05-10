import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load data from pickle file
with open('your_data.pkl', 'rb') as f:
    data = pickle.load(f)

# Assuming your data is in the format of X (features) and y (target)
X = data['X']
y = data['y']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and fit the Random Forest model
model = RandomForestClassifier(n_estimators=100, criterion='entropy', random_state=42)
model.fit(X_train, y_train)

# Make predictions on the testing set
y_pred = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

# Optionally, you can save the trained model for later use
# with open('random_forest_model.pkl', 'wb') as f:
#     pickle.dump(model, f)


#For the random forest the metrics =entropy is not used because there are more trees which internally 
# the classifier itself will have so
