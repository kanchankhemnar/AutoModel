# Summary of 4_Linear_KMeansFeatures

[<< Go back](../README.md)


## Logistic Regression (Linear)
- **n_jobs**: -1
- **explain_level**: 0

## Validation
 - **validation_type**: split
 - **train_ratio**: 0.9
 - **shuffle**: True
 - **stratify**: True

## Optimized metric
logloss

## Training time

3.8 seconds

## Metric details
|           |     score |     threshold |
|:----------|----------:|--------------:|
| logloss   | 0.0651124 | nan           |
| auc       | 0.995833  | nan           |
| f1        | 0.98      |   0.374396    |
| accuracy  | 0.98004   |   0.374396    |
| precision | 1         |   0.940068    |
| recall    | 1         |   2.36468e-06 |
| mcc       | 0.96008   |   0.374396    |


## Metric details with threshold from accuracy metric
|           |     score |   threshold |
|:----------|----------:|------------:|
| logloss   | 0.0651124 |  nan        |
| auc       | 0.995833  |  nan        |
| f1        | 0.98      |    0.374396 |
| accuracy  | 0.98004   |    0.374396 |
| precision | 0.98      |    0.374396 |
| recall    | 0.98      |    0.374396 |
| mcc       | 0.96008   |    0.374396 |


## Confusion matrix (at threshold=0.374396)
|                   |   Predicted as Female |   Predicted as Male |
|:------------------|----------------------:|--------------------:|
| Labeled as Female |                   246 |                   5 |
| Labeled as Male   |                     5 |                 245 |

## Learning curves
![Learning curves](learning_curves.png)
## Confusion Matrix

![Confusion Matrix](confusion_matrix.png)


## Normalized Confusion Matrix

![Normalized Confusion Matrix](confusion_matrix_normalized.png)


## ROC Curve

![ROC Curve](roc_curve.png)


## Kolmogorov-Smirnov Statistic

![Kolmogorov-Smirnov Statistic](ks_statistic.png)


## Precision-Recall Curve

![Precision-Recall Curve](precision_recall_curve.png)


## Calibration Curve

![Calibration Curve](calibration_curve_curve.png)


## Cumulative Gains Curve

![Cumulative Gains Curve](cumulative_gains_curve.png)


## Lift Curve

![Lift Curve](lift_curve.png)



[<< Go back](../README.md)
