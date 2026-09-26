## Data Collection

import pandas as pd
df = pd.read_csv("dataset_traffic_accident_prediction1.csv")

## Data Understanding

print(df.head())
print(df.columns)
print(df.dtypes)
print(df.shape)
df.info()
print(df.describe())

## Data Cleaning

# 1. Check Missing Values
print("Missing Values : ",df.isnull().sum())

missing_values_in_each_row = df.isnull().sum(axis=1)
print(missing_values_in_each_row.value_counts())

# Target => missing values row remove
df  = df.dropna(subset=['Accident_Severity'])

print(df.isnull().sum())

# Numerical columns Missing values Fill
print("Unique : " ,df.select_dtypes(include='number').nunique())

df['Traffic_Density'] = df['Traffic_Density'].fillna(df['Traffic_Density'].mean())
print("Traffic_Density :" ,df['Traffic_Density'].isnull().sum())

df['Speed_Limit'] = df['Speed_Limit'].fillna(df['Speed_Limit'].median())
print("Speed_Limit :" ,df['Speed_Limit'].isnull().sum())

df['Number_of_Vehicles'] = df['Number_of_Vehicles'].fillna(df['Number_of_Vehicles'].median())
print("Number_of_Vehicles :" ,df['Number_of_Vehicles'].isnull().sum())

df['Driver_Alcohol'] = df['Driver_Alcohol'].fillna(df['Driver_Alcohol'].mode()[0])
print("Driver_Alcohol :" ,df['Driver_Alcohol'].isnull().sum())

df['Driver_Age'] = df['Driver_Age'].fillna(df['Driver_Age'].mean())
print("Driver_Age :" ,df['Driver_Age'].isnull().sum())

df['Driver_Experience'] = df['Driver_Experience'].fillna(df['Driver_Experience'].median())
print("Driver_Experience :" ,df['Driver_Experience'].isnull().sum())

df['Accident'] = df['Accident'].fillna(df['Accident'].mode()[0])
print("Accident :" ,df['Accident'].isnull().sum())

# Categorical Columns Missing Values Fill

df['Weather'] = df['Weather'].fillna(df['Weather'].mode()[0])
print("Weather :" ,df['Weather'].isnull().sum())

df['Road_Type'] = df['Road_Type'].fillna(df['Road_Type'].mode()[0])
print("Road_Type :" ,df['Road_Type'].isnull().sum())

df['Time_of_Day'] = df['Time_of_Day'].fillna(df['Time_of_Day'].mode()[0])
print("Time_of_Day :" ,df['Time_of_Day'].isnull().sum())

df['Road_Condition'] = df['Road_Condition'].fillna(df['Road_Condition'].mode()[0])
print("Road_Condition :" ,df['Road_Condition'].isnull().sum())

df['Vehicle_Type'] = df['Vehicle_Type'].fillna(df['Vehicle_Type'].mode()[0])
print("Vehicle_Type :" ,df['Vehicle_Type'].isnull().sum())

df['Road_Light_Condition'] = df['Road_Light_Condition'].fillna(df['Road_Light_Condition'].mode()[0])
print("Road_Light_Condition :" ,df['Road_Light_Condition'].isnull().sum())


# 2. Check Duplicates Rows
print("Duplicate Values : ",df.duplicated().sum())
df = df.drop_duplicates()
print("Duplicate Values : ",df.duplicated().sum())

# 3.Check Numerical Columns
num_cols = df.select_dtypes(include='number').columns
print("Numerical Columns :" ,num_cols)

# 4. Outliers

# 1. Traffic_Density Column
Q1 = df['Traffic_Density'].quantile(0.25)
Q3 = df['Traffic_Density'].quantile(0.75)

IQR = Q3 - Q1

lower_limit = Q1 - 1.5 * IQR
upper_limit = Q3 + 1.5 * IQR

outliers = ((df['Traffic_Density'] < lower_limit) | (df['Traffic_Density'] > upper_limit))
print("Traffic_Density Column Outliers :" ,outliers.sum())

# 2. Speed_Limit Column
Q1 = df['Speed_Limit'].quantile(0.25)
Q3 = df['Speed_Limit'].quantile(0.75)

IQR = Q3 - Q1

