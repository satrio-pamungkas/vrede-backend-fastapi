from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.svm import LinearSVC
import pandas as pd
import joblib

def get_prediction(text_input):
    data = pd.read_csv("dataset/dataset-cyberbullying.csv")
    data['Komentar'] = data['Komentar'].str.replace(r"[\"\',]", '')
    
    x = data['Komentar']
    y = data['Kategori']

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)
    
    cv = joblib.load("model/Vectorizer.pkl")
    model = joblib.load("model/SVM_Cyberbullying_model.pkl")
    
    inputan = cv.transform([text_input])
    result = model.predict(inputan)
    
    if result[0] == "Bullying":
        return True
    else:
        return False
    