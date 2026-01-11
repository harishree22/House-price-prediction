import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import joblib

# Load data
data = pd.read_csv("data.csv")

X = data[["Area", "Bedrooms", "Bathrooms", "Age"]]
y = data["Price"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Save model
joblib.dump(model, "house_price_model.pkl")

print("✅ Model trained and saved as house_price_model.pkl")
