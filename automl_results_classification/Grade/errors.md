## Error for 1_DecisionTree

[Errno 2] No such file or directory: 'C:\\Users\\lenovo\\OneDrive\\Desktop\\AutoModel\\automl_results_classification\\Grade\\1_DecisionTree\\learning_curves.png'
Traceback (most recent call last):
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\base_automl.py", line 1183, in _fit
    trained = self.train_model(params)
              ^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\base_automl.py", line 394, in train_model
    mf.save(results_path, model_subpath)
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\model_framework.py", line 639, in save
    LearningCurves.plot(
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\utils\learning_curves.py", line 42, in plot
    LearningCurves.plot_single_iter(
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\utils\learning_curves.py", line 73, in plot_single_iter
    plt.savefig(plot_path)
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\matplotlib\pyplot.py", line 1023, in savefig
    res = fig.savefig(*args, **kwargs)
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\matplotlib\figure.py", line 3378, in savefig
    self.canvas.print_figure(fname, **kwargs)
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\matplotlib\backend_bases.py", line 2366, in print_figure
    result = print_method(
             ^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\matplotlib\backend_bases.py", line 2232, in <lambda>
    print_method = functools.wraps(meth)(lambda *args, **kwargs: meth(
                                                                 ^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\matplotlib\backends\backend_agg.py", line 509, in print_png
    self._print_pil(filename_or_obj, "png", pil_kwargs, metadata)
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\matplotlib\backends\backend_agg.py", line 458, in _print_pil
    mpl.image.imsave(
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\matplotlib\image.py", line 1689, in imsave
    image.save(fname, **pil_kwargs)
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\PIL\Image.py", line 2600, in save
    fp = builtins.open(filename, "w+b")
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
FileNotFoundError: [Errno 2] No such file or directory: 'C:\\Users\\lenovo\\OneDrive\\Desktop\\AutoModel\\automl_results_classification\\Grade\\1_DecisionTree\\learning_curves.png'


Please set a GitHub issue with above error message at: https://github.com/mljar/mljar-supervised/issues/new

## Error for 5_Default_LightGBM

Cannot save file into a non-existent directory: 'automl_results_classification\Grade\5_Default_LightGBM'
Traceback (most recent call last):
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\base_automl.py", line 1183, in _fit
    trained = self.train_model(params)
              ^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\base_automl.py", line 394, in train_model
    mf.save(results_path, model_subpath)
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\model_framework.py", line 606, in save
    predictions.to_csv(self._oof_predictions_fname, index=False)
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\pandas\core\generic.py", line 3902, in to_csv
    return DataFrameRenderer(formatter).to_csv(
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\pandas\io\formats\format.py", line 1152, in to_csv
    csv_formatter.save()
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\pandas\io\formats\csvs.py", line 247, in save
    with get_handle(
         ^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\pandas\io\common.py", line 739, in get_handle
    check_parent_directory(str(handle))
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\pandas\io\common.py", line 604, in check_parent_directory
    raise OSError(rf"Cannot save file into a non-existent directory: '{parent}'")
OSError: Cannot save file into a non-existent directory: 'automl_results_classification\Grade\5_Default_LightGBM'


Please set a GitHub issue with above error message at: https://github.com/mljar/mljar-supervised/issues/new

## Error for 23_CatBoost

Cannot save file into a non-existent directory: 'automl_results_classification\Grade\23_CatBoost'
Traceback (most recent call last):
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\base_automl.py", line 1183, in _fit
    trained = self.train_model(params)
              ^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\base_automl.py", line 388, in train_model
    mf.train(results_path, model_subpath)
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\model_framework.py", line 249, in train
    learner.fit(
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\algorithms\catboost.py", line 279, in fit
    result.to_csv(log_to_file, index=False, header=False)
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\pandas\core\generic.py", line 3902, in to_csv
    return DataFrameRenderer(formatter).to_csv(
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\pandas\io\formats\format.py", line 1152, in to_csv
    csv_formatter.save()
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\pandas\io\formats\csvs.py", line 247, in save
    with get_handle(
         ^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\pandas\io\common.py", line 739, in get_handle
    check_parent_directory(str(handle))
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\pandas\io\common.py", line 604, in check_parent_directory
    raise OSError(rf"Cannot save file into a non-existent directory: '{parent}'")
OSError: Cannot save file into a non-existent directory: 'automl_results_classification\Grade\23_CatBoost'


Please set a GitHub issue with above error message at: https://github.com/mljar/mljar-supervised/issues/new

## Error for 14_LightGBM

<matplotlib.backends.backend_agg.RendererAgg object at 0x000002C5423B9AC0>
Traceback (most recent call last):
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\base_automl.py", line 1183, in _fit
    trained = self.train_model(params)
              ^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\base_automl.py", line 391, in train_model
    self.keep_model(mf, model_subpath)
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\base_automl.py", line 304, in keep_model
    self.select_and_save_best()
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\base_automl.py", line 1381, in select_and_save_best
    LeaderboardPlots.compute(
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\utils\leaderboard_plots.py", line 63, in compute
    plt.savefig(plot_path)
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\matplotlib\pyplot.py", line 1023, in savefig
    res = fig.savefig(*args, **kwargs)
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\matplotlib\figure.py", line 3378, in savefig
    self.canvas.print_figure(fname, **kwargs)
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\matplotlib\backend_bases.py", line 2336, in print_figure
    renderer = _get_renderer(
               ^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\matplotlib\backend_bases.py", line 1598, in _get_renderer
    print_method(io.BytesIO())
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\matplotlib\backend_bases.py", line 2232, in <lambda>
    print_method = functools.wraps(meth)(lambda *args, **kwargs: meth(
                                                                 ^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\matplotlib\backends\backend_agg.py", line 509, in print_png
    self._print_pil(filename_or_obj, "png", pil_kwargs, metadata)
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\matplotlib\backends\backend_agg.py", line 457, in _print_pil
    FigureCanvasAgg.draw(self)
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\matplotlib\backends\backend_agg.py", line 400, in draw
    self.figure.draw(self.renderer)
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\matplotlib\backend_bases.py", line 1588, in _draw
    def _draw(renderer): raise Done(renderer)
                         ^^^^^^^^^^^^^^^^^^^^
matplotlib.backend_bases._get_renderer.<locals>.Done: <matplotlib.backends.backend_agg.RendererAgg object at 0x000002C5423B9AC0>


Please set a GitHub issue with above error message at: https://github.com/mljar/mljar-supervised/issues/new

## Error for 5_Default_LightGBM_KMeansFeatures

functools.partial(<function FigureCanvasAgg.print_png at 0x000002C5423AE660>, orientation='portrait') did not call Figure.draw, so no renderer is available
Traceback (most recent call last):
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\base_automl.py", line 1183, in _fit
    trained = self.train_model(params)
              ^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\base_automl.py", line 391, in train_model
    self.keep_model(mf, model_subpath)
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\base_automl.py", line 304, in keep_model
    self.select_and_save_best()
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\base_automl.py", line 1381, in select_and_save_best
    LeaderboardPlots.compute(
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\utils\leaderboard_plots.py", line 63, in compute
    plt.savefig(plot_path)
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\matplotlib\pyplot.py", line 1023, in savefig
    res = fig.savefig(*args, **kwargs)
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\matplotlib\figure.py", line 3378, in savefig
    self.canvas.print_figure(fname, **kwargs)
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\matplotlib\backend_bases.py", line 2336, in print_figure
    renderer = _get_renderer(
               ^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\matplotlib\backend_bases.py", line 1603, in _get_renderer
    raise RuntimeError(f"{print_method} did not call Figure.draw, so "
RuntimeError: functools.partial(<function FigureCanvasAgg.print_png at 0x000002C5423AE660>, orientation='portrait') did not call Figure.draw, so no renderer is available


Please set a GitHub issue with above error message at: https://github.com/mljar/mljar-supervised/issues/new

## Error for 14_LightGBM_BoostOnErrors

Found input variables with inconsistent numbers of samples: [180, 180, 18]
Traceback (most recent call last):
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\base_automl.py", line 1183, in _fit
    trained = self.train_model(params)
              ^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\base_automl.py", line 388, in train_model
    mf.train(results_path, model_subpath)
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\model_framework.py", line 171, in train
    train_data, validation_data = self.validation.get_split(k_fold, repeat)
                                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\validation\validation_step.py", line 28, in get_split
    return self.validator.get_split(k, repeat)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\validation\validator_split.py", line 67, in get_split
    output_data = train_test_split(
                  ^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\utils\_param_validation.py", line 213, in wrapper
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\model_selection\_split.py", line 2782, in train_test_split
    arrays = indexable(*arrays)
             ^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\utils\validation.py", line 514, in indexable
    check_consistent_length(*result)
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\utils\validation.py", line 457, in check_consistent_length
    raise ValueError(
ValueError: Found input variables with inconsistent numbers of samples: [180, 180, 18]


Please set a GitHub issue with above error message at: https://github.com/mljar/mljar-supervised/issues/new

## Error for 14_LightGBM_KMeansFeatures_Stacked

Input X contains NaN.
MiniBatchKMeans does not accept missing values encoded as NaN natively. For supervised learning, you might want to consider sklearn.ensemble.HistGradientBoostingClassifier and Regressor which accept missing values encoded as NaNs natively. Alternatively, it is possible to preprocess the data, for instance by using an imputer transformer in a pipeline or drop samples with missing values. See https://scikit-learn.org/stable/modules/impute.html You can find a list of all estimators that handle NaN values at the following page: https://scikit-learn.org/stable/modules/impute.html#estimators-that-handle-nan-values
Traceback (most recent call last):
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\base_automl.py", line 1183, in _fit
    trained = self.train_model(params)
              ^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\base_automl.py", line 388, in train_model
    mf.train(results_path, model_subpath)
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\model_framework.py", line 192, in train
    ].fit_and_transform(
      ^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\preprocessing\preprocessing.py", line 199, in fit_and_transform
    self._kmeans.fit(X_train[numeric_cols], y_train)
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\supervised\preprocessing\kmeans_transformer.py", line 55, in fit
    self._kmeans.fit(X)
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\base.py", line 1473, in wrapper
    return fit_method(estimator, *args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\cluster\_kmeans.py", line 2073, in fit
    X = self._validate_data(
        ^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\base.py", line 633, in _validate_data
    out = check_array(X, input_name="X", **check_params)
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\utils\validation.py", line 1064, in check_array
    _assert_all_finite(
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\utils\validation.py", line 123, in _assert_all_finite
    _assert_all_finite_element_wise(
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\utils\validation.py", line 172, in _assert_all_finite_element_wise
    raise ValueError(msg_err)
ValueError: Input X contains NaN.
MiniBatchKMeans does not accept missing values encoded as NaN natively. For supervised learning, you might want to consider sklearn.ensemble.HistGradientBoostingClassifier and Regressor which accept missing values encoded as NaNs natively. Alternatively, it is possible to preprocess the data, for instance by using an imputer transformer in a pipeline or drop samples with missing values. See https://scikit-learn.org/stable/modules/impute.html You can find a list of all estimators that handle NaN values at the following page: https://scikit-learn.org/stable/modules/impute.html#estimators-that-handle-nan-values


Please set a GitHub issue with above error message at: https://github.com/mljar/mljar-supervised/issues/new

