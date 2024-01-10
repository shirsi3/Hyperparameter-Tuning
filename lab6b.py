import pandas as pd
from sklearn.svm import SVC
from sklearn.model_selection import StratifiedKFold, RandomizedSearchCV
from sklearn.metrics import f1_score
from scipy.stats import loguniform


data = pd.read_csv("reduced_dataset.csv")

label_mapping = {'malware': 1, 'benignware': 0}
data['label'] = data['label'].map(label_mapping)


X = data.drop(["MD5", "Target", "label"], axis=1)
y = data['label']

param_space = {
    'kernel': ['linear', 'poly', 'rbf'],
    'C': loguniform(1e-5, 100),
    'tol': loguniform(1e-5, 100)
}


cv = StratifiedKFold(n_splits=10, shuffle=True, random_state=42)

model = SVC()


search = RandomizedSearchCV(model, param_space, n_iter=500, scoring='f1', cv=cv, random_state=42)


search.fit(X,y)

print("Best Parameters:", search.best_params_)
print("Best Score (F1):", search.best_score_)
