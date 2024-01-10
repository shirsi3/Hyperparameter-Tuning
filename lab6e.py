import pandas as pd
import numpy as np
import json
from sklearn import metrics
import matplotlib.pyplot as plt
from sklearn.svm import SVC 


samples_df = pd.read_csv("samples.csv")

samples_df['target'] = (samples_df['label'] == 'malware').astype(int)


with open("detector.log", "r") as log_file:
    detector_log_lines = log_file.readlines()

log_messages = [json.loads(line.strip()) for line in detector_log_lines]

y_true = samples_df['target'].values
y_pred = [1 if message['classification'] == "malware" else 0 for message in log_messages]
y_proba = [1.0 if message['classification'] == "malware" else 0.0 for message in log_messages]


classification_report = metrics.classification_report(y_true, y_pred)
confusion_matrix = metrics.confusion_matrix(y_true, y_pred)

print("Classification Report:\n", classification_report)
print("Confusion Matrix:\n", confusion_matrix)

model = SVC(kernel='rbf', C=1.5)

fpr, tpr, thresholds = metrics.roc_curve(y_true, y_proba)
roc_auc = metrics.auc(fpr, tpr)

plt.figure()
plt.plot(fpr, tpr, color='darkorange', lw=2, label='ROC curve (area = %0.2f)' % roc_auc)
plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver Operating Characteristic')
plt.legend(loc='lower right')
plt.show()
