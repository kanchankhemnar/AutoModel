## Error for 1_DecisionTree

y_true and y_pred contain different number of classes 30, 2. Please provide the true labels explicitly through the labels argument. Classes found in y_true: [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
 24 25 26 27 28 29]
Traceback (most recent call last):
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\base_automl.py", line 1183, in _fit
    trained = self.train_model(params)
              ^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\base_automl.py", line 388, in train_model
    mf.train(results_path, model_subpath)
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\model_framework.py", line 265, in train
    self.callbacks.on_iteration_end(
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\callbacks\callback_list.py", line 23, in on_iteration_end
    cb.on_iteration_end(logs, predictions)
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\callbacks\early_stopping.py", line 96, in on_iteration_end
    train_loss = self.metric(
                 ^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\utils\metric.py", line 408, in __call__
    return self.metric(y_true, y_predicted, sample_weight=sample_weight)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\utils\metric.py", line 24, in logloss
    ll = log_loss(y_true, y_predicted.astype(np.float32), sample_weight=sample_weight)
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\utils\_param_validation.py", line 213, in wrapper
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\metrics\_classification.py", line 2968, in log_loss
    raise ValueError(
ValueError: y_true and y_pred contain different number of classes 30, 2. Please provide the true labels explicitly through the labels argument. Classes found in y_true: [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
 24 25 26 27 28 29]


Please set a GitHub issue with above error message at: https://github.com/mljar/mljar-supervised/issues/new

## Error for 1_DecisionTree

y_true and y_pred contain different number of classes 30, 2. Please provide the true labels explicitly through the labels argument. Classes found in y_true: [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
 24 25 26 27 28 29]
Traceback (most recent call last):
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\base_automl.py", line 1183, in _fit
    trained = self.train_model(params)
              ^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\base_automl.py", line 388, in train_model
    mf.train(results_path, model_subpath)
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\model_framework.py", line 265, in train
    self.callbacks.on_iteration_end(
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\callbacks\callback_list.py", line 23, in on_iteration_end
    cb.on_iteration_end(logs, predictions)
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\callbacks\early_stopping.py", line 96, in on_iteration_end
    train_loss = self.metric(
                 ^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\utils\metric.py", line 408, in __call__
    return self.metric(y_true, y_predicted, sample_weight=sample_weight)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\utils\metric.py", line 24, in logloss
    ll = log_loss(y_true, y_predicted.astype(np.float32), sample_weight=sample_weight)
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\utils\_param_validation.py", line 213, in wrapper
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\metrics\_classification.py", line 2968, in log_loss
    raise ValueError(
ValueError: y_true and y_pred contain different number of classes 30, 2. Please provide the true labels explicitly through the labels argument. Classes found in y_true: [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
 24 25 26 27 28 29]


Please set a GitHub issue with above error message at: https://github.com/mljar/mljar-supervised/issues/new

## Error for 2_DecisionTree

y_true and y_pred contain different number of classes 30, 2. Please provide the true labels explicitly through the labels argument. Classes found in y_true: [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
 24 25 26 27 28 29]
Traceback (most recent call last):
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\base_automl.py", line 1183, in _fit
    trained = self.train_model(params)
              ^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\base_automl.py", line 388, in train_model
    mf.train(results_path, model_subpath)
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\model_framework.py", line 265, in train
    self.callbacks.on_iteration_end(
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\callbacks\callback_list.py", line 23, in on_iteration_end
    cb.on_iteration_end(logs, predictions)
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\callbacks\early_stopping.py", line 96, in on_iteration_end
    train_loss = self.metric(
                 ^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\utils\metric.py", line 408, in __call__
    return self.metric(y_true, y_predicted, sample_weight=sample_weight)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\utils\metric.py", line 24, in logloss
    ll = log_loss(y_true, y_predicted.astype(np.float32), sample_weight=sample_weight)
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\utils\_param_validation.py", line 213, in wrapper
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\metrics\_classification.py", line 2968, in log_loss
    raise ValueError(
ValueError: y_true and y_pred contain different number of classes 30, 2. Please provide the true labels explicitly through the labels argument. Classes found in y_true: [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
 24 25 26 27 28 29]


Please set a GitHub issue with above error message at: https://github.com/mljar/mljar-supervised/issues/new

## Error for 3_DecisionTree

y_true and y_pred contain different number of classes 30, 2. Please provide the true labels explicitly through the labels argument. Classes found in y_true: [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
 24 25 26 27 28 29]
Traceback (most recent call last):
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\base_automl.py", line 1183, in _fit
    trained = self.train_model(params)
              ^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\base_automl.py", line 388, in train_model
    mf.train(results_path, model_subpath)
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\model_framework.py", line 265, in train
    self.callbacks.on_iteration_end(
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\callbacks\callback_list.py", line 23, in on_iteration_end
    cb.on_iteration_end(logs, predictions)
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\callbacks\early_stopping.py", line 96, in on_iteration_end
    train_loss = self.metric(
                 ^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\utils\metric.py", line 408, in __call__
    return self.metric(y_true, y_predicted, sample_weight=sample_weight)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\utils\metric.py", line 24, in logloss
    ll = log_loss(y_true, y_predicted.astype(np.float32), sample_weight=sample_weight)
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\utils\_param_validation.py", line 213, in wrapper
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\metrics\_classification.py", line 2968, in log_loss
    raise ValueError(
ValueError: y_true and y_pred contain different number of classes 30, 2. Please provide the true labels explicitly through the labels argument. Classes found in y_true: [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
 24 25 26 27 28 29]


Please set a GitHub issue with above error message at: https://github.com/mljar/mljar-supervised/issues/new

## Error for 4_Linear

y_true and y_pred contain different number of classes 30, 2. Please provide the true labels explicitly through the labels argument. Classes found in y_true: [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
 24 25 26 27 28 29]
Traceback (most recent call last):
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\base_automl.py", line 1183, in _fit
    trained = self.train_model(params)
              ^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\base_automl.py", line 388, in train_model
    mf.train(results_path, model_subpath)
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\model_framework.py", line 265, in train
    self.callbacks.on_iteration_end(
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\callbacks\callback_list.py", line 23, in on_iteration_end
    cb.on_iteration_end(logs, predictions)
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\callbacks\early_stopping.py", line 96, in on_iteration_end
    train_loss = self.metric(
                 ^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\utils\metric.py", line 408, in __call__
    return self.metric(y_true, y_predicted, sample_weight=sample_weight)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\utils\metric.py", line 24, in logloss
    ll = log_loss(y_true, y_predicted.astype(np.float32), sample_weight=sample_weight)
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\utils\_param_validation.py", line 213, in wrapper
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\metrics\_classification.py", line 2968, in log_loss
    raise ValueError(
ValueError: y_true and y_pred contain different number of classes 30, 2. Please provide the true labels explicitly through the labels argument. Classes found in y_true: [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
 24 25 26 27 28 29]


Please set a GitHub issue with above error message at: https://github.com/mljar/mljar-supervised/issues/new

## Error for 1_Default_LightGBM

y_true and y_pred contain different number of classes 30, 2. Please provide the true labels explicitly through the labels argument. Classes found in y_true: [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
 24 25 26 27 28 29]
Traceback (most recent call last):
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\base_automl.py", line 1183, in _fit
    trained = self.train_model(params)
              ^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\base_automl.py", line 388, in train_model
    mf.train(results_path, model_subpath)
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\model_framework.py", line 265, in train
    self.callbacks.on_iteration_end(
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\callbacks\callback_list.py", line 23, in on_iteration_end
    cb.on_iteration_end(logs, predictions)
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\callbacks\early_stopping.py", line 96, in on_iteration_end
    train_loss = self.metric(
                 ^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\utils\metric.py", line 408, in __call__
    return self.metric(y_true, y_predicted, sample_weight=sample_weight)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\utils\metric.py", line 24, in logloss
    ll = log_loss(y_true, y_predicted.astype(np.float32), sample_weight=sample_weight)
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\utils\_param_validation.py", line 213, in wrapper
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\metrics\_classification.py", line 2968, in log_loss
    raise ValueError(
ValueError: y_true and y_pred contain different number of classes 30, 2. Please provide the true labels explicitly through the labels argument. Classes found in y_true: [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
 24 25 26 27 28 29]


Please set a GitHub issue with above error message at: https://github.com/mljar/mljar-supervised/issues/new

## Error for 2_Default_Xgboost

[17:08:51] C:\actions-runner\_work\xgboost\xgboost\src\objective\./regression_loss.h:69: Check failed: base_score > 0.0f && base_score < 1.0f: base_score must be in (0,1) for logistic loss, got: 14.5
Traceback (most recent call last):
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\base_automl.py", line 1183, in _fit
    trained = self.train_model(params)
              ^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\base_automl.py", line 388, in train_model
    mf.train(results_path, model_subpath)
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\model_framework.py", line 249, in train
    learner.fit(
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\algorithms\xgboost.py", line 201, in fit
    self.model = xgb.train(
                 ^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\xgboost\core.py", line 729, in inner_f
    return func(**kwargs)
           ^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\xgboost\training.py", line 183, in train
    bst.update(dtrain, iteration=i, fobj=obj)
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\xgboost\core.py", line 2246, in update
    _check_call(
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\xgboost\core.py", line 310, in _check_call
    raise XGBoostError(py_str(_LIB.XGBGetLastError()))
xgboost.core.XGBoostError: [17:08:51] C:\actions-runner\_work\xgboost\xgboost\src\objective\./regression_loss.h:69: Check failed: base_score > 0.0f && base_score < 1.0f: base_score must be in (0,1) for logistic loss, got: 14.5


Please set a GitHub issue with above error message at: https://github.com/mljar/mljar-supervised/issues/new

## Error for 3_Default_CatBoost

catboost/private/libs/target/target_converter.cpp:410: Target with classes must contain only 2 unique values for binary classification
Traceback (most recent call last):
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\base_automl.py", line 1183, in _fit
    trained = self.train_model(params)
              ^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\base_automl.py", line 388, in train_model
    mf.train(results_path, model_subpath)
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\model_framework.py", line 249, in train
    learner.fit(
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\algorithms\catboost.py", line 225, in fit
    self.model.fit(
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\catboost\core.py", line 5245, in fit
    self._fit(X, y, cat_features, text_features, embedding_features, None, graph, sample_weight, None, None, None, None, baseline, use_best_model,
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\catboost\core.py", line 2410, in _fit
    self._train(
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\catboost\core.py", line 1790, in _train
    self._object._train(train_pool, test_pool, params, allow_clear_pool, init_model._object if init_model else None)
  File "_catboost.pyx", line 5017, in _catboost._CatBoost._train
  File "_catboost.pyx", line 5066, in _catboost._CatBoost._train
_catboost.CatBoostError: catboost/private/libs/target/target_converter.cpp:410: Target with classes must contain only 2 unique values for binary classification


Please set a GitHub issue with above error message at: https://github.com/mljar/mljar-supervised/issues/new

## Error for 4_Default_NeuralNetwork

y_true and y_pred contain different number of classes 30, 2. Please provide the true labels explicitly through the labels argument. Classes found in y_true: [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
 24 25 26 27 28 29]
Traceback (most recent call last):
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\base_automl.py", line 1183, in _fit
    trained = self.train_model(params)
              ^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\base_automl.py", line 388, in train_model
    mf.train(results_path, model_subpath)
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\model_framework.py", line 265, in train
    self.callbacks.on_iteration_end(
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\callbacks\callback_list.py", line 23, in on_iteration_end
    cb.on_iteration_end(logs, predictions)
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\callbacks\early_stopping.py", line 96, in on_iteration_end
    train_loss = self.metric(
                 ^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\utils\metric.py", line 408, in __call__
    return self.metric(y_true, y_predicted, sample_weight=sample_weight)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\utils\metric.py", line 24, in logloss
    ll = log_loss(y_true, y_predicted.astype(np.float32), sample_weight=sample_weight)
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\utils\_param_validation.py", line 213, in wrapper
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\metrics\_classification.py", line 2968, in log_loss
    raise ValueError(
ValueError: y_true and y_pred contain different number of classes 30, 2. Please provide the true labels explicitly through the labels argument. Classes found in y_true: [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
 24 25 26 27 28 29]


Please set a GitHub issue with above error message at: https://github.com/mljar/mljar-supervised/issues/new

## Error for 5_Default_RandomForest

y_true and y_pred contain different number of classes 30, 2. Please provide the true labels explicitly through the labels argument. Classes found in y_true: [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
 24 25 26 27 28 29]
Traceback (most recent call last):
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\base_automl.py", line 1183, in _fit
    trained = self.train_model(params)
              ^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\base_automl.py", line 388, in train_model
    mf.train(results_path, model_subpath)
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\model_framework.py", line 249, in train
    learner.fit(
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\algorithms\sklearn.py", line 143, in fit
    tr = self.log_metric(
         ^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\utils\metric.py", line 408, in __call__
    return self.metric(y_true, y_predicted, sample_weight=sample_weight)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\utils\metric.py", line 24, in logloss
    ll = log_loss(y_true, y_predicted.astype(np.float32), sample_weight=sample_weight)
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\utils\_param_validation.py", line 213, in wrapper
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\metrics\_classification.py", line 2968, in log_loss
    raise ValueError(
ValueError: y_true and y_pred contain different number of classes 30, 2. Please provide the true labels explicitly through the labels argument. Classes found in y_true: [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
 24 25 26 27 28 29]


Please set a GitHub issue with above error message at: https://github.com/mljar/mljar-supervised/issues/new

## Error for 6_Default_ExtraTrees

y_true and y_pred contain different number of classes 30, 2. Please provide the true labels explicitly through the labels argument. Classes found in y_true: [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
 24 25 26 27 28 29]
Traceback (most recent call last):
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\base_automl.py", line 1183, in _fit
    trained = self.train_model(params)
              ^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\base_automl.py", line 388, in train_model
    mf.train(results_path, model_subpath)
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\model_framework.py", line 249, in train
    learner.fit(
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\algorithms\sklearn.py", line 143, in fit
    tr = self.log_metric(
         ^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\utils\metric.py", line 408, in __call__
    return self.metric(y_true, y_predicted, sample_weight=sample_weight)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\utils\metric.py", line 24, in logloss
    ll = log_loss(y_true, y_predicted.astype(np.float32), sample_weight=sample_weight)
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\utils\_param_validation.py", line 213, in wrapper
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\metrics\_classification.py", line 2968, in log_loss
    raise ValueError(
ValueError: y_true and y_pred contain different number of classes 30, 2. Please provide the true labels explicitly through the labels argument. Classes found in y_true: [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
 24 25 26 27 28 29]


Please set a GitHub issue with above error message at: https://github.com/mljar/mljar-supervised/issues/new

## Error for 7_Default_NearestNeighbors

y_true and y_pred contain different number of classes 30, 2. Please provide the true labels explicitly through the labels argument. Classes found in y_true: [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
 24 25 26 27 28 29]
Traceback (most recent call last):
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\base_automl.py", line 1183, in _fit
    trained = self.train_model(params)
              ^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\base_automl.py", line 388, in train_model
    mf.train(results_path, model_subpath)
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\model_framework.py", line 265, in train
    self.callbacks.on_iteration_end(
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\callbacks\callback_list.py", line 23, in on_iteration_end
    cb.on_iteration_end(logs, predictions)
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\callbacks\early_stopping.py", line 96, in on_iteration_end
    train_loss = self.metric(
                 ^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\utils\metric.py", line 408, in __call__
    return self.metric(y_true, y_predicted, sample_weight=sample_weight)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\utils\metric.py", line 24, in logloss
    ll = log_loss(y_true, y_predicted.astype(np.float32), sample_weight=sample_weight)
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\utils\_param_validation.py", line 213, in wrapper
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\metrics\_classification.py", line 2968, in log_loss
    raise ValueError(
ValueError: y_true and y_pred contain different number of classes 30, 2. Please provide the true labels explicitly through the labels argument. Classes found in y_true: [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
 24 25 26 27 28 29]


Please set a GitHub issue with above error message at: https://github.com/mljar/mljar-supervised/issues/new

## Error for 10_LightGBM

y_true and y_pred contain different number of classes 30, 2. Please provide the true labels explicitly through the labels argument. Classes found in y_true: [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
 24 25 26 27 28 29]
Traceback (most recent call last):
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\base_automl.py", line 1183, in _fit
    trained = self.train_model(params)
              ^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\base_automl.py", line 388, in train_model
    mf.train(results_path, model_subpath)
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\model_framework.py", line 265, in train
    self.callbacks.on_iteration_end(
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\callbacks\callback_list.py", line 23, in on_iteration_end
    cb.on_iteration_end(logs, predictions)
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\callbacks\early_stopping.py", line 96, in on_iteration_end
    train_loss = self.metric(
                 ^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\utils\metric.py", line 408, in __call__
    return self.metric(y_true, y_predicted, sample_weight=sample_weight)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\utils\metric.py", line 24, in logloss
    ll = log_loss(y_true, y_predicted.astype(np.float32), sample_weight=sample_weight)
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\utils\_param_validation.py", line 213, in wrapper
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\metrics\_classification.py", line 2968, in log_loss
    raise ValueError(
ValueError: y_true and y_pred contain different number of classes 30, 2. Please provide the true labels explicitly through the labels argument. Classes found in y_true: [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
 24 25 26 27 28 29]


Please set a GitHub issue with above error message at: https://github.com/mljar/mljar-supervised/issues/new

## Error for 1_Xgboost

[17:08:52] C:\actions-runner\_work\xgboost\xgboost\src\objective\./regression_loss.h:69: Check failed: base_score > 0.0f && base_score < 1.0f: base_score must be in (0,1) for logistic loss, got: 14.5
Traceback (most recent call last):
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\base_automl.py", line 1183, in _fit
    trained = self.train_model(params)
              ^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\base_automl.py", line 388, in train_model
    mf.train(results_path, model_subpath)
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\model_framework.py", line 249, in train
    learner.fit(
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\algorithms\xgboost.py", line 201, in fit
    self.model = xgb.train(
                 ^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\xgboost\core.py", line 729, in inner_f
    return func(**kwargs)
           ^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\xgboost\training.py", line 183, in train
    bst.update(dtrain, iteration=i, fobj=obj)
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\xgboost\core.py", line 2246, in update
    _check_call(
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\xgboost\core.py", line 310, in _check_call
    raise XGBoostError(py_str(_LIB.XGBGetLastError()))
xgboost.core.XGBoostError: [17:08:52] C:\actions-runner\_work\xgboost\xgboost\src\objective\./regression_loss.h:69: Check failed: base_score > 0.0f && base_score < 1.0f: base_score must be in (0,1) for logistic loss, got: 14.5


Please set a GitHub issue with above error message at: https://github.com/mljar/mljar-supervised/issues/new

## Error for 19_CatBoost

catboost/private/libs/target/target_converter.cpp:410: Target with classes must contain only 2 unique values for binary classification
Traceback (most recent call last):
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\base_automl.py", line 1183, in _fit
    trained = self.train_model(params)
              ^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\base_automl.py", line 388, in train_model
    mf.train(results_path, model_subpath)
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\model_framework.py", line 249, in train
    learner.fit(
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\algorithms\catboost.py", line 225, in fit
    self.model.fit(
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\catboost\core.py", line 5245, in fit
    self._fit(X, y, cat_features, text_features, embedding_features, None, graph, sample_weight, None, None, None, None, baseline, use_best_model,
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\catboost\core.py", line 2410, in _fit
    self._train(
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\catboost\core.py", line 1790, in _train
    self._object._train(train_pool, test_pool, params, allow_clear_pool, init_model._object if init_model else None)
  File "_catboost.pyx", line 5017, in _catboost._CatBoost._train
  File "_catboost.pyx", line 5066, in _catboost._CatBoost._train
_catboost.CatBoostError: catboost/private/libs/target/target_converter.cpp:410: Target with classes must contain only 2 unique values for binary classification


Please set a GitHub issue with above error message at: https://github.com/mljar/mljar-supervised/issues/new

## Error for 28_RandomForest

y_true and y_pred contain different number of classes 30, 2. Please provide the true labels explicitly through the labels argument. Classes found in y_true: [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
 24 25 26 27 28 29]
Traceback (most recent call last):
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\base_automl.py", line 1183, in _fit
    trained = self.train_model(params)
              ^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\base_automl.py", line 388, in train_model
    mf.train(results_path, model_subpath)
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\model_framework.py", line 249, in train
    learner.fit(
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\algorithms\sklearn.py", line 143, in fit
    tr = self.log_metric(
         ^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\utils\metric.py", line 408, in __call__
    return self.metric(y_true, y_predicted, sample_weight=sample_weight)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\utils\metric.py", line 24, in logloss
    ll = log_loss(y_true, y_predicted.astype(np.float32), sample_weight=sample_weight)
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\utils\_param_validation.py", line 213, in wrapper
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\metrics\_classification.py", line 2968, in log_loss
    raise ValueError(
ValueError: y_true and y_pred contain different number of classes 30, 2. Please provide the true labels explicitly through the labels argument. Classes found in y_true: [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
 24 25 26 27 28 29]


Please set a GitHub issue with above error message at: https://github.com/mljar/mljar-supervised/issues/new

## Error for 37_ExtraTrees

y_true and y_pred contain different number of classes 30, 2. Please provide the true labels explicitly through the labels argument. Classes found in y_true: [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
 24 25 26 27 28 29]
Traceback (most recent call last):
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\base_automl.py", line 1183, in _fit
    trained = self.train_model(params)
              ^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\base_automl.py", line 388, in train_model
    mf.train(results_path, model_subpath)
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\model_framework.py", line 249, in train
    learner.fit(
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\algorithms\sklearn.py", line 143, in fit
    tr = self.log_metric(
         ^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\utils\metric.py", line 408, in __call__
    return self.metric(y_true, y_predicted, sample_weight=sample_weight)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\utils\metric.py", line 24, in logloss
    ll = log_loss(y_true, y_predicted.astype(np.float32), sample_weight=sample_weight)
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\utils\_param_validation.py", line 213, in wrapper
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\metrics\_classification.py", line 2968, in log_loss
    raise ValueError(
ValueError: y_true and y_pred contain different number of classes 30, 2. Please provide the true labels explicitly through the labels argument. Classes found in y_true: [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
 24 25 26 27 28 29]


Please set a GitHub issue with above error message at: https://github.com/mljar/mljar-supervised/issues/new

## Error for 46_NeuralNetwork

y_true and y_pred contain different number of classes 30, 2. Please provide the true labels explicitly through the labels argument. Classes found in y_true: [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
 24 25 26 27 28 29]
Traceback (most recent call last):
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\base_automl.py", line 1183, in _fit
    trained = self.train_model(params)
              ^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\base_automl.py", line 388, in train_model
    mf.train(results_path, model_subpath)
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\model_framework.py", line 265, in train
    self.callbacks.on_iteration_end(
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\callbacks\callback_list.py", line 23, in on_iteration_end
    cb.on_iteration_end(logs, predictions)
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\callbacks\early_stopping.py", line 96, in on_iteration_end
    train_loss = self.metric(
                 ^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\utils\metric.py", line 408, in __call__
    return self.metric(y_true, y_predicted, sample_weight=sample_weight)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\utils\metric.py", line 24, in logloss
    ll = log_loss(y_true, y_predicted.astype(np.float32), sample_weight=sample_weight)
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\utils\_param_validation.py", line 213, in wrapper
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\metrics\_classification.py", line 2968, in log_loss
    raise ValueError(
ValueError: y_true and y_pred contain different number of classes 30, 2. Please provide the true labels explicitly through the labels argument. Classes found in y_true: [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
 24 25 26 27 28 29]


Please set a GitHub issue with above error message at: https://github.com/mljar/mljar-supervised/issues/new

## Error for 55_NearestNeighbors

y_true and y_pred contain different number of classes 30, 2. Please provide the true labels explicitly through the labels argument. Classes found in y_true: [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
 24 25 26 27 28 29]
Traceback (most recent call last):
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\base_automl.py", line 1183, in _fit
    trained = self.train_model(params)
              ^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\base_automl.py", line 388, in train_model
    mf.train(results_path, model_subpath)
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\model_framework.py", line 265, in train
    self.callbacks.on_iteration_end(
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\callbacks\callback_list.py", line 23, in on_iteration_end
    cb.on_iteration_end(logs, predictions)
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\callbacks\early_stopping.py", line 96, in on_iteration_end
    train_loss = self.metric(
                 ^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\utils\metric.py", line 408, in __call__
    return self.metric(y_true, y_predicted, sample_weight=sample_weight)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\utils\metric.py", line 24, in logloss
    ll = log_loss(y_true, y_predicted.astype(np.float32), sample_weight=sample_weight)
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\utils\_param_validation.py", line 213, in wrapper
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\metrics\_classification.py", line 2968, in log_loss
    raise ValueError(
ValueError: y_true and y_pred contain different number of classes 30, 2. Please provide the true labels explicitly through the labels argument. Classes found in y_true: [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
 24 25 26 27 28 29]


Please set a GitHub issue with above error message at: https://github.com/mljar/mljar-supervised/issues/new

## Error for 11_LightGBM

y_true and y_pred contain different number of classes 30, 2. Please provide the true labels explicitly through the labels argument. Classes found in y_true: [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
 24 25 26 27 28 29]
Traceback (most recent call last):
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\base_automl.py", line 1183, in _fit
    trained = self.train_model(params)
              ^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\base_automl.py", line 388, in train_model
    mf.train(results_path, model_subpath)
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\model_framework.py", line 265, in train
    self.callbacks.on_iteration_end(
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\callbacks\callback_list.py", line 23, in on_iteration_end
    cb.on_iteration_end(logs, predictions)
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\callbacks\early_stopping.py", line 96, in on_iteration_end
    train_loss = self.metric(
                 ^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\utils\metric.py", line 408, in __call__
    return self.metric(y_true, y_predicted, sample_weight=sample_weight)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\utils\metric.py", line 24, in logloss
    ll = log_loss(y_true, y_predicted.astype(np.float32), sample_weight=sample_weight)
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\utils\_param_validation.py", line 213, in wrapper
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\metrics\_classification.py", line 2968, in log_loss
    raise ValueError(
ValueError: y_true and y_pred contain different number of classes 30, 2. Please provide the true labels explicitly through the labels argument. Classes found in y_true: [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
 24 25 26 27 28 29]


Please set a GitHub issue with above error message at: https://github.com/mljar/mljar-supervised/issues/new

## Error for 2_Xgboost

[17:08:53] C:\actions-runner\_work\xgboost\xgboost\src\objective\./regression_loss.h:69: Check failed: base_score > 0.0f && base_score < 1.0f: base_score must be in (0,1) for logistic loss, got: 14.5
Traceback (most recent call last):
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\base_automl.py", line 1183, in _fit
    trained = self.train_model(params)
              ^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\base_automl.py", line 388, in train_model
    mf.train(results_path, model_subpath)
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\model_framework.py", line 249, in train
    learner.fit(
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\algorithms\xgboost.py", line 201, in fit
    self.model = xgb.train(
                 ^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\xgboost\core.py", line 729, in inner_f
    return func(**kwargs)
           ^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\xgboost\training.py", line 183, in train
    bst.update(dtrain, iteration=i, fobj=obj)
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\xgboost\core.py", line 2246, in update
    _check_call(
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\xgboost\core.py", line 310, in _check_call
    raise XGBoostError(py_str(_LIB.XGBGetLastError()))
xgboost.core.XGBoostError: [17:08:53] C:\actions-runner\_work\xgboost\xgboost\src\objective\./regression_loss.h:69: Check failed: base_score > 0.0f && base_score < 1.0f: base_score must be in (0,1) for logistic loss, got: 14.5


Please set a GitHub issue with above error message at: https://github.com/mljar/mljar-supervised/issues/new

## Error for 20_CatBoost

catboost/private/libs/target/target_converter.cpp:410: Target with classes must contain only 2 unique values for binary classification
Traceback (most recent call last):
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\base_automl.py", line 1183, in _fit
    trained = self.train_model(params)
              ^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\base_automl.py", line 388, in train_model
    mf.train(results_path, model_subpath)
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\model_framework.py", line 249, in train
    learner.fit(
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\algorithms\catboost.py", line 225, in fit
    self.model.fit(
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\catboost\core.py", line 5245, in fit
    self._fit(X, y, cat_features, text_features, embedding_features, None, graph, sample_weight, None, None, None, None, baseline, use_best_model,
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\catboost\core.py", line 2410, in _fit
    self._train(
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\catboost\core.py", line 1790, in _train
    self._object._train(train_pool, test_pool, params, allow_clear_pool, init_model._object if init_model else None)
  File "_catboost.pyx", line 5017, in _catboost._CatBoost._train
  File "_catboost.pyx", line 5066, in _catboost._CatBoost._train
_catboost.CatBoostError: catboost/private/libs/target/target_converter.cpp:410: Target with classes must contain only 2 unique values for binary classification


Please set a GitHub issue with above error message at: https://github.com/mljar/mljar-supervised/issues/new

## Error for 29_RandomForest

y_true and y_pred contain different number of classes 30, 2. Please provide the true labels explicitly through the labels argument. Classes found in y_true: [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
 24 25 26 27 28 29]
Traceback (most recent call last):
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\base_automl.py", line 1183, in _fit
    trained = self.train_model(params)
              ^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\base_automl.py", line 388, in train_model
    mf.train(results_path, model_subpath)
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\model_framework.py", line 249, in train
    learner.fit(
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\algorithms\sklearn.py", line 143, in fit
    tr = self.log_metric(
         ^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\utils\metric.py", line 408, in __call__
    return self.metric(y_true, y_predicted, sample_weight=sample_weight)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\utils\metric.py", line 24, in logloss
    ll = log_loss(y_true, y_predicted.astype(np.float32), sample_weight=sample_weight)
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\utils\_param_validation.py", line 213, in wrapper
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\metrics\_classification.py", line 2968, in log_loss
    raise ValueError(
ValueError: y_true and y_pred contain different number of classes 30, 2. Please provide the true labels explicitly through the labels argument. Classes found in y_true: [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
 24 25 26 27 28 29]


Please set a GitHub issue with above error message at: https://github.com/mljar/mljar-supervised/issues/new

## Error for 38_ExtraTrees

y_true and y_pred contain different number of classes 30, 2. Please provide the true labels explicitly through the labels argument. Classes found in y_true: [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
 24 25 26 27 28 29]
Traceback (most recent call last):
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\base_automl.py", line 1183, in _fit
    trained = self.train_model(params)
              ^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\base_automl.py", line 388, in train_model
    mf.train(results_path, model_subpath)
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\model_framework.py", line 249, in train
    learner.fit(
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\algorithms\sklearn.py", line 143, in fit
    tr = self.log_metric(
         ^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\utils\metric.py", line 408, in __call__
    return self.metric(y_true, y_predicted, sample_weight=sample_weight)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\utils\metric.py", line 24, in logloss
    ll = log_loss(y_true, y_predicted.astype(np.float32), sample_weight=sample_weight)
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\utils\_param_validation.py", line 213, in wrapper
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\metrics\_classification.py", line 2968, in log_loss
    raise ValueError(
ValueError: y_true and y_pred contain different number of classes 30, 2. Please provide the true labels explicitly through the labels argument. Classes found in y_true: [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
 24 25 26 27 28 29]


Please set a GitHub issue with above error message at: https://github.com/mljar/mljar-supervised/issues/new

## Error for 47_NeuralNetwork

y_true and y_pred contain different number of classes 30, 2. Please provide the true labels explicitly through the labels argument. Classes found in y_true: [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
 24 25 26 27 28 29]
Traceback (most recent call last):
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\base_automl.py", line 1183, in _fit
    trained = self.train_model(params)
              ^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\base_automl.py", line 388, in train_model
    mf.train(results_path, model_subpath)
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\model_framework.py", line 265, in train
    self.callbacks.on_iteration_end(
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\callbacks\callback_list.py", line 23, in on_iteration_end
    cb.on_iteration_end(logs, predictions)
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\callbacks\early_stopping.py", line 96, in on_iteration_end
    train_loss = self.metric(
                 ^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\utils\metric.py", line 408, in __call__
    return self.metric(y_true, y_predicted, sample_weight=sample_weight)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\utils\metric.py", line 24, in logloss
    ll = log_loss(y_true, y_predicted.astype(np.float32), sample_weight=sample_weight)
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\utils\_param_validation.py", line 213, in wrapper
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\metrics\_classification.py", line 2968, in log_loss
    raise ValueError(
ValueError: y_true and y_pred contain different number of classes 30, 2. Please provide the true labels explicitly through the labels argument. Classes found in y_true: [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
 24 25 26 27 28 29]


Please set a GitHub issue with above error message at: https://github.com/mljar/mljar-supervised/issues/new

## Error for 56_NearestNeighbors

y_true and y_pred contain different number of classes 30, 2. Please provide the true labels explicitly through the labels argument. Classes found in y_true: [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
 24 25 26 27 28 29]
Traceback (most recent call last):
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\base_automl.py", line 1183, in _fit
    trained = self.train_model(params)
              ^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\base_automl.py", line 388, in train_model
    mf.train(results_path, model_subpath)
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\model_framework.py", line 265, in train
    self.callbacks.on_iteration_end(
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\callbacks\callback_list.py", line 23, in on_iteration_end
    cb.on_iteration_end(logs, predictions)
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\callbacks\early_stopping.py", line 96, in on_iteration_end
    train_loss = self.metric(
                 ^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\utils\metric.py", line 408, in __call__
    return self.metric(y_true, y_predicted, sample_weight=sample_weight)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\utils\metric.py", line 24, in logloss
    ll = log_loss(y_true, y_predicted.astype(np.float32), sample_weight=sample_weight)
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\utils\_param_validation.py", line 213, in wrapper
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\metrics\_classification.py", line 2968, in log_loss
    raise ValueError(
ValueError: y_true and y_pred contain different number of classes 30, 2. Please provide the true labels explicitly through the labels argument. Classes found in y_true: [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
 24 25 26 27 28 29]


Please set a GitHub issue with above error message at: https://github.com/mljar/mljar-supervised/issues/new

## Error for 12_LightGBM

y_true and y_pred contain different number of classes 30, 2. Please provide the true labels explicitly through the labels argument. Classes found in y_true: [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
 24 25 26 27 28 29]
Traceback (most recent call last):
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\base_automl.py", line 1183, in _fit
    trained = self.train_model(params)
              ^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\base_automl.py", line 388, in train_model
    mf.train(results_path, model_subpath)
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\model_framework.py", line 265, in train
    self.callbacks.on_iteration_end(
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\callbacks\callback_list.py", line 23, in on_iteration_end
    cb.on_iteration_end(logs, predictions)
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\callbacks\early_stopping.py", line 96, in on_iteration_end
    train_loss = self.metric(
                 ^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\utils\metric.py", line 408, in __call__
    return self.metric(y_true, y_predicted, sample_weight=sample_weight)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\utils\metric.py", line 24, in logloss
    ll = log_loss(y_true, y_predicted.astype(np.float32), sample_weight=sample_weight)
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\utils\_param_validation.py", line 213, in wrapper
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\metrics\_classification.py", line 2968, in log_loss
    raise ValueError(
ValueError: y_true and y_pred contain different number of classes 30, 2. Please provide the true labels explicitly through the labels argument. Classes found in y_true: [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
 24 25 26 27 28 29]


Please set a GitHub issue with above error message at: https://github.com/mljar/mljar-supervised/issues/new

## Error for 3_Xgboost

[17:08:54] C:\actions-runner\_work\xgboost\xgboost\src\objective\./regression_loss.h:69: Check failed: base_score > 0.0f && base_score < 1.0f: base_score must be in (0,1) for logistic loss, got: 14.5
Traceback (most recent call last):
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\base_automl.py", line 1183, in _fit
    trained = self.train_model(params)
              ^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\base_automl.py", line 388, in train_model
    mf.train(results_path, model_subpath)
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\model_framework.py", line 249, in train
    learner.fit(
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\algorithms\xgboost.py", line 201, in fit
    self.model = xgb.train(
                 ^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\xgboost\core.py", line 729, in inner_f
    return func(**kwargs)
           ^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\xgboost\training.py", line 183, in train
    bst.update(dtrain, iteration=i, fobj=obj)
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\xgboost\core.py", line 2246, in update
    _check_call(
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\xgboost\core.py", line 310, in _check_call
    raise XGBoostError(py_str(_LIB.XGBGetLastError()))
xgboost.core.XGBoostError: [17:08:54] C:\actions-runner\_work\xgboost\xgboost\src\objective\./regression_loss.h:69: Check failed: base_score > 0.0f && base_score < 1.0f: base_score must be in (0,1) for logistic loss, got: 14.5


Please set a GitHub issue with above error message at: https://github.com/mljar/mljar-supervised/issues/new

## Error for 21_CatBoost

catboost/private/libs/target/target_converter.cpp:410: Target with classes must contain only 2 unique values for binary classification
Traceback (most recent call last):
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\base_automl.py", line 1183, in _fit
    trained = self.train_model(params)
              ^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\base_automl.py", line 388, in train_model
    mf.train(results_path, model_subpath)
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\model_framework.py", line 249, in train
    learner.fit(
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\algorithms\catboost.py", line 225, in fit
    self.model.fit(
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\catboost\core.py", line 5245, in fit
    self._fit(X, y, cat_features, text_features, embedding_features, None, graph, sample_weight, None, None, None, None, baseline, use_best_model,
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\catboost\core.py", line 2410, in _fit
    self._train(
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\catboost\core.py", line 1790, in _train
    self._object._train(train_pool, test_pool, params, allow_clear_pool, init_model._object if init_model else None)
  File "_catboost.pyx", line 5017, in _catboost._CatBoost._train
  File "_catboost.pyx", line 5066, in _catboost._CatBoost._train
_catboost.CatBoostError: catboost/private/libs/target/target_converter.cpp:410: Target with classes must contain only 2 unique values for binary classification


Please set a GitHub issue with above error message at: https://github.com/mljar/mljar-supervised/issues/new

## Error for 30_RandomForest

y_true and y_pred contain different number of classes 30, 2. Please provide the true labels explicitly through the labels argument. Classes found in y_true: [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
 24 25 26 27 28 29]
Traceback (most recent call last):
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\base_automl.py", line 1183, in _fit
    trained = self.train_model(params)
              ^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\base_automl.py", line 388, in train_model
    mf.train(results_path, model_subpath)
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\model_framework.py", line 249, in train
    learner.fit(
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\algorithms\sklearn.py", line 143, in fit
    tr = self.log_metric(
         ^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\utils\metric.py", line 408, in __call__
    return self.metric(y_true, y_predicted, sample_weight=sample_weight)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\utils\metric.py", line 24, in logloss
    ll = log_loss(y_true, y_predicted.astype(np.float32), sample_weight=sample_weight)
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\utils\_param_validation.py", line 213, in wrapper
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\metrics\_classification.py", line 2968, in log_loss
    raise ValueError(
ValueError: y_true and y_pred contain different number of classes 30, 2. Please provide the true labels explicitly through the labels argument. Classes found in y_true: [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
 24 25 26 27 28 29]


Please set a GitHub issue with above error message at: https://github.com/mljar/mljar-supervised/issues/new

## Error for 39_ExtraTrees

y_true and y_pred contain different number of classes 30, 2. Please provide the true labels explicitly through the labels argument. Classes found in y_true: [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
 24 25 26 27 28 29]
Traceback (most recent call last):
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\base_automl.py", line 1183, in _fit
    trained = self.train_model(params)
              ^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\base_automl.py", line 388, in train_model
    mf.train(results_path, model_subpath)
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\model_framework.py", line 249, in train
    learner.fit(
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\algorithms\sklearn.py", line 143, in fit
    tr = self.log_metric(
         ^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\utils\metric.py", line 408, in __call__
    return self.metric(y_true, y_predicted, sample_weight=sample_weight)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\utils\metric.py", line 24, in logloss
    ll = log_loss(y_true, y_predicted.astype(np.float32), sample_weight=sample_weight)
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\utils\_param_validation.py", line 213, in wrapper
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\metrics\_classification.py", line 2968, in log_loss
    raise ValueError(
ValueError: y_true and y_pred contain different number of classes 30, 2. Please provide the true labels explicitly through the labels argument. Classes found in y_true: [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
 24 25 26 27 28 29]


Please set a GitHub issue with above error message at: https://github.com/mljar/mljar-supervised/issues/new

## Error for 48_NeuralNetwork

y_true and y_pred contain different number of classes 30, 2. Please provide the true labels explicitly through the labels argument. Classes found in y_true: [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
 24 25 26 27 28 29]
Traceback (most recent call last):
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\base_automl.py", line 1183, in _fit
    trained = self.train_model(params)
              ^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\base_automl.py", line 388, in train_model
    mf.train(results_path, model_subpath)
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\model_framework.py", line 265, in train
    self.callbacks.on_iteration_end(
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\callbacks\callback_list.py", line 23, in on_iteration_end
    cb.on_iteration_end(logs, predictions)
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\callbacks\early_stopping.py", line 96, in on_iteration_end
    train_loss = self.metric(
                 ^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\utils\metric.py", line 408, in __call__
    return self.metric(y_true, y_predicted, sample_weight=sample_weight)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\utils\metric.py", line 24, in logloss
    ll = log_loss(y_true, y_predicted.astype(np.float32), sample_weight=sample_weight)
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\utils\_param_validation.py", line 213, in wrapper
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\metrics\_classification.py", line 2968, in log_loss
    raise ValueError(
ValueError: y_true and y_pred contain different number of classes 30, 2. Please provide the true labels explicitly through the labels argument. Classes found in y_true: [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
 24 25 26 27 28 29]


Please set a GitHub issue with above error message at: https://github.com/mljar/mljar-supervised/issues/new

## Error for 57_NearestNeighbors

y_true and y_pred contain different number of classes 30, 2. Please provide the true labels explicitly through the labels argument. Classes found in y_true: [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
 24 25 26 27 28 29]
Traceback (most recent call last):
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\base_automl.py", line 1183, in _fit
    trained = self.train_model(params)
              ^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\base_automl.py", line 388, in train_model
    mf.train(results_path, model_subpath)
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\model_framework.py", line 265, in train
    self.callbacks.on_iteration_end(
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\callbacks\callback_list.py", line 23, in on_iteration_end
    cb.on_iteration_end(logs, predictions)
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\callbacks\early_stopping.py", line 96, in on_iteration_end
    train_loss = self.metric(
                 ^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\utils\metric.py", line 408, in __call__
    return self.metric(y_true, y_predicted, sample_weight=sample_weight)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\utils\metric.py", line 24, in logloss
    ll = log_loss(y_true, y_predicted.astype(np.float32), sample_weight=sample_weight)
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\utils\_param_validation.py", line 213, in wrapper
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\metrics\_classification.py", line 2968, in log_loss
    raise ValueError(
ValueError: y_true and y_pred contain different number of classes 30, 2. Please provide the true labels explicitly through the labels argument. Classes found in y_true: [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
 24 25 26 27 28 29]


Please set a GitHub issue with above error message at: https://github.com/mljar/mljar-supervised/issues/new

## Error for 13_LightGBM

y_true and y_pred contain different number of classes 30, 2. Please provide the true labels explicitly through the labels argument. Classes found in y_true: [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
 24 25 26 27 28 29]
Traceback (most recent call last):
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\base_automl.py", line 1183, in _fit
    trained = self.train_model(params)
              ^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\base_automl.py", line 388, in train_model
    mf.train(results_path, model_subpath)
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\model_framework.py", line 265, in train
    self.callbacks.on_iteration_end(
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\callbacks\callback_list.py", line 23, in on_iteration_end
    cb.on_iteration_end(logs, predictions)
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\callbacks\early_stopping.py", line 96, in on_iteration_end
    train_loss = self.metric(
                 ^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\utils\metric.py", line 408, in __call__
    return self.metric(y_true, y_predicted, sample_weight=sample_weight)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\utils\metric.py", line 24, in logloss
    ll = log_loss(y_true, y_predicted.astype(np.float32), sample_weight=sample_weight)
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\utils\_param_validation.py", line 213, in wrapper
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\metrics\_classification.py", line 2968, in log_loss
    raise ValueError(
ValueError: y_true and y_pred contain different number of classes 30, 2. Please provide the true labels explicitly through the labels argument. Classes found in y_true: [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
 24 25 26 27 28 29]


Please set a GitHub issue with above error message at: https://github.com/mljar/mljar-supervised/issues/new

## Error for 4_Xgboost

[17:08:56] C:\actions-runner\_work\xgboost\xgboost\src\objective\./regression_loss.h:69: Check failed: base_score > 0.0f && base_score < 1.0f: base_score must be in (0,1) for logistic loss, got: 14.5
Traceback (most recent call last):
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\base_automl.py", line 1183, in _fit
    trained = self.train_model(params)
              ^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\base_automl.py", line 388, in train_model
    mf.train(results_path, model_subpath)
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\model_framework.py", line 249, in train
    learner.fit(
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\algorithms\xgboost.py", line 201, in fit
    self.model = xgb.train(
                 ^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\xgboost\core.py", line 729, in inner_f
    return func(**kwargs)
           ^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\xgboost\training.py", line 183, in train
    bst.update(dtrain, iteration=i, fobj=obj)
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\xgboost\core.py", line 2246, in update
    _check_call(
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\xgboost\core.py", line 310, in _check_call
    raise XGBoostError(py_str(_LIB.XGBGetLastError()))
xgboost.core.XGBoostError: [17:08:56] C:\actions-runner\_work\xgboost\xgboost\src\objective\./regression_loss.h:69: Check failed: base_score > 0.0f && base_score < 1.0f: base_score must be in (0,1) for logistic loss, got: 14.5


Please set a GitHub issue with above error message at: https://github.com/mljar/mljar-supervised/issues/new

## Error for 22_CatBoost

catboost/private/libs/target/target_converter.cpp:410: Target with classes must contain only 2 unique values for binary classification
Traceback (most recent call last):
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\base_automl.py", line 1183, in _fit
    trained = self.train_model(params)
              ^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\base_automl.py", line 388, in train_model
    mf.train(results_path, model_subpath)
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\model_framework.py", line 249, in train
    learner.fit(
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\algorithms\catboost.py", line 225, in fit
    self.model.fit(
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\catboost\core.py", line 5245, in fit
    self._fit(X, y, cat_features, text_features, embedding_features, None, graph, sample_weight, None, None, None, None, baseline, use_best_model,
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\catboost\core.py", line 2410, in _fit
    self._train(
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\catboost\core.py", line 1790, in _train
    self._object._train(train_pool, test_pool, params, allow_clear_pool, init_model._object if init_model else None)
  File "_catboost.pyx", line 5017, in _catboost._CatBoost._train
  File "_catboost.pyx", line 5066, in _catboost._CatBoost._train
_catboost.CatBoostError: catboost/private/libs/target/target_converter.cpp:410: Target with classes must contain only 2 unique values for binary classification


Please set a GitHub issue with above error message at: https://github.com/mljar/mljar-supervised/issues/new

## Error for 31_RandomForest

y_true and y_pred contain different number of classes 30, 2. Please provide the true labels explicitly through the labels argument. Classes found in y_true: [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
 24 25 26 27 28 29]
Traceback (most recent call last):
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\base_automl.py", line 1183, in _fit
    trained = self.train_model(params)
              ^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\base_automl.py", line 388, in train_model
    mf.train(results_path, model_subpath)
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\model_framework.py", line 249, in train
    learner.fit(
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\algorithms\sklearn.py", line 143, in fit
    tr = self.log_metric(
         ^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\utils\metric.py", line 408, in __call__
    return self.metric(y_true, y_predicted, sample_weight=sample_weight)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\utils\metric.py", line 24, in logloss
    ll = log_loss(y_true, y_predicted.astype(np.float32), sample_weight=sample_weight)
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\utils\_param_validation.py", line 213, in wrapper
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\metrics\_classification.py", line 2968, in log_loss
    raise ValueError(
ValueError: y_true and y_pred contain different number of classes 30, 2. Please provide the true labels explicitly through the labels argument. Classes found in y_true: [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
 24 25 26 27 28 29]


Please set a GitHub issue with above error message at: https://github.com/mljar/mljar-supervised/issues/new

## Error for 40_ExtraTrees

y_true and y_pred contain different number of classes 30, 2. Please provide the true labels explicitly through the labels argument. Classes found in y_true: [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
 24 25 26 27 28 29]
Traceback (most recent call last):
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\base_automl.py", line 1183, in _fit
    trained = self.train_model(params)
              ^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\base_automl.py", line 388, in train_model
    mf.train(results_path, model_subpath)
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\model_framework.py", line 249, in train
    learner.fit(
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\algorithms\sklearn.py", line 143, in fit
    tr = self.log_metric(
         ^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\utils\metric.py", line 408, in __call__
    return self.metric(y_true, y_predicted, sample_weight=sample_weight)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\utils\metric.py", line 24, in logloss
    ll = log_loss(y_true, y_predicted.astype(np.float32), sample_weight=sample_weight)
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\utils\_param_validation.py", line 213, in wrapper
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\metrics\_classification.py", line 2968, in log_loss
    raise ValueError(
ValueError: y_true and y_pred contain different number of classes 30, 2. Please provide the true labels explicitly through the labels argument. Classes found in y_true: [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
 24 25 26 27 28 29]


Please set a GitHub issue with above error message at: https://github.com/mljar/mljar-supervised/issues/new

## Error for 49_NeuralNetwork

y_true and y_pred contain different number of classes 30, 2. Please provide the true labels explicitly through the labels argument. Classes found in y_true: [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
 24 25 26 27 28 29]
Traceback (most recent call last):
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\base_automl.py", line 1183, in _fit
    trained = self.train_model(params)
              ^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\base_automl.py", line 388, in train_model
    mf.train(results_path, model_subpath)
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\model_framework.py", line 265, in train
    self.callbacks.on_iteration_end(
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\callbacks\callback_list.py", line 23, in on_iteration_end
    cb.on_iteration_end(logs, predictions)
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\callbacks\early_stopping.py", line 96, in on_iteration_end
    train_loss = self.metric(
                 ^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\utils\metric.py", line 408, in __call__
    return self.metric(y_true, y_predicted, sample_weight=sample_weight)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\utils\metric.py", line 24, in logloss
    ll = log_loss(y_true, y_predicted.astype(np.float32), sample_weight=sample_weight)
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\utils\_param_validation.py", line 213, in wrapper
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\metrics\_classification.py", line 2968, in log_loss
    raise ValueError(
ValueError: y_true and y_pred contain different number of classes 30, 2. Please provide the true labels explicitly through the labels argument. Classes found in y_true: [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
 24 25 26 27 28 29]


Please set a GitHub issue with above error message at: https://github.com/mljar/mljar-supervised/issues/new

## Error for 58_NearestNeighbors

y_true and y_pred contain different number of classes 30, 2. Please provide the true labels explicitly through the labels argument. Classes found in y_true: [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
 24 25 26 27 28 29]
Traceback (most recent call last):
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\base_automl.py", line 1183, in _fit
    trained = self.train_model(params)
              ^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\base_automl.py", line 388, in train_model
    mf.train(results_path, model_subpath)
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\model_framework.py", line 265, in train
    self.callbacks.on_iteration_end(
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\callbacks\callback_list.py", line 23, in on_iteration_end
    cb.on_iteration_end(logs, predictions)
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\callbacks\early_stopping.py", line 96, in on_iteration_end
    train_loss = self.metric(
                 ^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\utils\metric.py", line 408, in __call__
    return self.metric(y_true, y_predicted, sample_weight=sample_weight)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\utils\metric.py", line 24, in logloss
    ll = log_loss(y_true, y_predicted.astype(np.float32), sample_weight=sample_weight)
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\utils\_param_validation.py", line 213, in wrapper
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\metrics\_classification.py", line 2968, in log_loss
    raise ValueError(
ValueError: y_true and y_pred contain different number of classes 30, 2. Please provide the true labels explicitly through the labels argument. Classes found in y_true: [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
 24 25 26 27 28 29]


Please set a GitHub issue with above error message at: https://github.com/mljar/mljar-supervised/issues/new

## Error for 14_LightGBM

y_true and y_pred contain different number of classes 30, 2. Please provide the true labels explicitly through the labels argument. Classes found in y_true: [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
 24 25 26 27 28 29]
Traceback (most recent call last):
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\base_automl.py", line 1183, in _fit
    trained = self.train_model(params)
              ^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\base_automl.py", line 388, in train_model
    mf.train(results_path, model_subpath)
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\model_framework.py", line 265, in train
    self.callbacks.on_iteration_end(
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\callbacks\callback_list.py", line 23, in on_iteration_end
    cb.on_iteration_end(logs, predictions)
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\callbacks\early_stopping.py", line 96, in on_iteration_end
    train_loss = self.metric(
                 ^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\utils\metric.py", line 408, in __call__
    return self.metric(y_true, y_predicted, sample_weight=sample_weight)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\utils\metric.py", line 24, in logloss
    ll = log_loss(y_true, y_predicted.astype(np.float32), sample_weight=sample_weight)
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\utils\_param_validation.py", line 213, in wrapper
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\metrics\_classification.py", line 2968, in log_loss
    raise ValueError(
ValueError: y_true and y_pred contain different number of classes 30, 2. Please provide the true labels explicitly through the labels argument. Classes found in y_true: [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
 24 25 26 27 28 29]


Please set a GitHub issue with above error message at: https://github.com/mljar/mljar-supervised/issues/new

## Error for 5_Xgboost

[17:08:57] C:\actions-runner\_work\xgboost\xgboost\src\objective\./regression_loss.h:69: Check failed: base_score > 0.0f && base_score < 1.0f: base_score must be in (0,1) for logistic loss, got: 14.5
Traceback (most recent call last):
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\base_automl.py", line 1183, in _fit
    trained = self.train_model(params)
              ^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\base_automl.py", line 388, in train_model
    mf.train(results_path, model_subpath)
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\model_framework.py", line 249, in train
    learner.fit(
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\algorithms\xgboost.py", line 201, in fit
    self.model = xgb.train(
                 ^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\xgboost\core.py", line 729, in inner_f
    return func(**kwargs)
           ^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\xgboost\training.py", line 183, in train
    bst.update(dtrain, iteration=i, fobj=obj)
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\xgboost\core.py", line 2246, in update
    _check_call(
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\xgboost\core.py", line 310, in _check_call
    raise XGBoostError(py_str(_LIB.XGBGetLastError()))
xgboost.core.XGBoostError: [17:08:57] C:\actions-runner\_work\xgboost\xgboost\src\objective\./regression_loss.h:69: Check failed: base_score > 0.0f && base_score < 1.0f: base_score must be in (0,1) for logistic loss, got: 14.5


Please set a GitHub issue with above error message at: https://github.com/mljar/mljar-supervised/issues/new

## Error for 23_CatBoost

catboost/private/libs/target/target_converter.cpp:410: Target with classes must contain only 2 unique values for binary classification
Traceback (most recent call last):
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\base_automl.py", line 1183, in _fit
    trained = self.train_model(params)
              ^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\base_automl.py", line 388, in train_model
    mf.train(results_path, model_subpath)
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\model_framework.py", line 249, in train
    learner.fit(
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\algorithms\catboost.py", line 225, in fit
    self.model.fit(
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\catboost\core.py", line 5245, in fit
    self._fit(X, y, cat_features, text_features, embedding_features, None, graph, sample_weight, None, None, None, None, baseline, use_best_model,
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\catboost\core.py", line 2410, in _fit
    self._train(
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\catboost\core.py", line 1790, in _train
    self._object._train(train_pool, test_pool, params, allow_clear_pool, init_model._object if init_model else None)
  File "_catboost.pyx", line 5017, in _catboost._CatBoost._train
  File "_catboost.pyx", line 5066, in _catboost._CatBoost._train
_catboost.CatBoostError: catboost/private/libs/target/target_converter.cpp:410: Target with classes must contain only 2 unique values for binary classification


Please set a GitHub issue with above error message at: https://github.com/mljar/mljar-supervised/issues/new

## Error for 32_RandomForest

y_true and y_pred contain different number of classes 30, 2. Please provide the true labels explicitly through the labels argument. Classes found in y_true: [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
 24 25 26 27 28 29]
Traceback (most recent call last):
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\base_automl.py", line 1183, in _fit
    trained = self.train_model(params)
              ^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\base_automl.py", line 388, in train_model
    mf.train(results_path, model_subpath)
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\model_framework.py", line 249, in train
    learner.fit(
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\algorithms\sklearn.py", line 143, in fit
    tr = self.log_metric(
         ^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\utils\metric.py", line 408, in __call__
    return self.metric(y_true, y_predicted, sample_weight=sample_weight)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\utils\metric.py", line 24, in logloss
    ll = log_loss(y_true, y_predicted.astype(np.float32), sample_weight=sample_weight)
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\utils\_param_validation.py", line 213, in wrapper
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\metrics\_classification.py", line 2968, in log_loss
    raise ValueError(
ValueError: y_true and y_pred contain different number of classes 30, 2. Please provide the true labels explicitly through the labels argument. Classes found in y_true: [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
 24 25 26 27 28 29]


Please set a GitHub issue with above error message at: https://github.com/mljar/mljar-supervised/issues/new

## Error for 41_ExtraTrees

y_true and y_pred contain different number of classes 30, 2. Please provide the true labels explicitly through the labels argument. Classes found in y_true: [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
 24 25 26 27 28 29]
Traceback (most recent call last):
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\base_automl.py", line 1183, in _fit
    trained = self.train_model(params)
              ^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\base_automl.py", line 388, in train_model
    mf.train(results_path, model_subpath)
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\model_framework.py", line 249, in train
    learner.fit(
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\algorithms\sklearn.py", line 143, in fit
    tr = self.log_metric(
         ^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\utils\metric.py", line 408, in __call__
    return self.metric(y_true, y_predicted, sample_weight=sample_weight)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\utils\metric.py", line 24, in logloss
    ll = log_loss(y_true, y_predicted.astype(np.float32), sample_weight=sample_weight)
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\utils\_param_validation.py", line 213, in wrapper
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\metrics\_classification.py", line 2968, in log_loss
    raise ValueError(
ValueError: y_true and y_pred contain different number of classes 30, 2. Please provide the true labels explicitly through the labels argument. Classes found in y_true: [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
 24 25 26 27 28 29]


Please set a GitHub issue with above error message at: https://github.com/mljar/mljar-supervised/issues/new

## Error for 50_NeuralNetwork

y_true and y_pred contain different number of classes 30, 2. Please provide the true labels explicitly through the labels argument. Classes found in y_true: [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
 24 25 26 27 28 29]
Traceback (most recent call last):
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\base_automl.py", line 1183, in _fit
    trained = self.train_model(params)
              ^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\base_automl.py", line 388, in train_model
    mf.train(results_path, model_subpath)
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\model_framework.py", line 265, in train
    self.callbacks.on_iteration_end(
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\callbacks\callback_list.py", line 23, in on_iteration_end
    cb.on_iteration_end(logs, predictions)
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\callbacks\early_stopping.py", line 96, in on_iteration_end
    train_loss = self.metric(
                 ^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\utils\metric.py", line 408, in __call__
    return self.metric(y_true, y_predicted, sample_weight=sample_weight)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\utils\metric.py", line 24, in logloss
    ll = log_loss(y_true, y_predicted.astype(np.float32), sample_weight=sample_weight)
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\utils\_param_validation.py", line 213, in wrapper
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\metrics\_classification.py", line 2968, in log_loss
    raise ValueError(
ValueError: y_true and y_pred contain different number of classes 30, 2. Please provide the true labels explicitly through the labels argument. Classes found in y_true: [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
 24 25 26 27 28 29]


Please set a GitHub issue with above error message at: https://github.com/mljar/mljar-supervised/issues/new

## Error for 59_NearestNeighbors

y_true and y_pred contain different number of classes 30, 2. Please provide the true labels explicitly through the labels argument. Classes found in y_true: [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
 24 25 26 27 28 29]
Traceback (most recent call last):
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\base_automl.py", line 1183, in _fit
    trained = self.train_model(params)
              ^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\base_automl.py", line 388, in train_model
    mf.train(results_path, model_subpath)
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\model_framework.py", line 265, in train
    self.callbacks.on_iteration_end(
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\callbacks\callback_list.py", line 23, in on_iteration_end
    cb.on_iteration_end(logs, predictions)
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\callbacks\early_stopping.py", line 96, in on_iteration_end
    train_loss = self.metric(
                 ^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\utils\metric.py", line 408, in __call__
    return self.metric(y_true, y_predicted, sample_weight=sample_weight)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\utils\metric.py", line 24, in logloss
    ll = log_loss(y_true, y_predicted.astype(np.float32), sample_weight=sample_weight)
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\utils\_param_validation.py", line 213, in wrapper
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\metrics\_classification.py", line 2968, in log_loss
    raise ValueError(
ValueError: y_true and y_pred contain different number of classes 30, 2. Please provide the true labels explicitly through the labels argument. Classes found in y_true: [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
 24 25 26 27 28 29]


Please set a GitHub issue with above error message at: https://github.com/mljar/mljar-supervised/issues/new

## Error for 15_LightGBM

y_true and y_pred contain different number of classes 30, 2. Please provide the true labels explicitly through the labels argument. Classes found in y_true: [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
 24 25 26 27 28 29]
Traceback (most recent call last):
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\base_automl.py", line 1183, in _fit
    trained = self.train_model(params)
              ^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\base_automl.py", line 388, in train_model
    mf.train(results_path, model_subpath)
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\model_framework.py", line 265, in train
    self.callbacks.on_iteration_end(
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\callbacks\callback_list.py", line 23, in on_iteration_end
    cb.on_iteration_end(logs, predictions)
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\callbacks\early_stopping.py", line 96, in on_iteration_end
    train_loss = self.metric(
                 ^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\utils\metric.py", line 408, in __call__
    return self.metric(y_true, y_predicted, sample_weight=sample_weight)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\utils\metric.py", line 24, in logloss
    ll = log_loss(y_true, y_predicted.astype(np.float32), sample_weight=sample_weight)
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\utils\_param_validation.py", line 213, in wrapper
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\metrics\_classification.py", line 2968, in log_loss
    raise ValueError(
ValueError: y_true and y_pred contain different number of classes 30, 2. Please provide the true labels explicitly through the labels argument. Classes found in y_true: [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
 24 25 26 27 28 29]


Please set a GitHub issue with above error message at: https://github.com/mljar/mljar-supervised/issues/new

## Error for 6_Xgboost

[17:09:00] C:\actions-runner\_work\xgboost\xgboost\src\objective\./regression_loss.h:69: Check failed: base_score > 0.0f && base_score < 1.0f: base_score must be in (0,1) for logistic loss, got: 14.5
Traceback (most recent call last):
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\base_automl.py", line 1183, in _fit
    trained = self.train_model(params)
              ^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\base_automl.py", line 388, in train_model
    mf.train(results_path, model_subpath)
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\model_framework.py", line 249, in train
    learner.fit(
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\algorithms\xgboost.py", line 201, in fit
    self.model = xgb.train(
                 ^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\xgboost\core.py", line 729, in inner_f
    return func(**kwargs)
           ^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\xgboost\training.py", line 183, in train
    bst.update(dtrain, iteration=i, fobj=obj)
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\xgboost\core.py", line 2246, in update
    _check_call(
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\xgboost\core.py", line 310, in _check_call
    raise XGBoostError(py_str(_LIB.XGBGetLastError()))
xgboost.core.XGBoostError: [17:09:00] C:\actions-runner\_work\xgboost\xgboost\src\objective\./regression_loss.h:69: Check failed: base_score > 0.0f && base_score < 1.0f: base_score must be in (0,1) for logistic loss, got: 14.5


Please set a GitHub issue with above error message at: https://github.com/mljar/mljar-supervised/issues/new

## Error for 24_CatBoost

catboost/private/libs/target/target_converter.cpp:410: Target with classes must contain only 2 unique values for binary classification
Traceback (most recent call last):
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\base_automl.py", line 1183, in _fit
    trained = self.train_model(params)
              ^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\base_automl.py", line 388, in train_model
    mf.train(results_path, model_subpath)
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\model_framework.py", line 249, in train
    learner.fit(
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\algorithms\catboost.py", line 225, in fit
    self.model.fit(
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\catboost\core.py", line 5245, in fit
    self._fit(X, y, cat_features, text_features, embedding_features, None, graph, sample_weight, None, None, None, None, baseline, use_best_model,
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\catboost\core.py", line 2410, in _fit
    self._train(
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\catboost\core.py", line 1790, in _train
    self._object._train(train_pool, test_pool, params, allow_clear_pool, init_model._object if init_model else None)
  File "_catboost.pyx", line 5017, in _catboost._CatBoost._train
  File "_catboost.pyx", line 5066, in _catboost._CatBoost._train
_catboost.CatBoostError: catboost/private/libs/target/target_converter.cpp:410: Target with classes must contain only 2 unique values for binary classification


Please set a GitHub issue with above error message at: https://github.com/mljar/mljar-supervised/issues/new

## Error for 33_RandomForest

y_true and y_pred contain different number of classes 30, 2. Please provide the true labels explicitly through the labels argument. Classes found in y_true: [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
 24 25 26 27 28 29]
Traceback (most recent call last):
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\base_automl.py", line 1183, in _fit
    trained = self.train_model(params)
              ^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\base_automl.py", line 388, in train_model
    mf.train(results_path, model_subpath)
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\model_framework.py", line 249, in train
    learner.fit(
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\algorithms\sklearn.py", line 143, in fit
    tr = self.log_metric(
         ^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\utils\metric.py", line 408, in __call__
    return self.metric(y_true, y_predicted, sample_weight=sample_weight)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\utils\metric.py", line 24, in logloss
    ll = log_loss(y_true, y_predicted.astype(np.float32), sample_weight=sample_weight)
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\utils\_param_validation.py", line 213, in wrapper
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\metrics\_classification.py", line 2968, in log_loss
    raise ValueError(
ValueError: y_true and y_pred contain different number of classes 30, 2. Please provide the true labels explicitly through the labels argument. Classes found in y_true: [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
 24 25 26 27 28 29]


Please set a GitHub issue with above error message at: https://github.com/mljar/mljar-supervised/issues/new

## Error for 42_ExtraTrees

y_true and y_pred contain different number of classes 30, 2. Please provide the true labels explicitly through the labels argument. Classes found in y_true: [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
 24 25 26 27 28 29]
Traceback (most recent call last):
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\base_automl.py", line 1183, in _fit
    trained = self.train_model(params)
              ^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\base_automl.py", line 388, in train_model
    mf.train(results_path, model_subpath)
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\model_framework.py", line 249, in train
    learner.fit(
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\algorithms\sklearn.py", line 143, in fit
    tr = self.log_metric(
         ^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\utils\metric.py", line 408, in __call__
    return self.metric(y_true, y_predicted, sample_weight=sample_weight)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\utils\metric.py", line 24, in logloss
    ll = log_loss(y_true, y_predicted.astype(np.float32), sample_weight=sample_weight)
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\utils\_param_validation.py", line 213, in wrapper
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\metrics\_classification.py", line 2968, in log_loss
    raise ValueError(
ValueError: y_true and y_pred contain different number of classes 30, 2. Please provide the true labels explicitly through the labels argument. Classes found in y_true: [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
 24 25 26 27 28 29]


Please set a GitHub issue with above error message at: https://github.com/mljar/mljar-supervised/issues/new

## Error for 51_NeuralNetwork

y_true and y_pred contain different number of classes 30, 2. Please provide the true labels explicitly through the labels argument. Classes found in y_true: [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
 24 25 26 27 28 29]
Traceback (most recent call last):
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\base_automl.py", line 1183, in _fit
    trained = self.train_model(params)
              ^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\base_automl.py", line 388, in train_model
    mf.train(results_path, model_subpath)
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\model_framework.py", line 265, in train
    self.callbacks.on_iteration_end(
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\callbacks\callback_list.py", line 23, in on_iteration_end
    cb.on_iteration_end(logs, predictions)
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\callbacks\early_stopping.py", line 96, in on_iteration_end
    train_loss = self.metric(
                 ^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\utils\metric.py", line 408, in __call__
    return self.metric(y_true, y_predicted, sample_weight=sample_weight)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\utils\metric.py", line 24, in logloss
    ll = log_loss(y_true, y_predicted.astype(np.float32), sample_weight=sample_weight)
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\utils\_param_validation.py", line 213, in wrapper
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\metrics\_classification.py", line 2968, in log_loss
    raise ValueError(
ValueError: y_true and y_pred contain different number of classes 30, 2. Please provide the true labels explicitly through the labels argument. Classes found in y_true: [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
 24 25 26 27 28 29]


Please set a GitHub issue with above error message at: https://github.com/mljar/mljar-supervised/issues/new

## Error for 60_NearestNeighbors

y_true and y_pred contain different number of classes 30, 2. Please provide the true labels explicitly through the labels argument. Classes found in y_true: [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
 24 25 26 27 28 29]
Traceback (most recent call last):
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\base_automl.py", line 1183, in _fit
    trained = self.train_model(params)
              ^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\base_automl.py", line 388, in train_model
    mf.train(results_path, model_subpath)
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\model_framework.py", line 265, in train
    self.callbacks.on_iteration_end(
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\callbacks\callback_list.py", line 23, in on_iteration_end
    cb.on_iteration_end(logs, predictions)
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\callbacks\early_stopping.py", line 96, in on_iteration_end
    train_loss = self.metric(
                 ^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\utils\metric.py", line 408, in __call__
    return self.metric(y_true, y_predicted, sample_weight=sample_weight)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\utils\metric.py", line 24, in logloss
    ll = log_loss(y_true, y_predicted.astype(np.float32), sample_weight=sample_weight)
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\utils\_param_validation.py", line 213, in wrapper
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\metrics\_classification.py", line 2968, in log_loss
    raise ValueError(
ValueError: y_true and y_pred contain different number of classes 30, 2. Please provide the true labels explicitly through the labels argument. Classes found in y_true: [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
 24 25 26 27 28 29]


Please set a GitHub issue with above error message at: https://github.com/mljar/mljar-supervised/issues/new

## Error for 16_LightGBM

y_true and y_pred contain different number of classes 30, 2. Please provide the true labels explicitly through the labels argument. Classes found in y_true: [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
 24 25 26 27 28 29]
Traceback (most recent call last):
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\base_automl.py", line 1183, in _fit
    trained = self.train_model(params)
              ^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\base_automl.py", line 388, in train_model
    mf.train(results_path, model_subpath)
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\model_framework.py", line 265, in train
    self.callbacks.on_iteration_end(
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\callbacks\callback_list.py", line 23, in on_iteration_end
    cb.on_iteration_end(logs, predictions)
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\callbacks\early_stopping.py", line 96, in on_iteration_end
    train_loss = self.metric(
                 ^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\utils\metric.py", line 408, in __call__
    return self.metric(y_true, y_predicted, sample_weight=sample_weight)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\utils\metric.py", line 24, in logloss
    ll = log_loss(y_true, y_predicted.astype(np.float32), sample_weight=sample_weight)
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\utils\_param_validation.py", line 213, in wrapper
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\metrics\_classification.py", line 2968, in log_loss
    raise ValueError(
ValueError: y_true and y_pred contain different number of classes 30, 2. Please provide the true labels explicitly through the labels argument. Classes found in y_true: [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
 24 25 26 27 28 29]


Please set a GitHub issue with above error message at: https://github.com/mljar/mljar-supervised/issues/new

## Error for 7_Xgboost

[17:09:02] C:\actions-runner\_work\xgboost\xgboost\src\objective\./regression_loss.h:69: Check failed: base_score > 0.0f && base_score < 1.0f: base_score must be in (0,1) for logistic loss, got: 14.5
Traceback (most recent call last):
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\base_automl.py", line 1183, in _fit
    trained = self.train_model(params)
              ^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\base_automl.py", line 388, in train_model
    mf.train(results_path, model_subpath)
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\model_framework.py", line 249, in train
    learner.fit(
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\algorithms\xgboost.py", line 201, in fit
    self.model = xgb.train(
                 ^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\xgboost\core.py", line 729, in inner_f
    return func(**kwargs)
           ^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\xgboost\training.py", line 183, in train
    bst.update(dtrain, iteration=i, fobj=obj)
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\xgboost\core.py", line 2246, in update
    _check_call(
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\xgboost\core.py", line 310, in _check_call
    raise XGBoostError(py_str(_LIB.XGBGetLastError()))
xgboost.core.XGBoostError: [17:09:02] C:\actions-runner\_work\xgboost\xgboost\src\objective\./regression_loss.h:69: Check failed: base_score > 0.0f && base_score < 1.0f: base_score must be in (0,1) for logistic loss, got: 14.5


Please set a GitHub issue with above error message at: https://github.com/mljar/mljar-supervised/issues/new

## Error for 25_CatBoost

catboost/private/libs/target/target_converter.cpp:410: Target with classes must contain only 2 unique values for binary classification
Traceback (most recent call last):
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\base_automl.py", line 1183, in _fit
    trained = self.train_model(params)
              ^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\base_automl.py", line 388, in train_model
    mf.train(results_path, model_subpath)
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\model_framework.py", line 249, in train
    learner.fit(
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\algorithms\catboost.py", line 225, in fit
    self.model.fit(
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\catboost\core.py", line 5245, in fit
    self._fit(X, y, cat_features, text_features, embedding_features, None, graph, sample_weight, None, None, None, None, baseline, use_best_model,
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\catboost\core.py", line 2410, in _fit
    self._train(
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\catboost\core.py", line 1790, in _train
    self._object._train(train_pool, test_pool, params, allow_clear_pool, init_model._object if init_model else None)
  File "_catboost.pyx", line 5017, in _catboost._CatBoost._train
  File "_catboost.pyx", line 5066, in _catboost._CatBoost._train
_catboost.CatBoostError: catboost/private/libs/target/target_converter.cpp:410: Target with classes must contain only 2 unique values for binary classification


Please set a GitHub issue with above error message at: https://github.com/mljar/mljar-supervised/issues/new

## Error for 34_RandomForest

y_true and y_pred contain different number of classes 30, 2. Please provide the true labels explicitly through the labels argument. Classes found in y_true: [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
 24 25 26 27 28 29]
Traceback (most recent call last):
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\base_automl.py", line 1183, in _fit
    trained = self.train_model(params)
              ^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\base_automl.py", line 388, in train_model
    mf.train(results_path, model_subpath)
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\model_framework.py", line 249, in train
    learner.fit(
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\algorithms\sklearn.py", line 143, in fit
    tr = self.log_metric(
         ^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\utils\metric.py", line 408, in __call__
    return self.metric(y_true, y_predicted, sample_weight=sample_weight)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\utils\metric.py", line 24, in logloss
    ll = log_loss(y_true, y_predicted.astype(np.float32), sample_weight=sample_weight)
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\utils\_param_validation.py", line 213, in wrapper
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\metrics\_classification.py", line 2968, in log_loss
    raise ValueError(
ValueError: y_true and y_pred contain different number of classes 30, 2. Please provide the true labels explicitly through the labels argument. Classes found in y_true: [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
 24 25 26 27 28 29]


Please set a GitHub issue with above error message at: https://github.com/mljar/mljar-supervised/issues/new

## Error for 43_ExtraTrees

y_true and y_pred contain different number of classes 30, 2. Please provide the true labels explicitly through the labels argument. Classes found in y_true: [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
 24 25 26 27 28 29]
Traceback (most recent call last):
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\base_automl.py", line 1183, in _fit
    trained = self.train_model(params)
              ^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\base_automl.py", line 388, in train_model
    mf.train(results_path, model_subpath)
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\model_framework.py", line 249, in train
    learner.fit(
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\algorithms\sklearn.py", line 143, in fit
    tr = self.log_metric(
         ^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\utils\metric.py", line 408, in __call__
    return self.metric(y_true, y_predicted, sample_weight=sample_weight)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\utils\metric.py", line 24, in logloss
    ll = log_loss(y_true, y_predicted.astype(np.float32), sample_weight=sample_weight)
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\utils\_param_validation.py", line 213, in wrapper
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\metrics\_classification.py", line 2968, in log_loss
    raise ValueError(
ValueError: y_true and y_pred contain different number of classes 30, 2. Please provide the true labels explicitly through the labels argument. Classes found in y_true: [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
 24 25 26 27 28 29]


Please set a GitHub issue with above error message at: https://github.com/mljar/mljar-supervised/issues/new

## Error for 52_NeuralNetwork

y_true and y_pred contain different number of classes 30, 2. Please provide the true labels explicitly through the labels argument. Classes found in y_true: [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
 24 25 26 27 28 29]
Traceback (most recent call last):
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\base_automl.py", line 1183, in _fit
    trained = self.train_model(params)
              ^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\base_automl.py", line 388, in train_model
    mf.train(results_path, model_subpath)
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\model_framework.py", line 265, in train
    self.callbacks.on_iteration_end(
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\callbacks\callback_list.py", line 23, in on_iteration_end
    cb.on_iteration_end(logs, predictions)
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\callbacks\early_stopping.py", line 96, in on_iteration_end
    train_loss = self.metric(
                 ^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\utils\metric.py", line 408, in __call__
    return self.metric(y_true, y_predicted, sample_weight=sample_weight)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\utils\metric.py", line 24, in logloss
    ll = log_loss(y_true, y_predicted.astype(np.float32), sample_weight=sample_weight)
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\utils\_param_validation.py", line 213, in wrapper
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\metrics\_classification.py", line 2968, in log_loss
    raise ValueError(
ValueError: y_true and y_pred contain different number of classes 30, 2. Please provide the true labels explicitly through the labels argument. Classes found in y_true: [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
 24 25 26 27 28 29]


Please set a GitHub issue with above error message at: https://github.com/mljar/mljar-supervised/issues/new

## Error for 61_NearestNeighbors

y_true and y_pred contain different number of classes 30, 2. Please provide the true labels explicitly through the labels argument. Classes found in y_true: [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
 24 25 26 27 28 29]
Traceback (most recent call last):
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\base_automl.py", line 1183, in _fit
    trained = self.train_model(params)
              ^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\base_automl.py", line 388, in train_model
    mf.train(results_path, model_subpath)
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\model_framework.py", line 265, in train
    self.callbacks.on_iteration_end(
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\callbacks\callback_list.py", line 23, in on_iteration_end
    cb.on_iteration_end(logs, predictions)
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\callbacks\early_stopping.py", line 96, in on_iteration_end
    train_loss = self.metric(
                 ^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\utils\metric.py", line 408, in __call__
    return self.metric(y_true, y_predicted, sample_weight=sample_weight)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\utils\metric.py", line 24, in logloss
    ll = log_loss(y_true, y_predicted.astype(np.float32), sample_weight=sample_weight)
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\utils\_param_validation.py", line 213, in wrapper
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\metrics\_classification.py", line 2968, in log_loss
    raise ValueError(
ValueError: y_true and y_pred contain different number of classes 30, 2. Please provide the true labels explicitly through the labels argument. Classes found in y_true: [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
 24 25 26 27 28 29]


Please set a GitHub issue with above error message at: https://github.com/mljar/mljar-supervised/issues/new

## Error for 17_LightGBM

y_true and y_pred contain different number of classes 30, 2. Please provide the true labels explicitly through the labels argument. Classes found in y_true: [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
 24 25 26 27 28 29]
Traceback (most recent call last):
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\base_automl.py", line 1183, in _fit
    trained = self.train_model(params)
              ^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\base_automl.py", line 388, in train_model
    mf.train(results_path, model_subpath)
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\model_framework.py", line 265, in train
    self.callbacks.on_iteration_end(
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\callbacks\callback_list.py", line 23, in on_iteration_end
    cb.on_iteration_end(logs, predictions)
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\callbacks\early_stopping.py", line 96, in on_iteration_end
    train_loss = self.metric(
                 ^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\utils\metric.py", line 408, in __call__
    return self.metric(y_true, y_predicted, sample_weight=sample_weight)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\utils\metric.py", line 24, in logloss
    ll = log_loss(y_true, y_predicted.astype(np.float32), sample_weight=sample_weight)
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\utils\_param_validation.py", line 213, in wrapper
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\metrics\_classification.py", line 2968, in log_loss
    raise ValueError(
ValueError: y_true and y_pred contain different number of classes 30, 2. Please provide the true labels explicitly through the labels argument. Classes found in y_true: [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
 24 25 26 27 28 29]


Please set a GitHub issue with above error message at: https://github.com/mljar/mljar-supervised/issues/new

## Error for 8_Xgboost

[17:09:03] C:\actions-runner\_work\xgboost\xgboost\src\objective\./regression_loss.h:69: Check failed: base_score > 0.0f && base_score < 1.0f: base_score must be in (0,1) for logistic loss, got: 14.5
Traceback (most recent call last):
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\base_automl.py", line 1183, in _fit
    trained = self.train_model(params)
              ^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\base_automl.py", line 388, in train_model
    mf.train(results_path, model_subpath)
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\model_framework.py", line 249, in train
    learner.fit(
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\algorithms\xgboost.py", line 201, in fit
    self.model = xgb.train(
                 ^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\xgboost\core.py", line 729, in inner_f
    return func(**kwargs)
           ^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\xgboost\training.py", line 183, in train
    bst.update(dtrain, iteration=i, fobj=obj)
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\xgboost\core.py", line 2246, in update
    _check_call(
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\xgboost\core.py", line 310, in _check_call
    raise XGBoostError(py_str(_LIB.XGBGetLastError()))
xgboost.core.XGBoostError: [17:09:03] C:\actions-runner\_work\xgboost\xgboost\src\objective\./regression_loss.h:69: Check failed: base_score > 0.0f && base_score < 1.0f: base_score must be in (0,1) for logistic loss, got: 14.5


Please set a GitHub issue with above error message at: https://github.com/mljar/mljar-supervised/issues/new

## Error for 26_CatBoost

catboost/private/libs/target/target_converter.cpp:410: Target with classes must contain only 2 unique values for binary classification
Traceback (most recent call last):
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\base_automl.py", line 1183, in _fit
    trained = self.train_model(params)
              ^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\base_automl.py", line 388, in train_model
    mf.train(results_path, model_subpath)
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\model_framework.py", line 249, in train
    learner.fit(
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\algorithms\catboost.py", line 225, in fit
    self.model.fit(
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\catboost\core.py", line 5245, in fit
    self._fit(X, y, cat_features, text_features, embedding_features, None, graph, sample_weight, None, None, None, None, baseline, use_best_model,
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\catboost\core.py", line 2410, in _fit
    self._train(
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\catboost\core.py", line 1790, in _train
    self._object._train(train_pool, test_pool, params, allow_clear_pool, init_model._object if init_model else None)
  File "_catboost.pyx", line 5017, in _catboost._CatBoost._train
  File "_catboost.pyx", line 5066, in _catboost._CatBoost._train
_catboost.CatBoostError: catboost/private/libs/target/target_converter.cpp:410: Target with classes must contain only 2 unique values for binary classification


Please set a GitHub issue with above error message at: https://github.com/mljar/mljar-supervised/issues/new

## Error for 35_RandomForest

y_true and y_pred contain different number of classes 30, 2. Please provide the true labels explicitly through the labels argument. Classes found in y_true: [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
 24 25 26 27 28 29]
Traceback (most recent call last):
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\base_automl.py", line 1183, in _fit
    trained = self.train_model(params)
              ^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\base_automl.py", line 388, in train_model
    mf.train(results_path, model_subpath)
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\model_framework.py", line 249, in train
    learner.fit(
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\algorithms\sklearn.py", line 143, in fit
    tr = self.log_metric(
         ^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\utils\metric.py", line 408, in __call__
    return self.metric(y_true, y_predicted, sample_weight=sample_weight)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\utils\metric.py", line 24, in logloss
    ll = log_loss(y_true, y_predicted.astype(np.float32), sample_weight=sample_weight)
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\utils\_param_validation.py", line 213, in wrapper
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\metrics\_classification.py", line 2968, in log_loss
    raise ValueError(
ValueError: y_true and y_pred contain different number of classes 30, 2. Please provide the true labels explicitly through the labels argument. Classes found in y_true: [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
 24 25 26 27 28 29]


Please set a GitHub issue with above error message at: https://github.com/mljar/mljar-supervised/issues/new

## Error for 44_ExtraTrees

y_true and y_pred contain different number of classes 30, 2. Please provide the true labels explicitly through the labels argument. Classes found in y_true: [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
 24 25 26 27 28 29]
Traceback (most recent call last):
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\base_automl.py", line 1183, in _fit
    trained = self.train_model(params)
              ^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\base_automl.py", line 388, in train_model
    mf.train(results_path, model_subpath)
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\model_framework.py", line 249, in train
    learner.fit(
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\algorithms\sklearn.py", line 143, in fit
    tr = self.log_metric(
         ^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\utils\metric.py", line 408, in __call__
    return self.metric(y_true, y_predicted, sample_weight=sample_weight)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\utils\metric.py", line 24, in logloss
    ll = log_loss(y_true, y_predicted.astype(np.float32), sample_weight=sample_weight)
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\utils\_param_validation.py", line 213, in wrapper
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\metrics\_classification.py", line 2968, in log_loss
    raise ValueError(
ValueError: y_true and y_pred contain different number of classes 30, 2. Please provide the true labels explicitly through the labels argument. Classes found in y_true: [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
 24 25 26 27 28 29]


Please set a GitHub issue with above error message at: https://github.com/mljar/mljar-supervised/issues/new

## Error for 53_NeuralNetwork

y_true and y_pred contain different number of classes 30, 2. Please provide the true labels explicitly through the labels argument. Classes found in y_true: [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
 24 25 26 27 28 29]
Traceback (most recent call last):
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\base_automl.py", line 1183, in _fit
    trained = self.train_model(params)
              ^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\base_automl.py", line 388, in train_model
    mf.train(results_path, model_subpath)
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\model_framework.py", line 265, in train
    self.callbacks.on_iteration_end(
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\callbacks\callback_list.py", line 23, in on_iteration_end
    cb.on_iteration_end(logs, predictions)
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\callbacks\early_stopping.py", line 96, in on_iteration_end
    train_loss = self.metric(
                 ^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\utils\metric.py", line 408, in __call__
    return self.metric(y_true, y_predicted, sample_weight=sample_weight)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\utils\metric.py", line 24, in logloss
    ll = log_loss(y_true, y_predicted.astype(np.float32), sample_weight=sample_weight)
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\utils\_param_validation.py", line 213, in wrapper
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\metrics\_classification.py", line 2968, in log_loss
    raise ValueError(
ValueError: y_true and y_pred contain different number of classes 30, 2. Please provide the true labels explicitly through the labels argument. Classes found in y_true: [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
 24 25 26 27 28 29]


Please set a GitHub issue with above error message at: https://github.com/mljar/mljar-supervised/issues/new

## Error for 62_NearestNeighbors

y_true and y_pred contain different number of classes 30, 2. Please provide the true labels explicitly through the labels argument. Classes found in y_true: [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
 24 25 26 27 28 29]
Traceback (most recent call last):
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\base_automl.py", line 1183, in _fit
    trained = self.train_model(params)
              ^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\base_automl.py", line 388, in train_model
    mf.train(results_path, model_subpath)
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\model_framework.py", line 265, in train
    self.callbacks.on_iteration_end(
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\callbacks\callback_list.py", line 23, in on_iteration_end
    cb.on_iteration_end(logs, predictions)
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\callbacks\early_stopping.py", line 96, in on_iteration_end
    train_loss = self.metric(
                 ^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\utils\metric.py", line 408, in __call__
    return self.metric(y_true, y_predicted, sample_weight=sample_weight)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\utils\metric.py", line 24, in logloss
    ll = log_loss(y_true, y_predicted.astype(np.float32), sample_weight=sample_weight)
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\utils\_param_validation.py", line 213, in wrapper
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\metrics\_classification.py", line 2968, in log_loss
    raise ValueError(
ValueError: y_true and y_pred contain different number of classes 30, 2. Please provide the true labels explicitly through the labels argument. Classes found in y_true: [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
 24 25 26 27 28 29]


Please set a GitHub issue with above error message at: https://github.com/mljar/mljar-supervised/issues/new

## Error for 18_LightGBM

y_true and y_pred contain different number of classes 30, 2. Please provide the true labels explicitly through the labels argument. Classes found in y_true: [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
 24 25 26 27 28 29]
Traceback (most recent call last):
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\base_automl.py", line 1183, in _fit
    trained = self.train_model(params)
              ^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\base_automl.py", line 388, in train_model
    mf.train(results_path, model_subpath)
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\model_framework.py", line 265, in train
    self.callbacks.on_iteration_end(
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\callbacks\callback_list.py", line 23, in on_iteration_end
    cb.on_iteration_end(logs, predictions)
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\callbacks\early_stopping.py", line 96, in on_iteration_end
    train_loss = self.metric(
                 ^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\utils\metric.py", line 408, in __call__
    return self.metric(y_true, y_predicted, sample_weight=sample_weight)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\utils\metric.py", line 24, in logloss
    ll = log_loss(y_true, y_predicted.astype(np.float32), sample_weight=sample_weight)
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\utils\_param_validation.py", line 213, in wrapper
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\metrics\_classification.py", line 2968, in log_loss
    raise ValueError(
ValueError: y_true and y_pred contain different number of classes 30, 2. Please provide the true labels explicitly through the labels argument. Classes found in y_true: [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
 24 25 26 27 28 29]


Please set a GitHub issue with above error message at: https://github.com/mljar/mljar-supervised/issues/new

## Error for 9_Xgboost

[17:09:04] C:\actions-runner\_work\xgboost\xgboost\src\objective\./regression_loss.h:69: Check failed: base_score > 0.0f && base_score < 1.0f: base_score must be in (0,1) for logistic loss, got: 14.5
Traceback (most recent call last):
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\base_automl.py", line 1183, in _fit
    trained = self.train_model(params)
              ^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\base_automl.py", line 388, in train_model
    mf.train(results_path, model_subpath)
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\model_framework.py", line 249, in train
    learner.fit(
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\algorithms\xgboost.py", line 201, in fit
    self.model = xgb.train(
                 ^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\xgboost\core.py", line 729, in inner_f
    return func(**kwargs)
           ^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\xgboost\training.py", line 183, in train
    bst.update(dtrain, iteration=i, fobj=obj)
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\xgboost\core.py", line 2246, in update
    _check_call(
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\xgboost\core.py", line 310, in _check_call
    raise XGBoostError(py_str(_LIB.XGBGetLastError()))
xgboost.core.XGBoostError: [17:09:04] C:\actions-runner\_work\xgboost\xgboost\src\objective\./regression_loss.h:69: Check failed: base_score > 0.0f && base_score < 1.0f: base_score must be in (0,1) for logistic loss, got: 14.5


Please set a GitHub issue with above error message at: https://github.com/mljar/mljar-supervised/issues/new

## Error for 27_CatBoost

catboost/private/libs/target/target_converter.cpp:410: Target with classes must contain only 2 unique values for binary classification
Traceback (most recent call last):
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\base_automl.py", line 1183, in _fit
    trained = self.train_model(params)
              ^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\base_automl.py", line 388, in train_model
    mf.train(results_path, model_subpath)
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\model_framework.py", line 249, in train
    learner.fit(
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\algorithms\catboost.py", line 225, in fit
    self.model.fit(
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\catboost\core.py", line 5245, in fit
    self._fit(X, y, cat_features, text_features, embedding_features, None, graph, sample_weight, None, None, None, None, baseline, use_best_model,
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\catboost\core.py", line 2410, in _fit
    self._train(
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\catboost\core.py", line 1790, in _train
    self._object._train(train_pool, test_pool, params, allow_clear_pool, init_model._object if init_model else None)
  File "_catboost.pyx", line 5017, in _catboost._CatBoost._train
  File "_catboost.pyx", line 5066, in _catboost._CatBoost._train
_catboost.CatBoostError: catboost/private/libs/target/target_converter.cpp:410: Target with classes must contain only 2 unique values for binary classification


Please set a GitHub issue with above error message at: https://github.com/mljar/mljar-supervised/issues/new

## Error for 36_RandomForest

y_true and y_pred contain different number of classes 30, 2. Please provide the true labels explicitly through the labels argument. Classes found in y_true: [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
 24 25 26 27 28 29]
Traceback (most recent call last):
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\base_automl.py", line 1183, in _fit
    trained = self.train_model(params)
              ^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\base_automl.py", line 388, in train_model
    mf.train(results_path, model_subpath)
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\model_framework.py", line 249, in train
    learner.fit(
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\algorithms\sklearn.py", line 143, in fit
    tr = self.log_metric(
         ^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\utils\metric.py", line 408, in __call__
    return self.metric(y_true, y_predicted, sample_weight=sample_weight)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\utils\metric.py", line 24, in logloss
    ll = log_loss(y_true, y_predicted.astype(np.float32), sample_weight=sample_weight)
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\utils\_param_validation.py", line 213, in wrapper
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\metrics\_classification.py", line 2968, in log_loss
    raise ValueError(
ValueError: y_true and y_pred contain different number of classes 30, 2. Please provide the true labels explicitly through the labels argument. Classes found in y_true: [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
 24 25 26 27 28 29]


Please set a GitHub issue with above error message at: https://github.com/mljar/mljar-supervised/issues/new

## Error for 45_ExtraTrees

y_true and y_pred contain different number of classes 30, 2. Please provide the true labels explicitly through the labels argument. Classes found in y_true: [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
 24 25 26 27 28 29]
Traceback (most recent call last):
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\base_automl.py", line 1183, in _fit
    trained = self.train_model(params)
              ^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\base_automl.py", line 388, in train_model
    mf.train(results_path, model_subpath)
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\model_framework.py", line 249, in train
    learner.fit(
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\algorithms\sklearn.py", line 143, in fit
    tr = self.log_metric(
         ^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\utils\metric.py", line 408, in __call__
    return self.metric(y_true, y_predicted, sample_weight=sample_weight)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\utils\metric.py", line 24, in logloss
    ll = log_loss(y_true, y_predicted.astype(np.float32), sample_weight=sample_weight)
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\utils\_param_validation.py", line 213, in wrapper
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\metrics\_classification.py", line 2968, in log_loss
    raise ValueError(
ValueError: y_true and y_pred contain different number of classes 30, 2. Please provide the true labels explicitly through the labels argument. Classes found in y_true: [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
 24 25 26 27 28 29]


Please set a GitHub issue with above error message at: https://github.com/mljar/mljar-supervised/issues/new

## Error for 54_NeuralNetwork

y_true and y_pred contain different number of classes 30, 2. Please provide the true labels explicitly through the labels argument. Classes found in y_true: [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
 24 25 26 27 28 29]
Traceback (most recent call last):
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\base_automl.py", line 1183, in _fit
    trained = self.train_model(params)
              ^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\base_automl.py", line 388, in train_model
    mf.train(results_path, model_subpath)
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\model_framework.py", line 265, in train
    self.callbacks.on_iteration_end(
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\callbacks\callback_list.py", line 23, in on_iteration_end
    cb.on_iteration_end(logs, predictions)
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\callbacks\early_stopping.py", line 96, in on_iteration_end
    train_loss = self.metric(
                 ^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\utils\metric.py", line 408, in __call__
    return self.metric(y_true, y_predicted, sample_weight=sample_weight)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\utils\metric.py", line 24, in logloss
    ll = log_loss(y_true, y_predicted.astype(np.float32), sample_weight=sample_weight)
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\utils\_param_validation.py", line 213, in wrapper
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\metrics\_classification.py", line 2968, in log_loss
    raise ValueError(
ValueError: y_true and y_pred contain different number of classes 30, 2. Please provide the true labels explicitly through the labels argument. Classes found in y_true: [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
 24 25 26 27 28 29]


Please set a GitHub issue with above error message at: https://github.com/mljar/mljar-supervised/issues/new

## Error for 63_NearestNeighbors

y_true and y_pred contain different number of classes 30, 2. Please provide the true labels explicitly through the labels argument. Classes found in y_true: [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
 24 25 26 27 28 29]
Traceback (most recent call last):
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\base_automl.py", line 1183, in _fit
    trained = self.train_model(params)
              ^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\base_automl.py", line 388, in train_model
    mf.train(results_path, model_subpath)
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\model_framework.py", line 265, in train
    self.callbacks.on_iteration_end(
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\callbacks\callback_list.py", line 23, in on_iteration_end
    cb.on_iteration_end(logs, predictions)
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\callbacks\early_stopping.py", line 96, in on_iteration_end
    train_loss = self.metric(
                 ^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\utils\metric.py", line 408, in __call__
    return self.metric(y_true, y_predicted, sample_weight=sample_weight)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\utils\metric.py", line 24, in logloss
    ll = log_loss(y_true, y_predicted.astype(np.float32), sample_weight=sample_weight)
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\utils\_param_validation.py", line 213, in wrapper
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\metrics\_classification.py", line 2968, in log_loss
    raise ValueError(
ValueError: y_true and y_pred contain different number of classes 30, 2. Please provide the true labels explicitly through the labels argument. Classes found in y_true: [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
 24 25 26 27 28 29]


Please set a GitHub issue with above error message at: https://github.com/mljar/mljar-supervised/issues/new

