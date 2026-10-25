"""Classify three wine cultivars using lab-measured chemistry."""
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

def main():
    wine = load_wine()
    x_train, x_test, y_train, y_test = train_test_split(
        wine.data, wine.target, test_size=0.25, stratify=wine.target, random_state=42
    )
    model = make_pipeline(StandardScaler(), KNeighborsClassifier(n_neighbors=5))
    model.fit(x_train, y_train)
    predicted = model.predict(x_test)
    print("Test accuracy:", round(accuracy_score(y_test, predicted), 3))
    print("Confusion matrix (rows actual, columns predicted):")
    print(confusion_matrix(y_test, predicted))
    print("Attributes:", len(wine.feature_names), "| Samples:", len(wine.data))

if __name__ == "__main__":
    main()
