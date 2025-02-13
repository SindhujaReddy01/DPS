# """This module contains necessary function needed"""

# # Import necessary modules
# import numpy as np
# import pandas as pd
# from sklearn.tree import DecisionTreeClassifier
# import streamlit as st



# def load_data():
#     """This function returns the preprocessed data"""

#     # Load the Diabetes dataset into DataFrame.
#     df = pd.read_csv('diabetes.csv')

#     # Perform feature and target split
#     X = df[["Pregnancies","FastingGlc","AfterGlc","BloodPressure","SkinThickness","Insulin", "BMI", "GeneticCorr", "Age"]]
#     y = df['Outcome']

#     return df, X, y


# def train_model(X, y):
#     """This function trains the model and return the model and model score"""
#     # Create the model
#     model = DecisionTreeClassifier(
#             ccp_alpha=0.0, class_weight=None, criterion='entropy',
#             max_depth=4, max_features=None, max_leaf_nodes=None,
#             min_impurity_decrease=0.0, min_samples_leaf=1, 
#             min_samples_split=2, min_weight_fraction_leaf=0.0,
#             random_state=42, splitter='best'
#         )
#     # Fit the data on model
#     model.fit(X, y)
#     # Get the model score
#     score = model.score(X, y)

#     # Return the values
#     return model, score

# def predict(X, y, features):
#     # Get model and model score
#     model, score = train_model(X, y)
#     # Predict the value
#     prediction = model.predict(np.array(features).reshape(1, -1))

#     return prediction, score

#SVM
# """This module contains necessary function needed"""

# # Import necessary modules
# import numpy as np
# import pandas as pd
# from sklearn.svm import SVC
# import streamlit as st

# def load_data():
#     """This function returns the preprocessed data"""
#     # Load the Diabetes dataset into DataFrame.
#     df = pd.read_csv('diabetes.csv')

#     # Perform feature and target split
#     X = df[["Pregnancies","FastingGlc","AfterGlc","BloodPressure","SkinThickness","Insulin", "BMI", "GeneticCorr", "Age"]]
#     y = df['Outcome']

#     return df, X, y

# def train_model(X, y):
#     """This function trains the SVM model and returns the model and model score"""
#     # Create the SVM model
#     model = SVC(kernel='rbf', C=1.0, gamma='scale', random_state=42)
    
#     # Fit the data to the model
#     model.fit(X, y)
    
#     # Get the model score
#     score = model.score(X, y)

#     # Return the trained model and its score
#     return model, score

# def predict(X, y, features):
#     # Get the trained model and model score
#     model, score = train_model(X, y)
    
#     # Predict the value
#     prediction = model.predict(np.array(features).reshape(1, -1))

#     return prediction, score

# # Example usage:
# if __name__ == "__main__":
#     # Load data
#     df, X, y = load_data()

#     # Get user input for features
#     features = [float(x) for x in input("Enter features separated by space: ").split()]

#     # Predict
#     prediction, score = predict(X, y, features)
#     print("Prediction:", prediction)
#     print("Model Score:", score)

#LR
# """This module contains necessary function needed"""

# # Import necessary modules
# import numpy as np
# import pandas as pd
# from sklearn.linear_model import LogisticRegression
# import streamlit as st

# def load_data():
#     """This function returns the preprocessed data"""
#     # Load the Diabetes dataset into DataFrame.
#     df = pd.read_csv('diabetes.csv')

#     # Perform feature and target split
#     X = df[["Pregnancies","FastingGlc","AfterGlc","BloodPressure","SkinThickness","Insulin", "BMI", "GeneticCorr", "Age"]]
#     y = df['Outcome']

#     return df, X, y

# def train_model(X, y):
#     """This function trains the Logistic Regression model and returns the model and model score"""
#     # Create the Logistic Regression model
#     model = LogisticRegression(random_state=42)
    
#     # Fit the data to the model
#     model.fit(X, y)
    
#     # Get the model score
#     score = model.score(X, y)

#     # Return the trained model and its score
#     return model, score

# def predict(X, y, features):
#     # Get the trained model and model score
#     model, score = train_model(X, y)
    
#     # Predict the value
#     prediction = model.predict(np.array(features).reshape(1, -1))

#     return prediction, score

# # Example usage:
# if __name__ == "__main__":
#     # Load data
#     df, X, y = load_data()

#     # Get user input for features
#     features = [float(x) for x in input("Enter features separated by space: ").split()]

