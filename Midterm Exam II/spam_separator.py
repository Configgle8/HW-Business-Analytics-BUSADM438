import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import f1_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier

#Load CSV
emails = pd.read_csv("Midterm Exam II/emails_shuffle.csv")

#TF-IDF
vectorizer = TfidfVectorizer(stop_words='english', min_df=0.05, max_df=0.95)
X_features = vectorizer.fit_transform(emails['text'])
labels = emails['spam']

#Data division
train_X = X_features[:4500]
test_X = X_features[4500:]
train_y = labels[:4500]
test_y = labels[4500:]

#Tree Training
tree_grid = GridSearchCV(
    DecisionTreeClassifier(),
    {
        'max_depth': [5, 6, 7, 25],
        'min_samples_split': [5, 10, 15, 20],
        'max_features': ['sqrt', 'log2', None]
    },
    cv=5,
    scoring='f1'
)
tree_grid.fit(train_X, train_y)
tree_model = DecisionTreeClassifier(**tree_grid.best_params_)
tree_model.fit(train_X, train_y)
tree_preds = tree_model.predict(test_X)
tree_error = (tree_preds != test_y).mean()
tree_f1 = f1_score(test_y, tree_preds)

#KNNeighbor Training
knn_grid = GridSearchCV(
    KNeighborsClassifier(),
    {
        'n_neighbors': [5, 6, 7, 25],
        'weights': ['uniform', 'distance'],
        'metric': ['euclidean', 'manhattan', 'minkowski']
    },
    cv=5,
    scoring='f1'
)
knn_grid.fit(train_X, train_y)
knn_model = KNeighborsClassifier(**knn_grid.best_params_)
knn_model.fit(train_X, train_y)
knn_preds = knn_model.predict(test_X)
knn_error = (knn_preds != test_y).mean()
knn_f1 = f1_score(test_y, knn_preds)

#print evals

print("DT Error:", tree_error)
print("DT F1:", tree_f1)
print("KNN Error:", knn_error)
print("KNN F1:", knn_f1)

#bonus comparative statement

if tree_f1 > knn_f1:
    best_model ="Decision Tree"
    best_f1 = tree_f1
    best_error = tree_error
else:
    best_model = "Nearest Neighbor"
    best_f1 = knn_f1
    best_error = knn_error

print(f"\nComparison Found! :")
print(f"The best model in terms of F1 score is {best_model}.")
print(f"The {best_model} has the highest F1 score & the lower error rate.")