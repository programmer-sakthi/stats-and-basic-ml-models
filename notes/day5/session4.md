# Test - Train Split

Train set: The training dataset is a set of data that was utilized to fit the model. The dataset on which the model is trained. This data is seen and learned by the model.

Test set: The test dataset is a subset of the training dataset that is utilized to give an accurate evaluation of a final model fit.

validation set: A validation dataset is a sample of data from your model's training set that is used to estimate model performance while tuning the model's hyperparameters.

## sklearn train_test_split

Syntax: sklearn.model_selection.train_test_split()

parameters:

arrays: sequence of indexables. Lists, numpy arrays, scipy-sparse matrices, and pandas dataframes are all valid inputs.
test_size: int or float, by default None. If float, it should be between 0.0 and 1.0 and represent the percentage of the dataset to test split. If int is used, it refers to the total number of test samples. If the value is None, the complement of the train size is used. It will be set to 0.25 if train size is also None.
train_size: int or float, by default None.
random_state : int,by default None. Controls how the data is shuffled before the split is implemented. For repeatable output across several function calls, pass an int.

shuffle: boolean object , by default True. Whether or not the data should be shuffled before splitting. Stratify must be None if shuffle=False.
stratify: array-like object , by default it is None. If None is selected, the data is stratified using these as class labels.

returns: splitting: list

## Python code using sklearn to perform train-test split

```python
from sklearn.model_selection import train_test_split

# Sample data
X = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]]
y = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

```
