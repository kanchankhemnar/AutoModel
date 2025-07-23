# Summary of Ensemble

[<< Go back](../README.md)


## Ensemble structure
| Model                   |   Weight |
|:------------------------|---------:|
| 4_Linear_KMeansFeatures |       10 |
| 52_NeuralNetwork        |        1 |
| 53_Xgboost              |        3 |
| 57_Xgboost              |        3 |

## Metric details
|           |     score |     threshold |
|:----------|----------:|--------------:|
| logloss   | 0.0583023 | nan           |
| auc       | 0.996327  | nan           |
| f1        | 0.98      |   0.391602    |
| accuracy  | 0.98004   |   0.391602    |
| precision | 1         |   0.954053    |
| recall    | 1         |   0.000555552 |
| mcc       | 0.96008   |   0.391602    |


## Metric details with threshold from accuracy metric
|           |     score |   threshold |
|:----------|----------:|------------:|
| logloss   | 0.0583023 |  nan        |
| auc       | 0.996327  |  nan        |
| f1        | 0.98      |    0.391602 |
| accuracy  | 0.98004   |    0.391602 |
| precision | 0.98      |    0.391602 |
| recall    | 0.98      |    0.391602 |
| mcc       | 0.96008   |    0.391602 |


## Confusion matrix (at threshold=0.391602)
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
