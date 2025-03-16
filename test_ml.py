import pytest
from sklearn.model_selection import train_test_split
import pandas as pd
import os

@pytest.fixture(scope="session")
def data():
    project_path = os.getcwd()
    data_path = os.path.join(project_path, "data", "census.csv")
    df = pd.read_csv(data_path)
    return df

def test_one(data):
    """
    Test that the train and test sets are segmented into correct proportions.
    """
    train, test = train_test_split(data, test_size=0.2, random_state=12)
    
    # Calculate expected sizes
    total_rows = len(data)
    expected_test_size = int(total_rows * 0.2)
    expected_train_size = total_rows - expected_test_size

    # Assert correct sizes
    assert len(train) == expected_train_size, f"Train size is {len(train)}, expected {expected_train_size}."
    assert len(test) == expected_test_size, f"Test size is {len(test)}, expected {expected_test_size}."

def test_two(data):
    """
    Test that the split returns pd.DataFrame data type.
    """
    train, test = train_test_split(data, test_size=0.2, random_state=12)
    
    # Assert types
    assert isinstance(train, data), "Train set is not a DataFrame."
    assert isinstance(test, data), "Test set is not a DataFrame."

def test_three(data):
    """
    Test that data has the proper number of columns.
    """
    # Assert the number of columns
    assert data.shape[1] == 15, f"Expected 15 columns, but got {data.shape[1]}."
