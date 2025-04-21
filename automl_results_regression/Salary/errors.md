## Error for 1_DecisionTree_GoldenFeatures

Golden Features not created. Empty scores.
Traceback (most recent call last):
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\base_automl.py", line 1183, in _fit
    trained = self.train_model(params)
              ^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\base_automl.py", line 388, in train_model
    mf.train(results_path, model_subpath)
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\model_framework.py", line 192, in train
    ].fit_and_transform(
      ^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\preprocessing\preprocessing.py", line 189, in fit_and_transform
    self._golden_features.fit(X_train[numeric_cols], y_train)
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\preprocessing\goldenfeatures_transformer.py", line 172, in fit
    raise AutoMLException("Golden Features not created. Empty scores.")
supervised.exceptions.AutoMLException: Golden Features not created. Empty scores.


Please set a GitHub issue with above error message at: https://github.com/mljar/mljar-supervised/issues/new

## Error for 4_Linear_GoldenFeatures

Golden Features not created due to error (please check errors.md). Golden Features not created. Empty scores. Input data shape: (27, 1), (27,)
Traceback (most recent call last):
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\base_automl.py", line 1183, in _fit
    trained = self.train_model(params)
              ^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\base_automl.py", line 388, in train_model
    mf.train(results_path, model_subpath)
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\model_framework.py", line 192, in train
    ].fit_and_transform(
      ^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\preprocessing\preprocessing.py", line 189, in fit_and_transform
    self._golden_features.fit(X_train[numeric_cols], y_train)
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\preprocessing\goldenfeatures_transformer.py", line 137, in fit
    raise AutoMLException(
supervised.exceptions.AutoMLException: Golden Features not created due to error (please check errors.md). Golden Features not created. Empty scores. Input data shape: (27, 1), (27,)


Please set a GitHub issue with above error message at: https://github.com/mljar/mljar-supervised/issues/new

## Error for 54_NeuralNetwork_GoldenFeatures

Golden Features not created due to error (please check errors.md). Golden Features not created. Empty scores. Input data shape: (27, 1), (27,)
Traceback (most recent call last):
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\base_automl.py", line 1183, in _fit
    trained = self.train_model(params)
              ^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\base_automl.py", line 388, in train_model
    mf.train(results_path, model_subpath)
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\model_framework.py", line 192, in train
    ].fit_and_transform(
      ^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\preprocessing\preprocessing.py", line 189, in fit_and_transform
    self._golden_features.fit(X_train[numeric_cols], y_train)
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\preprocessing\goldenfeatures_transformer.py", line 137, in fit
    raise AutoMLException(
supervised.exceptions.AutoMLException: Golden Features not created due to error (please check errors.md). Golden Features not created. Empty scores. Input data shape: (27, 1), (27,)


Please set a GitHub issue with above error message at: https://github.com/mljar/mljar-supervised/issues/new

