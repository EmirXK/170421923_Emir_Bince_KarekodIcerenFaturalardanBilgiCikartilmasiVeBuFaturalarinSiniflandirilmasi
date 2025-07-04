from module import models
from module import datasets
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.preprocessing import LabelEncoder

cv: CountVectorizer
le: LabelEncoder

cv = models.load_model("models/vectorizer.pkl")
le = models.load_model("models/labelencoder.pkl")

model = models.load_model("models/lr_full.pkl")

print("Model loaded successfully")
while True:
    string = input("Input: ")
    string = cv.transform([string])
    nnz = string.nnz
    prediction = model.predict(string)
    class_name = le.inverse_transform(prediction)[0]
    # If no words in bag, the class in Unknown
    if nnz == 0:
        class_name = "Unknown"
    print(f"Predicted class: {class_name}")