lower_limit = Q1 - 1.5 * IQR
upper_limit = Q3 + 1.5 * IQR

outliers = ((df['Speed_Limit'] < lower_limit) | (df['Speed_Limit'] > upper_limit))
print("Speed_Limit Column Outliers :" ,outliers.sum())
print("Values :" , df.loc[outliers,'Speed_Limit'].to_list())

# 3. Number_of_Vehicles
Q1 = df['Number_of_Vehicles'].quantile(0.25)
Q3 = df['Number_of_Vehicles'].quantile(0.75)

IQR = Q3 - Q1

lower_limit = Q1 - 1.5 * IQR
upper_limit = Q3 + 1.5 * IQR

outliers = ((df['Number_of_Vehicles'] < lower_limit) | (df['Number_of_Vehicles'] > upper_limit))
print("Number_of_Vehicles Outliers :" ,outliers.sum())
print("Values :" , df.loc[outliers,'Number_of_Vehicles'].to_list())

# 4. Driver_Age Column
Q1 = df['Driver_Age'].quantile(0.25)
Q3 = df['Driver_Age'].quantile(0.75)

IQR = Q3 - Q1

lower_limit = Q1 - 1.5 * IQR
upper_limit = Q3 + 1.5 * IQR

outliers = ((df['Driver_Age'] < lower_limit) | (df['Driver_Age'] > upper_limit))
print("Driver_Age Column Outliers :" ,outliers.sum())

# 5. Driver_Experience Column
Q1 = df['Driver_Experience'].quantile(0.25)
Q3 = df['Driver_Experience'].quantile(0.75)

IQR = Q3 - Q1

lower_limit = Q1 - 1.5 * IQR
upper_limit = Q3 + 1.5 * IQR

outliers = ((df['Driver_Experience'] < lower_limit) | (df['Driver_Experience'] > upper_limit))
print("Driver_Experience Column Outliers :" ,outliers.sum())


#  Check Invalid/Incorrect Values

# Numerical Features

# 1. Traffic_Density Column
print("Traffic_Density Minimum : ", df["Traffic_Density"].min())
print("Traffic_Density Maximum : ", df["Traffic_Density"].max())

# 2. Speed_Limit Column
print("Speed_Limit Minimum : ", df["Speed_Limit"].min())
print("Speed_Limit Maximum : ", df["Speed_Limit"].max())

# 3. Number_of_Vehicles Column
print("Number_of_Vehicles Minimum : ", df["Number_of_Vehicles"].min())
print("Number_of_Vehicles Maximum : ", df["Number_of_Vehicles"].max())

# 4. Driver_Alcohol Column
print("Driver_Alcohol Minimum : ", df["Driver_Alcohol"].min())
print("Driver_Alcohol Maximum : ", df["Driver_Alcohol"].max())

# 5. Driver_Age Column
print("Driver_Age Minimum : ", df["Driver_Age"].min())
print("Driver_Age Maximum : ", df["Driver_Age"].max())

# 6. Driver_Experience Column
print("Driver_Experience Minimum : ", df["Driver_Experience"].min())
print("Driver_Experience Maximum : ", df["Driver_Experience"].max())

# 7. Accident Column
print("Accident Minimum : ", df["Accident"].min())
print("Accident Maximum : ", df["Accident"].max())

# Categorical Features

cat_cols = df.select_dtypes(include='object').columns
print("Categorical Columns :" ,cat_cols)

print("Value Count :" ,df['Weather'].value_counts())
print("Value Count :" ,df['Road_Type'].value_counts())
print("Value Count :" ,df['Time_of_Day'].value_counts())
print("Value Count :" ,df['Road_Condition'].value_counts())
print("Value Count :" ,df['Vehicle_Type'].value_counts())
print("Value Count :" ,df['Road_Light_Condition'].value_counts())

# Check Target Column
print("Unique Value :" ,df['Accident_Severity'].unique())
print("Value Count :" ,df['Accident_Severity'].value_counts())


## EDA
import matplotlib.pyplot as plt

# 1. Univariate Analysis
# Distribution Of Numerical Feature

print("1. Traffic_Density Graph")
plt.hist(df["Traffic_Density"])
plt.title("Distribution Of Traffic Density")
plt.xlabel("Traffic Density")
plt.ylabel("Count")
plt.show()


