import joblib
from datetime import datetime

def get_prediction(text_input):
    cv = joblib.load("model/Vectorizer.pkl")
    model = joblib.load("model/SVM_Cyberbullying_model.pkl")
    
    inputan = cv.transform([text_input])
    result = model.predict(inputan)
    
    if result[0] == "Bullying":
        return True
    else:
        return False
    

    