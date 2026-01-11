import tkinter as tk
from tkinter import messagebox
import joblib

model = joblib.load("house_price_model.pkl")

def predict_price():
    try:
        a = float(area.get())
        b = int(bed.get())
        ba = int(bath.get())
        ag = int(age.get())

        result = model.predict([[a, b, ba, ag]])
        messagebox.showinfo("Result", f"Estimated Price: ₹ {int(result[0]):,}")
    except:
        messagebox.showerror("Error", "Please enter valid numbers")

root = tk.Tk()
root.title("House Price Predictor")
root.geometry("400x400")

tk.Label(root, text="House Price Prediction",
         font=("Arial", 16, "bold")).pack(pady=15)

area = tk.Entry(root)
bed = tk.Entry(root)
bath = tk.Entry(root)
age = tk.Entry(root)

for label, box in zip(
    ["Area", "Bedrooms", "Bathrooms", "Age"],
    [area, bed, bath, age]
):
    tk.Label(root, text=label).pack()
    box.pack()

tk.Button(root, text="Predict Price",
          command=predict_price).pack(pady=20)

root.mainloop()
