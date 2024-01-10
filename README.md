# Lab 6: Malware Analysis and Machine Learning

This lab involves various scripts that deal with malware analysis, file processing, and machine learning using SVM for classification. Each script has a unique role in the broader context of understanding and detecting malware.

## 1. lab6_task1.py - File Hashing and Labeling

- **Functionality:** Calculates MD5 hashes of files in specified directories, possibly labeling them as benign or malware.
- **Libraries Used:** os, hashlib

## 2. lab6b.py - SVM Classification with Randomized Parameter Tuning

- **Functionality:** Uses Support Vector Machines for classification of malware data, with randomized search for hyperparameter optimization.
- **Libraries Used:** pandas, sklearn.svm, sklearn.model_selection, sklearn.metrics, scipy.stats

## 3. lab6c.py - SVM Classification with Grid Search Parameter Tuning

- **Functionality:** Similar to `lab6b.py`, but utilizes grid search for hyperparameter optimization in SVM classification.
- **Libraries Used:** pandas, sklearn.svm, sklearn.model_selection, sklearn.metrics

## 4. lab6e.py - Performance Evaluation of Malware Detection

- **Functionality:** Evaluates the performance of a malware detection system by analyzing log files and comparing predictions against true labels.
- **Libraries Used:** pandas, numpy, json, sklearn, matplotlib

*Note: Each script contributes to the overall objective of understanding and detecting malware. For detailed usage and code explanations, refer to comments within each script.*