print("2. Speed_Limit Graph")
plt.boxplot(df["Speed_Limit"])
plt.title("Distribution Of Speed Limit")
plt.xlabel("Speed Limit")
plt.ylabel("Count")
plt.show()


print("3. Number_of_Vehicles Graph")
plt.boxplot(df["Number_of_Vehicles"])
plt.title("Distribution Of Number Of Vehicles")
plt.xlabel("Number Of Vehicles")
plt.ylabel("Count")
plt.show()


print("4. Driver_Alcohol Graph")
plt.hist(df["Driver_Alcohol"])
plt.title("Distribution Of Driver Alcohol")
plt.xlabel("Driver Alcohol")
plt.ylabel("Count")
plt.show()


print("5. Driver_Age Graph")
plt.hist(df["Driver_Age"])
plt.title("Distribution Of Driver Age")
plt.xlabel("Driver Age")
plt.ylabel("Count")
plt.show()

print("6. Driver Experience Graph")
plt.hist(df["Driver_Experience"])
plt.title("Distribution Of Driver Experience")
plt.xlabel("Driver Experience")
plt.ylabel("Count")
plt.show()

print("7. Accident Graph")
plt.hist(df["Accident"])
plt.title("Distribution Of Accident")
plt.xlabel("Accident")
plt.ylabel("Count")
plt.show()


# Distribution Of Categorical Features

print("1. Weather Graph")
plt.bar(df["Weather"].value_counts().index , df["Weather"].value_counts().values)
plt.title("Distribution Of Weather")
plt.xlabel("Weather")
plt.ylabel("Count")
plt.show()

print("2. Road_Type Graph")
plt.bar(df["Road_Type"].value_counts().index , df["Road_Type"].value_counts().values)
plt.title("Distribution Of Road Type")
plt.xlabel("Road Type")
plt.ylabel("Count")
plt.show()


print("3. Time_of_Day Graph")
plt.bar(df["Time_of_Day"].value_counts().index , df["Time_of_Day"].value_counts().values)
plt.title("Distribution Of Time Of Day")
plt.xlabel("Time Of Day")
plt.ylabel("Count")
plt.show()


print("4. Accident Severity Graph")
plt.bar(df["Accident_Severity"].value_counts().index , df["Accident_Severity"].value_counts().values)
plt.title("Distribution Of Accident Severity")
plt.xlabel("Accident Severity")
plt.ylabel("Count")
plt.show()

print("5. Road Condition Graph")
plt.bar(df["Road_Condition"].value_counts().index , df["Road_Condition"].value_counts().values)
plt.title("Distribution Of Road Condition")
plt.xlabel("Road Condition")
plt.ylabel("Count")
plt.show()


print("6. Vehicle Type Graph")
plt.bar(df["Vehicle_Type"].value_counts().index , df["Vehicle_Type"].value_counts().values)
plt.title("Distribution Of Vehicle Type")
plt.xlabel("Vehicle_Type")
plt.ylabel("Count")
plt.show()


print("7. Road_Light_Condition Graph")
plt.bar(df["Road_Light_Condition"].value_counts().index , df["Road_Light_Condition"].value_counts().values)
plt.title("Distribution Of Road Light Condition")
plt.xlabel("Road Light Condition")
plt.ylabel("Count")
plt.show()



# Bivariate Analysis
import seaborn as sns

# Numerical Features VS Target

print("1. Traffic_Density VS Accident_Severity Graph")
sns.barplot(data=df ,x = "Traffic_Density", y = "Accident_Severity")
plt.title("Traffic Density VS Accident Severity Graph")
plt.xlabel("Traffic Density")
plt.ylabel("Accident Severity")
plt.show()


print("2. Speed Limit VS Accident_Severity Graph")
sns.boxplot(data=df ,x = "Speed_Limit", y = "Accident_Severity")
plt.title("Speed Limit VS Accident Severity Graph")
plt.xlabel("Speed Limit")
plt.ylabel("Accident Severity")
plt.show()

print("3. Number_of_Vehicles VS Accident_Severity Graph")
sns.boxplot(data=df ,x = "Number_of_Vehicles", y = "Accident_Severity")
plt.title("Number Of Vehicles VS Accident_Severity Graph")
plt.xlabel("Number Of Vehicles")
plt.ylabel("Accident Severity")
plt.show()


