import pytest
# TODO: add necessary import
from sklearn.model_selection import train_test_split
import pandas as pd

@pytest.fixture(scope="session")
def data():
    project_path = os.getcwd()
    data_path = os.path.join(project_path, "data", "census.csv")
    df = pd.read_csv(data_path)
    return df

# TODO: implement the first test. Change the function name and input as needed
def test_one():
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
    


# TODO: implement the second test. Change the function name and input as needed
def test_two():
    """
    Test that the split returns pd.DataFrame data type.
    """
    train, test = train_test_split(data, test_size=0.2, random_state=12)
    
    # Assert types
    assert isinstance(train, pd.DataFrame), "Train set is not a DataFrame."
    assert isinstance(test, pd.DataFrame), "Test set is not a DataFrame."


# TODO: implement the third test. Change the function name and input as needed
def test_three():
    """
    tests that data has proper number of columns
    """
    # Your code here
    assert data.shape[1] == 15, f"Expected 15 columns, but got {data.shape[1]}"
