import pandas as pd
from sklearn.svm import SVC
from sklearn.model_selection import StratifiedKFold, GridSearchCV
from sklearn.metrics import f1_score


data = pd.read_csv("reduceddataset.csv")


label_mapping = {'malware': 1, 'benignware': 0}
data['label'] = data['label'].map(label_mapping)


X = data.drop(["MD5", "Target", "label"], axis=1)
y = data['label']


param_space = {
    'kernel': ['linear', 'poly', 'rbf'],
    'C': [0.1, 1.0, 10.0],
    'tol': [1e-5, 1e-3, 0.01]
}

cv = StratifiedKFold(n_splits=10, shuffle=True, random_state=42)


model = SVC()


search = GridSearchCV(model, param_space, scoring='f1', cv=cv)


search.fit(X, y)


print("Best Parameters:", search.best_params_)
print("Best Score (F1):", search.best_score_)
