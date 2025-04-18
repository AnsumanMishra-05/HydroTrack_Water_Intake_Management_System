import pickle
from sklearn.linear_model import LinearRegression

# Sample dataset: [age, weight, activity_level]
X = [
    [18, 65, 1],
    [22, 70, 2],
    [25, 80, 3],
    [30, 75, 2],
    [35, 85, 3],
    [40, 90, 1],
    [45, 95, 2]
]

# Corresponding water intake in liters
y = [2.5, 2.8, 3.2, 3.0, 3.5, 2.9, 3.1]

# Train and save the model
model = LinearRegression()
model.fit(X, y)

# Save to model.pkl
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ Model trained and saved as model.pkl")