print("4. Driver_Alcohol VS Accident_Severity Graph")
sns.countplot(data=df ,x = "Driver_Alcohol", hue = "Accident_Severity")
plt.title("Driver Alcohol VS Accident Severity Graph")
plt.xlabel("Driver Alcohol")
plt.ylabel("Count")
plt.show()


print("5. Driver_Age VS Accident_Severity Graph")
sns.barplot(data=df ,x = "Driver_Age", y = "Accident_Severity")
plt.title("Driver Age VS Accident Severity Graph")
plt.xlabel("Driver Age")
plt.ylabel("Accident Severity")
plt.show()


print("6. Driver_Experience VS Accident_Severity Graph")
sns.barplot(data=df ,x = "Driver_Experience", y = "Accident_Severity")
plt.title("Driver Experience VS Accident Severity Graph")
plt.xlabel("Driver Experience")
plt.ylabel("Accident Severity")
plt.show()


print("7. Accident VS Accident_Severity Graph")
sns.countplot(data=df ,x = "Accident", hue = "Accident_Severity")
plt.title("Accident VS Accident Severity Graph")
plt.xlabel("Accident")
plt.ylabel("Count")
plt.show()


# Categorical Features VS Target

print("1. Weather VS Accident_Severity Graph")
sns.countplot(data=df ,x = "Weather", hue = "Accident_Severity")
plt.title("Weather VS Accident_Severity Graph")
plt.xlabel("Weather")
plt.ylabel("Count")
plt.show()


print("2. Road_Type VS Accident_Severity Graph")
sns.countplot(data=df ,x = "Road_Type", hue = "Accident_Severity")
plt.title("Road Type VS Accident_Severity Graph")
plt.xlabel("Road Type")
plt.ylabel("Count")
plt.show()

print("3. Time_of_Day VS Accident_Severity Graph")
sns.countplot(data=df ,x = "Time_of_Day", hue = "Accident_Severity")
plt.title("Time of Day VS Accident_Severity Graph")
plt.xlabel("Time of Day")
plt.ylabel("Count")
plt.show()


print("4. Road_Condition VS Accident_Severity Graph")
sns.countplot(data=df ,x = "Road_Condition", hue = "Accident_Severity")
plt.title("Road Condition VS Accident_Severity Graph")
plt.xlabel("Road Condition")
plt.ylabel("Count")
plt.show()


print("5. Vehicle_Type VS Accident_Severity Graph")
sns.countplot(data=df ,x = "Vehicle_Type", hue = "Accident_Severity")
plt.title("Vehicle Type VS Accident_Severity Graph")
plt.xlabel("Vehicle Type")
plt.ylabel("Count")
plt.show()


print("6. Road_Light_Condition VS Accident_Severity Graph")
sns.countplot(data=df ,x = "Road_Light_Condition", hue = "Accident_Severity")
plt.title("Road Light Condition VS Accident_Severity Graph")
plt.xlabel("Road Light Condition")
plt.ylabel("Count")
plt.show()

# Multivariate Analysis

# Correlation
print("Correlation : " ,df[num_cols].corr())

# Heatmap
sns.heatmap(df[num_cols].corr(), annot = True)
plt.show()


## Data Processing
# 1. Encoding

# One-Hot Encoding
one_hot = pd.get_dummies(df[["Weather","Road_Type","Time_of_Day","Road_Condition","Vehicle_Type","Road_Light_Condition"]])
print(one_hot)

final_encoding_df = one_hot 

X = pd.concat([df[num_cols],final_encoding_df],axis=1)
y = df['Accident_Severity']

# 2. Train_Test Split

from sklearn.model_selection import train_test_split

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42)

print(X_test.shape)
print(X_train.shape)
print(y_train.shape)
print(y_test.shape)

# 3. Feature Scaling

from sklearn.preprocessing import StandardScaler

scaler  = StandardScaler()

scaler.fit(X_train)
X_train_scaled = scaler.transform(X_train)

X_test_scaled = scaler.transform(X_test)

print(X_train_scaled.shape)
print(X_test_scaled.shape)