#     # Predict
#     prediction, score = predict(X, y, features)
#     print("Prediction:", prediction)
#     print("Model Score:", score)

#Gaussian NB
# """This module contains necessary function needed"""

# # Import necessary modules
# import numpy as np
# import pandas as pd
# from sklearn.naive_bayes import GaussianNB
# import streamlit as st

# def load_data():
#     """This function returns the preprocessed data"""
#     # Load the Diabetes dataset into DataFrame.
#     df = pd.read_csv('diabetes.csv')

#     # Perform feature and target split
#     X = df[["Pregnancies","FastingGlc","AfterGlc","BloodPressure","SkinThickness","Insulin", "BMI", "GeneticCorr", "Age"]]
#     y = df['Outcome']

#     return df, X, y

# def train_model(X, y):
#     """This function trains the Naive Bayes model and returns the model and model score"""
#     # Create the Naive Bayes model
#     model = GaussianNB()
    
#     # Fit the data to the model
#     model.fit(X, y)
    
#     # Get the model score
#     score = model.score(X, y)

#     # Return the trained model and its score
#     return model, score

# def predict(X, y, features):
#     # Get the trained model and model score
#     model, score = train_model(X, y)
    
#     # Predict the value
#     prediction = model.predict(np.array(features).reshape(1, -1))

#     return prediction, score

# # Example usage:
# if __name__ == "__main__":
#     # Load data
#     df, X, y = load_data()

#     # Get user input for features
#     features = [float(x) for x in input("Enter features separated by space: ").split()]

#     # Predict
#     prediction, score = predict(X, y, features)
#     print("Prediction:", prediction)
#     print("Model Score:", score)

#Logestic Regtression
# """This module contains necessary function needed"""

# # Import necessary modules
# import numpy as np
# import pandas as pd
# from sklearn.linear_model import LogisticRegression
# import streamlit as st

# def load_data():
#     """This function returns the preprocessed data"""
#     # Load the Diabetes dataset into DataFrame.
#     df = pd.read_csv('diabetes.csv')

#     # Perform feature and target split
#     X = df[["Pregnancies","FastingGlc","AfterGlc","BloodPressure","SkinThickness","Insulin", "BMI", "GeneticCorr", "Age"]]
#     y = df['Outcome']

#     return df, X, y

# def train_model(X, y):
#     """This function trains the Logistic Regression model and returns the model and model score"""
#     # Create the Logistic Regression model
#     model = LogisticRegression(random_state=42)
    
#     # Fit the data to the model
#     model.fit(X, y)
    
#     # Get the model score
#     score = model.score(X, y)

#     # Return the trained model and its score
#     return model, score

# def predict(X, y, features):
#     # Get the trained model and model score
#     model, score = train_model(X, y)
    
#     # Predict the value
#     prediction = model.predict(np.array(features).reshape(1, -1))

#     return prediction, score

# # Example usage:
# if __name__ == "__main__":
#     # Load data
#     df, X, y = load_data()

#     # Get user input for features
#     features = [float(x) for x in input("Enter features separated by space: ").split()]

#     # Predict
#     prediction, score = predict(X, y, features)
#     print("Prediction:", prediction)
#     print("Model Score:", score)

"""This module contains necessary function needed"""

# Import necessary modules
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import streamlit as st

def load_data():
    """This function returns the preprocessed data"""
    # Load the Diabetes dataset into DataFrame.
    df = pd.read_csv('diabetes.csv')

    # Perform feature and target split
    X = df[["Pregnancies","FastingGlc","AfterGlc","BloodPressure","SkinThickness","Insulin", "BMI", "GeneticCorr", "Age"]]
    y = df['Outcome']

    return df, X, y

def train_model(X, y):
    """This function trains the Random Forest model and returns the model and model score"""
    # Create the Random Forest model
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    
    # Fit the data to the model
    model.fit(X, y)
    
    # Get the model score
    score = model.score(X, y)

    # Return the trained model and its score
    return model, score

def predict(X, y, features):
    # Get the trained model and model score
    model, score = train_model(X, y)
    
    # Predict the value
    prediction = model.predict(np.array(features).reshape(1, -1))

    return prediction, score

# Example usage:
if __name__ == "__main__":
    # Load data
    df, X, y = load_data()

    # Get user input for features
    features = [float(x) for x in input("Enter features separated by space: ").split()]

    # Predict
    prediction, score = predict(X, y, features)
    print("Prediction:", prediction)
    print("Model Score:", score)


