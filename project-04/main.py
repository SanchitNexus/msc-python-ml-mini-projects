"""Illustrate simple bag-of-words SMS spam filtering."""
from pathlib import Path
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report, confusion_matrix

def main():
    messages = pd.read_csv(Path(__file__).parent / "data" / "messages.csv")
    x_train, x_test, y_train, y_test = train_test_split(
        messages["message"], messages["label"], test_size=0.3,
        stratify=messages["label"], random_state=42
    )
    model = make_pipeline(CountVectorizer(), MultinomialNB())
    model.fit(x_train, y_train)
    predictions = model.predict(x_test)
    print(classification_report(y_test, predictions, zero_division=0))
    print("Confusion matrix [ham, spam]:")
    print(confusion_matrix(y_test, predictions, labels=["ham", "spam"]))
    print("Demo prediction:", model.predict(["Claim your free prize now"])[0])

if __name__ == "__main__":
    main()
