import pytest
from sklearn.tree import DecisionTreeClassifier
from ml.model import train_model
import numpy as np 

def test_model_type():
    """
    Tests whether train_model returns expected type 
    """
    X_train = [[1, 2], [3, 4]]
    y_train = [0, 1]
    model = train_model(X_train, y_train)
    assert model is not None, "Model is none"
    assert isinstance(model, DecisionTreeClassifier), "Model is not decision tree classifier"

def test_prediction_consistency():
    """
    Test if model's predicitions are conisstent using the same data and random state
    """
    X_train = [[1, 2], [3, 4], [5, 6]]
    y_train = [0, 1, 1]

    model_a = DecisionTreeClassifier(random_state=42)
    model_b = DecisionTreeClassifier(random_state=42)

    model_a.fit(X_train, y_train)
    model_b.fit(X_train, y_train)

    train_model(X_train, y_train)
    train_model(X_train, y_train)

    predictions_a = model_a.predict(X_train)
    predictions_b = model_b.predict(X_train)

    assert np.array_equal(predictions_a, predictions_b), "Predictions inconsistent"

def test_model_performance():
    """
    Tests to ensure that model performs above level of random guessing
    """
    X_train = [[1, 2], [3, 4]]
    y_train = [0, 1]
    model = train_model(X_train, y_train)

    accuracy = model.score(X_train, y_train)

    assert accuracy > 0.5, f"Model accuracy: '{accuracy}' is too low"
