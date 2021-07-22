import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as pyplot
from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import cv2


X = np.load('G:\Whitehat Junior\Python WhiteHat Files\Whitehat jr Projects\Whitehat Jr Projects\image.npz')['arr_0']
y = pd.read_csv('G:\Whitehat Junior\Python WhiteHat Files\Whitehat jr Projects\Whitehat Jr Projects\labels.csv')["labels"]
print(pd.Series(y).value_counts())

classes = ['A', 'B', 'C', 'D', 'D','E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
nLabels = len(classes)

sampelsPerClass = 5

figure = pyplot.figure(figsize=(nLabels * 2, ((1 + sampelsPerClass) * 2)))

col = 0
for i in classes:
    cols = np.flatnonzero(y == i)
    cols = np.random.choice(cols,sampelsPerClass,replace = False)
    row = 0
    for j in cols:
        pos = row * nLabels + col + 1
        p = pyplot.subplot(sampelsPerClass, nLabels, pos)
        p = sns.heatmap(np.reshape(X[j], (22, 30)), 
        cmap = pyplot.cm.gray, xticklabels = False, 
        yticklabels = False, cbar = False)

        p = pyplot.axis('off')

        row = row + 1
    col = col +1

xTrain, xTest , yTrain, yTest = train_test_split(X, y, test_size=2500 , train_size=7500,random_state=0)
xTrainScaled = xTrain / 255
xTestScaled = xTest / 255

lr = LogisticRegression(solver='saga', multi_class='multinomial').fit(xTrainScaled, yTrain)

yPred = lr.predict(xTestScaled)
accuracy = accuracy_score(yTest, yPred)
print(f"The acccuracy of the model is {accuracy}")

cm = pd.crosstab(yTest, yPred, rownames=['Actual'],colnames= ['Predict'])
p = pyplot.figure(figsize = (10,10))
p = sns.heatmap( cm, annot = True, cbar=False, fmt='d')
