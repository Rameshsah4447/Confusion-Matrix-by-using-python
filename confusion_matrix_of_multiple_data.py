# import dependencies
import numpy as np
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay, classification_report
import matplotlib.pyplot as plt

# Actual labels
y_true = ['Cat'] * 10 + ['Dog'] * 12 + ['Horse'] * 10
# Predicted labels
y_pred = ['Cat'] * 8 + ['Dog'] + ['Horse'] + ['Cat'] * 2 + ['Dog'] * 10 + ['Horse'] * 8 + ['Dog'] * 2
# Classes
classes = ['Cat', 'Dog', 'Horse']