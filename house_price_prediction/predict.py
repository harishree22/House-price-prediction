import joblib

model = joblib.load("house_price_model.pkl")

print("🏠 House Price Prediction")

area = float(input("Enter area (sq ft): "))
bed = int(input("Enter bedrooms: "))
bath = int(input("Enter bathrooms: "))
age = int(input("Enter house age: "))

price = model.predict([[area, bed, bath, age]])

print(f"\n💰 Estimated House Price: ₹ {int(price[0]):,}")