## Model Building

# Model 1. Logistic Regression Classification
print("1. Logistic Regression Classification")
from sklearn.linear_model import LogisticRegression

model = LogisticRegression()
model.fit(X_train_scaled,y_train)
y_pred = model.predict(X_test_scaled)
y_proba = model.predict_proba(X_test_scaled)

# Evaluation
from sklearn.metrics import confusion_matrix,accuracy_score,precision_score,recall_score,roc_curve,auc,f1_score,classification_report,roc_auc_score
from sklearn.preprocessing import label_binarize

# Confusion Matrix
lr_cm = confusion_matrix(y_test,y_pred)
print("Confusion Matrix :" ,lr_cm)

# Accuracy
lr_accuracy = accuracy_score(y_test,y_pred)
print("Accuracy :" ,lr_accuracy)

# Precision
lr_precision = precision_score(y_test,y_pred,average='weighted')
print("Precision :" ,lr_precision)

# Recall
lr_recall = recall_score(y_test,y_pred,average='weighted')
print("Recall :" ,lr_recall)

# F1 Score
lr_f1 = f1_score(y_test,y_pred,average='weighted')
print("F1 Score :" ,lr_f1)

# Classification Report
lr_cr = classification_report(y_test,y_pred)
print("Classification Report :" ,lr_cr)

# Roc Curve
classes = model.classes_
y_test_bin = label_binarize(y_test, classes=model.classes_)

for i in range(len(classes)):
    fpr,tpr,_ = roc_curve(y_test_bin[:,i],y_proba[:,i])

# AUC
lr_roc_auc = roc_auc_score(y_test,y_proba,multi_class = 'ovr',average='weighted')

# Plot Roc Curve
    plt.plot(fpr,tpr,label=f'{classes[i]} (AUC={lr_roc_auc:.2f})')

# Referance Line
plt.plot([0,1],[0,1],linestyle = '--')
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("Roc Curve")
plt.legend()
plt.show()


# Model 2. KNN Classification
print("2. KNN Classification")
from sklearn.neighbors import KNeighborsClassifier

model = KNeighborsClassifier()
model.fit(X_train_scaled,y_train)
y_pred = model.predict(X_test_scaled)
y_proba = model.predict_proba(X_test_scaled)

# Evaluation

# Confusion Matrix
knn_cm = confusion_matrix(y_test,y_pred)
print("Confusion Matrix :" ,knn_cm)

# Accuracy
knn_accuracy = accuracy_score(y_test,y_pred)
print("Accuracy :" ,knn_accuracy)

# Precision
knn_precision = precision_score(y_test,y_pred,average='weighted')
print("Precision :" ,knn_precision)

# Recall
knn_recall = recall_score(y_test,y_pred,average='weighted')
print("Recall :" ,knn_recall)

# F1 Score
knn_f1 = f1_score(y_test,y_pred,average='weighted')
print("F1 Score :" ,knn_f1)

# Classification Report
knn_cr = classification_report(y_test,y_pred)
print("Classification Report :" ,knn_cr)

# Roc Curve
classes = model.classes_
y_test_bin = label_binarize(y_test,classes=model.classes_)

for i in range(len(classes)):

    fpr , tpr, _ = roc_curve(y_test_bin[:,i],y_proba[:,i])

# AUC
knn_roc_auc = roc_auc_score(y_test,y_proba,multi_class = 'ovr',average='weighted')

# Plot Roc Curve
    plt.plot(fpr,tpr,label=f'{classes[i]}(AUC={knn_roc_auc:.2f})')

# Referance Line
plt.plot([0,1],[0,1],linestyle = '--')
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("Roc Curve")
plt.legend()
plt.show()


# Model 3. Decision Tree Classification
print("3. Decision Tree  Classification")
from sklearn.tree import DecisionTreeClassifier

model = DecisionTreeClassifier()
model.fit(X_train,y_train)
y_pred = model.predict(X_test)
y_proba = model.predict_proba(X_test)

# Evaluation

# Confusion Matrix
dt_cm = confusion_matrix(y_test,y_pred)
print("Confusion Matrix :" ,dt_cm)

# Accuracy
dt_accuracy = accuracy_score(y_test,y_pred)
print("Accuracy :" ,dt_accuracy)

