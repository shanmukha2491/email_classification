import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
import joblib


def extract_subject_and_body(email_text):
    lines = email_text.strip().split('\n')
    subject = ""
    body = ""
    for line in lines:
        if line.lower().startswith("subject:"):
            subject = line.replace("Subject:", "").strip()
        else:
            body += line + " "
    return subject.strip(), body.strip()



def train_model(csv_path="data/combined_emails_with_natural_pii.csv"):
    df = pd.read_csv(csv_path)
    df.dropna(subset=["email", "type"], inplace=True)

    df[["subject", "body"]] = df["email"].apply(
        lambda x: pd.Series(extract_subject_and_body(x))
    )
    df["combined"] = df["subject"] + " " + df["body"]

    X_train, X_test, y_train, y_test = train_test_split(
        df["combined"], df["type"], test_size=0.2, random_state=42
    )

    model = Pipeline([
        ("tfidf", TfidfVectorizer()),
        ("clf", MultinomialNB())
    ])
    
    model.fit(X_train, y_train)
    joblib.dump(model, "email_classification_system.pkl")
    return model

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
