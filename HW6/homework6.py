import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import KFold
from sklearn.neighbors import KNeighborsRegressor
from sklearn.preprocessing import MinMaxScaler

#dataframe
df = pd.read_csv('HW6/susedcars.csv', usecols=['price', 'mileage', 'year'])
df['age'] = 2015 - df.pop('year')
X = df[['mileage', 'age']].to_numpy()
y = df['price'].to_numpy()

scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)

kf = KFold(n_splits=5, shuffle=True, random_state=1)
k_values = range(1, 31)
sse_list = []

for k in k_values:
    sse = 0
    for train_index, test_index in kf.split(X_scaled):
        X_train, X_test = X_scaled[train_index], X_scaled[test_index]
        y_train, y_test = y[train_index], y[test_index]
        model = KNeighborsRegressor(n_neighbors=k)
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        sse += np.sum((y_pred - y_test) ** 2)
    sse_list.append(sse)

# Plot
plt.plot(k_values, sse_list)
plt.xlabel('k')
plt.ylabel('SSE')
plt.title('5-Fold CV: k vs SSE')
plt.grid()
plt.show()

# Optimized K expected val
optimal_k = k_values[np.argmin(sse_list)]
print(f"Optimal k: {optimal_k}")

knn = KNeighborsRegressor(n_neighbors=optimal_k)
knn.fit(X_scaled, y)

# Predict
new_data = np.array([[100000, 10], [50000, 3]])
new_data_scaled = scaler.transform(new_data)
predictions = knn.predict(new_data_scaled)

print(f'Predicted price for mileage=100000 and age=10: {predictions[0]}')
print(f'Predicted price for mileage=50000 and age=3: {predictions[1]}')
