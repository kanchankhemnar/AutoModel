# Summary of 14_LightGBM_KMeansFeatures

[<< Go back](../README.md)


## LightGBM
- **n_jobs**: -1
- **objective**: multiclass
- **num_leaves**: 15
- **learning_rate**: 0.05
- **feature_fraction**: 0.8
- **bagging_fraction**: 0.5
- **min_data_in_leaf**: 50
- **metric**: multi_logloss
- **custom_eval_metric_name**: None
- **num_class**: 8
- **explain_level**: 0

## Validation
 - **validation_type**: split
 - **train_ratio**: 0.9
 - **shuffle**: True
 - **stratify**: True

## Optimized metric
logloss

## Training time

2.3 seconds

### Metric details
|           |   AA |       BA |   BB |       CB |   CC |   DC |   DD |   Fail |   accuracy |   macro avg |   weighted avg |   logloss |
|:----------|-----:|---------:|-----:|---------:|-----:|-----:|-----:|-------:|-----------:|------------:|---------------:|----------:|
| precision | 1    | 0.333333 |    0 | 0.5      |  0.5 |    0 |  0.5 |      1 |   0.444444 |    0.479167 |       0.537037 |   1.50112 |
| recall    | 0.25 | 0.5      |    0 | 1        |  0.5 |    0 |  0.5 |      1 |   0.444444 |    0.46875  |       0.444444 |   1.50112 |
| f1-score  | 0.4  | 0.4      |    0 | 0.666667 |  0.5 |    0 |  0.5 |      1 |   0.444444 |    0.433333 |       0.42963  |   1.50112 |
| support   | 4    | 2        |    2 | 2        |  2   |    2 |  2   |      2 |   0.444444 |   18        |      18        |   1.50112 |


## Confusion matrix
|                 |   Predicted as AA |   Predicted as BA |   Predicted as BB |   Predicted as CB |   Predicted as CC |   Predicted as DC |   Predicted as DD |   Predicted as Fail |
|:----------------|------------------:|------------------:|------------------:|------------------:|------------------:|------------------:|------------------:|--------------------:|
| Labeled as AA   |                 1 |                 2 |                 0 |                 0 |                 0 |                 1 |                 0 |                   0 |
| Labeled as BA   |                 0 |                 1 |                 1 |                 0 |                 0 |                 0 |                 0 |                   0 |
| Labeled as BB   |                 0 |                 0 |                 0 |                 2 |                 0 |                 0 |                 0 |                   0 |
| Labeled as CB   |                 0 |                 0 |                 0 |                 2 |                 0 |                 0 |                 0 |                   0 |
| Labeled as CC   |                 0 |                 0 |                 1 |                 0 |                 1 |                 0 |                 0 |                   0 |
| Labeled as DC   |                 0 |                 0 |                 0 |                 0 |                 1 |                 0 |                 1 |                   0 |
| Labeled as DD   |                 0 |                 0 |                 0 |                 0 |                 0 |                 1 |                 1 |                   0 |
| Labeled as Fail |                 0 |                 0 |                 0 |                 0 |                 0 |                 0 |                 0 |                   2 |

## Learning curves
![Learning curves](learning_curves.png)
## Confusion Matrix

![Confusion Matrix](confusion_matrix.png)


## Normalized Confusion Matrix

![Normalized Confusion Matrix](confusion_matrix_normalized.png)


## ROC Curve

![ROC Curve](roc_curve.png)


## Precision Recall Curve

![Precision Recall Curve](precision_recall_curve.png)



[<< Go back](../README.md)
