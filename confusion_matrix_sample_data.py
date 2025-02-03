from sklearn.metrics import confusion_matrix, classification_report
import pandas as pd

# Sample dataset (actual and predicted labels)
data = {
    'Actual': ['Cat', 'Dog', 'Cat', 'Cat', 'Dog', 'Dog', 'Cat', 'Dog', 'Dog', 'Cat'],
    'Predicted': ['Cat', 'Dog', 'Dog', 'Cat', 'Dog', 'Cat', 'Cat', 'Dog', 'Dog', 'Dog']
}

# Create a DataFrame
df = pd.DataFrame(data)

# Display the dataset
print("Dataset:")
print(df)

# Compute confusion matrix
cm = confusion_matrix(df['Actual'], df['Predicted'], labels=['Cat', 'Dog'])

# Display confusion matrix
print("\nConfusion Matrix:")
print(cm)

# Convert confusion matrix to DataFrame for better readability
cm_df = pd.DataFrame(cm, index=['Cat (Actual)', 'Dog (Actual)'], columns=['Cat (Predicted)', 'Dog (Predicted)'])
print("\nConfusion Matrix (Formatted):")
print(cm_df)

# Classification report
print("\nClassification Report:")
print(classification_report(df['Actual'], df['Predicted']))