# Precision
dt_precision = precision_score(y_test,y_pred,average='weighted')
print("Precision :" ,dt_precision)

# Recall
dt_recall = recall_score(y_test,y_pred,average='weighted')
print("Recall :" ,dt_recall)

# F1 Score
dt_f1 = f1_score(y_test,y_pred,average='weighted')
print("F1 Score :" ,dt_f1)

# Classification Report
dt_cr = classification_report(y_test,y_pred)
print("Classification Report :" ,dt_cr)

# Roc Curve
classes = model.classes_
y_test_bin = label_binarize(y_test,classes=model.classes_)

for i in range(len(classes)):

    fpr , tpr , _ = roc_curve(y_test_bin[:,i],y_proba[:,i])

# AUC
dt_roc_auc = roc_auc_score(y_test,y_proba,multi_class = 'ovr',average='weighted')

# Plot Roc Curve
    plt.plot(fpr,tpr,label=f'{classes[i]}(AUC={dt_roc_auc:.2f})')

# Referance Line
plt.plot([0,1],[0,1],linestyle = '--')
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("Roc Curve")
plt.legend()
plt.show()


# Model 4. Randon Forest Classification
print("4. Random Forest Classification")
from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier()
model.fit(X_train,y_train)
y_pred = model.predict(X_test)
y_proba = model.predict_proba(X_test)

# Evaluation

# Confusion Matrix
rf_cm = confusion_matrix(y_test,y_pred)
print("Confusion Matrix :" ,rf_cm)

# Accuracy
rf_accuracy = accuracy_score(y_test,y_pred)
print("Accuracy :" ,rf_accuracy)

# Precision
rf_precision = precision_score(y_test,y_pred,average='weighted')
print("Precision :" ,rf_precision)

# Recall
rf_recall = recall_score(y_test,y_pred,average='weighted')
print("Recall :" ,rf_recall)

# F1 Score
rf_f1 = f1_score(y_test,y_pred,average='weighted')
print("F1 Score :" ,rf_f1)

# Classification Report
rf_cr = classification_report(y_test,y_pred)
print("Classification Report :" ,rf_cr)

# Roc Curve
classes = model.classes_
y_test_bin = label_binarize(y_test,classes=model.classes_)

for i in range(len(classes)):

    fpr , tpr , _ = roc_curve(y_test_bin[:,i],y_proba[:,i])

# AUC
rf_roc_auc = roc_auc_score(y_test,y_proba,multi_class = 'ovr',average='weighted')

# Plot Roc Curve
    plt.plot(fpr,tpr,label=f'{classes[i]}(AUC={rf_roc_auc:.2f})')

# Referance Line
plt.plot([0,1],[0,1],linestyle = '--')
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("Roc Curve")
plt.legend()
plt.show()


# Model 5. SVM  Classification
print("5. SVM  Classification")
from sklearn.svm import SVC

model = SVC(probability=True)
model.fit(X_train_scaled,y_train)
y_pred = model.predict(X_test_scaled)
y_proba = model.predict_proba(X_test_scaled)

# Evaluation

# Confusion Matrix
svm_cm = confusion_matrix(y_test,y_pred)
print("Confusion Matrix :" ,svm_cm)

# Accuracy
svm_accuracy = accuracy_score(y_test,y_pred)
print("Accuracy :" ,svm_accuracy)

# Precision
svm_precision = precision_score(y_test,y_pred,average='weighted')
print("Precision :" ,svm_precision)

# Recall
svm_recall = recall_score(y_test,y_pred,average='weighted')
print("Recall :" ,svm_recall)

# F1 Score
svm_f1 = f1_score(y_test,y_pred,average='weighted')
print("F1 Score :" ,svm_f1)

# Classification Report
svm_cr = classification_report(y_test,y_pred)
print("Classification Report :" ,svm_cr)

# Roc Curve
classes = model.classes_
y_test_bin = label_binarize(y_test,classes=model.classes_)

for i in range(len(classes)):

    fpr , tpr , _ = roc_curve(y_test_bin[:,i],y_proba[:,i])

# AUC
svm_roc_auc = roc_auc_score(y_test,y_proba,multi_class = 'ovr',average='weighted')

