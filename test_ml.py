
import pytest
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from train_model import train_model, cat_features
from ml.model import compute_model_metrics

# TODO: add necessary import

# TODO: implement the first test. Change the function name and input as needed
def test_train_model():
    """
    # Test that the train_model function returns a RandomForestClassifier.
    """
    X_train = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])
    y_train = np.array([0, 1, 0, 1])

    model = train_model(X_train, y_train)

    assert isinstance(model, RandomForestClassifier), f"Expected RandomForestClassifier, and got {type(model)}"



# TODO: implement the second test. Change the function name and input as needed
def test_compute_model_metrics():
    """
    Tests to see if compute model metrics returns the correct metrics.
    """
    y_true = np.array([0, 1, 1, 0, 1])
    y_pred = np.array([0, 1, 1, 0, 0])

    precision, recall, fbeta = compute_model_metrics(y_true, y_pred)

    assert len([precision, recall, fbeta]) == 3, f"Expected 3 metrics, and got {len([precision, recall, fbeta])}."



# TODO: implement the third test. Change the function name and input as needed
def test_cat_features():
    """
    # Testing to see if the cat features list has the correct features.
    """
    cat_features_from_dataset = [
        "workclass",
        "education",
        "marital-status",
        "occupation",
        "relationship",
        "race",
        "sex",
        "native-country",
    ]

    assert cat_features == cat_features_from_dataset, f"Expected {cat_features_from_dataset}, and got {cat_features}"