import pandas as pd
from sklearn.tree import DecisionTreeClassifier # Import Decision Tree Classifier
from sklearn.model_selection import train_test_split # Import train_test_split function
from sklearn import metrics #Import scikit-learn metrics module for accuracy calculation
from Visualiser import Visualiser
import time


class Classifier:
    def __init__(self, col_names, filename, classes):
        self.classes = classes
        self.visualiser = Visualiser()
        
        self.col_names = col_names
        # load dataset
        self.dataset = pd.read_csv(filename, header=None, names=self.col_names)
        
        for c in self.col_names:
            labels = self.dataset[c].astype('category').cat.categories.tolist()
            replace_map = {c : {k: v for k,v in zip(labels,list(range(1,len(labels)+1)))}}
            self.dataset.replace(replace_map, inplace=True)
           
        self.feature_cols = self.col_names
        self.col = self.feature_cols.pop(len(self.col_names) - 1)
        print(self.feature_cols)
            
    def classify(self):
        start_time = time.time()
        #split dataset in features and target variable
        
        X = self.dataset[self.feature_cols] # Features
        y = self.dataset[self.col] # Target variable

        # Split dataset into training set and test set
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1) # 70% training and 30% test

        # Create Decision Tree classifer object
        clf = DecisionTreeClassifier()

        # Train Decision Tree Classifer
        clf = clf.fit(X_train,y_train)

        #Predict the response for test dataset
        y_pred = clf.predict(X_test)

     
  
        self.visualiser.visualise(clf, self.feature_cols, self.classes )
        print("Cars Classification Accuracy:",metrics.accuracy_score(y_test, y_pred))
        print("--- %s seconds execution time ---" % (time.time() - start_time))
        