# Plot Roc Curve
    plt.plot(fpr,tpr,label=f'{classes[i]}(AUC={svm_roc_auc:.2f})')

# Referance Line
plt.plot([0,1],[0,1],linestyle = '--')
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("Roc Curve")
plt.legend()
plt.show()

# Model 6. Naive Bayes Classification
print("6. Naive Bayes Classification")
from sklearn.naive_bayes import GaussianNB

model = GaussianNB()
model.fit(X_train,y_train)
y_pred = model.predict(X_test)
y_proba = model.predict_proba(X_test)

# Evaluation

# Confusion Matrix
nb_cm = confusion_matrix(y_test,y_pred)
print("Confusion Matrix :" ,nb_cm)

# Accuracy
nb_accuracy = accuracy_score(y_test,y_pred)
print("Accuracy :" ,nb_accuracy)

# Precision
nb_precision = precision_score(y_test,y_pred,average='weighted')
print("Precision :" ,nb_precision)

# Recall
nb_recall = recall_score(y_test,y_pred,average='weighted')
print("Recall :" ,nb_recall)

# F1 Score
nb_f1 = f1_score(y_test,y_pred,average='weighted')
print("F1 Score :" ,nb_f1)

# Classification Report
nb_cr = classification_report(y_test,y_pred)
print("Classification Report :" ,nb_cr)

# Roc Curve
classes = model.classes_
y_test_bin = label_binarize(y_test,classes=model.classes_)

for i in range(len(classes)):

    fpr , tpr , _= roc_curve(y_test_bin[:,i],y_proba[:,i])

# AUC
nb_roc_auc = roc_auc_score(y_test,y_proba,multi_class = 'ovr',average='weighted')

# Plot Roc Curve
    plt.plot(fpr,tpr,label=f'{classes[i]}(AUC={nb_roc_auc:.2f})')

# Referance Line
plt.plot([0,1],[0,1],linestyle = '--')
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("Roc Curve")
plt.legend()
plt.show()


## Model Comparison

comparison = pd.DataFrame({
    'Model' : [
        'Logistic Regression' ,
        'KNN' ,
        'Decision Tree' ,
        'Random Forest' ,
        'SVM' ,
        'Naive Bayes'
    ] ,
    'Accuracy' : [
        lr_accuracy,
        knn_accuracy,
        dt_accuracy,
        rf_accuracy,
        svm_accuracy,
        nb_accuracy
    ] ,

    'Precision' : [
        lr_precision,
        knn_precision,
        dt_precision,
        rf_precision,
        svm_precision,
        nb_precision
    ],
    'Recall' : [
        lr_recall,
        knn_recall,
        dt_recall,
        rf_recall,
        svm_recall,
        nb_recall
    ],
    'F1 Score' : [
        lr_f1,
        knn_f1,
        dt_f1,
        rf_f1,
        svm_f1,
        nb_f1
    ],
    'ROC-AUC' : [
        lr_roc_auc,
        knn_roc_auc,
        dt_roc_auc,
        rf_roc_auc,
        svm_roc_auc,
        nb_roc_auc
    ]
})
print("Comparison :" ,comparison)

## Check Target Leakage
print("Accident_Severity" in X)

## Final Model Selection
final_model = RandomForestClassifier(random_state=42)
final_model.fit(X,y)

## New/Unseen data
print(df.columns)
print(df.drop(columns='Accident_Severity').columns)

new_data = pd.DataFrame([{
    "Weather": "Clear",
    "Road_Type": "City Road",
    "Time_of_Day": "Morning",
    "Traffic_Density": 1,
    "Speed_Limit": 60,
    "Number_of_Vehicles": 2,
    "Driver_Alcohol": 0,
    "Road_Condition": "Dry",
    "Vehicle_Type": "Car",
    "Driver_Age": 30,
    "Driver_Experience": 8,
    "Road_Light_Condition": "Daylight",
    "Accident": 1
}])

## New data encoding
new_data_encoded = pd.get_dummies(new_data)
print(new_data_encoded)

new_data_encoded =new_data_encoded.reindex(columns=X.columns,fill_value=0)

## Final Model Prediction

prediction = final_model.predict(new_data_encoded)
print("Prediction :"  ,prediction)