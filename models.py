import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
import joblib

def train_model(csv_path="data/combined_emails_with_natural_pii.csv"):
    print("Read The csv file")

    df = pd.read_csv(csv_path)
    
    df.head()
    
    X_train, _, y_train, _ = train_test_split(
        df["email"], df["type"], test_size=0.2, random_state=42
    )
    
    model = Pipeline([
        ("tfidf", TfidfVectorizer()),
        ("clf", MultinomialNB())
    ])
    
    model.fit(X_train, y_train)
    joblib.dump(model, "email_classification_system.pkl")
    return model
