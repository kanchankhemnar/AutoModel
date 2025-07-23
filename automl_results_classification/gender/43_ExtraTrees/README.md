# Summary of 43_ExtraTrees

[<< Go back](../README.md)


## Extra Trees Classifier (Extra Trees)
- **n_jobs**: -1
- **criterion**: gini
- **max_features**: 0.5
- **min_samples_split**: 20
- **max_depth**: 4
- **eval_metric_name**: logloss
- **explain_level**: 0

## Validation
 - **validation_type**: split
 - **train_ratio**: 0.9
 - **shuffle**: True
 - **stratify**: True

## Optimized metric
logloss

## Training time

2.4 seconds

## Metric details
|           |     score |   threshold |
|:----------|----------:|------------:|
| logloss   | 0.0867141 | nan         |
| auc       | 0.994207  | nan         |
| f1        | 0.970297  |   0.478829  |
| accuracy  | 0.97006   |   0.478829  |
| precision | 1         |   0.938946  |
| recall    | 1         |   0.0042685 |
| mcc       | 0.940309  |   0.478829  |


## Metric details with threshold from accuracy metric
|           |     score |   threshold |
|:----------|----------:|------------:|
| logloss   | 0.0867141 |  nan        |
| auc       | 0.994207  |  nan        |
| f1        | 0.970297  |    0.478829 |
| accuracy  | 0.97006   |    0.478829 |
| precision | 0.960784  |    0.478829 |
| recall    | 0.98      |    0.478829 |
| mcc       | 0.940309  |    0.478829 |


## Confusion matrix (at threshold=0.478829)
|                   |   Predicted as Female |   Predicted as Male |
|:------------------|----------------------:|--------------------:|
| Labeled as Female |                   241 |                  10 |
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
