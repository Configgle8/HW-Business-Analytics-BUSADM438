import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import f1_score

# Load & preprocessing
df = pd.read_csv('HW7/bank_shuffle.csv')
df['y'] = df['y'].map({'yes': 1, 'no': 0})
df = pd.get_dummies(df)

split = int(len(df) * 0.8)
X_train, y_train = df.iloc[:split].drop('y', axis=1), df.iloc[:split]['y']
X_test, y_test = df.iloc[split:].drop('y', axis=1), df.iloc[split:]['y']

#5-fold CV
params = {'criterion': ['gini', 'entropy'], 'max_depth': range(4, 21)}
grid = GridSearchCV(DecisionTreeClassifier(random_state=42), params, cv=5, scoring='f1', n_jobs=-1)
grid.fit(X_train, y_train)

model = grid.best_estimator_
y_pred = model.predict(X_test)
error_rate = (y_pred != y_test).mean()
f1 = f1_score(y_test, y_pred)

print("Error Rate:", error_rate)
print("F1 Score:", f1)
print("Best Parameters:", grid.best_params_)
