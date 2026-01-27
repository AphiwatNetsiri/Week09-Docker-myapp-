from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# Load diabetes dataset
data = datasets.load_diabetes()
X = data.data
y = (data.target > data.target.mean()).astype(int)  # Convert to binary classification

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=123)

# Train model
best_model = RandomForestClassifier(random_state=123)
best_model.fit(X_train, y_train)

# Evaluate
y_pred = best_model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print(f"Best Model: Random Forest Classifier")
print(f"Accuracy: {accuracy:.4f}")
print("\nClassification Report:")
print(classification_report(y_test, y_pred))