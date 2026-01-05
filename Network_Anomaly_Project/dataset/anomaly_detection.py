import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import IsolationForest
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv("kddcup.csv", header=None)

# Keep only numeric columns
data = data.select_dtypes(include=['int64', 'float64'])

# Remove missing values
data = data.dropna()

# Scale features
scaler = StandardScaler()
scaled_data = scaler.fit_transform(data)

# Train Isolation Forest model
model = IsolationForest(
    n_estimators=100,
    contamination=0.05,
    random_state=42
)
model.fit(scaled_data)

# Predict anomalies
data['anomaly'] = model.predict(scaled_data)

# Show result count
print(data['anomaly'].value_counts())

# Plot result
plt.hist(data['anomaly'])
plt.title("Network Traffic Anomaly Detection")
plt.show()
