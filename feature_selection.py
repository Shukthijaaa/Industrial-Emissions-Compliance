import pandas as pd
from sklearn.model_selection import train_test_split
from model_preparation import prepare_data

# Get prepared data
X, y = prepare_data()

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("Training set size:", X_train.shape)
print("Testing set size:", X_test.shape)