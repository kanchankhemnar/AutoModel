# Summary of Ensemble

[<< Go back](../README.md)


## Ensemble structure
| Model           |   Weight |
|:----------------|---------:|
| 14_LightGBM     |        1 |
| 19_DecisionTree |        2 |
| 1_DecisionTree  |        3 |
| 20_LightGBM     |       10 |

### Metric details
|           |   AA |       BA |   BB |   CB |   CC |   DC |       DD |     Fail |   accuracy |   macro avg |   weighted avg |   logloss |
|:----------|-----:|---------:|-----:|-----:|-----:|-----:|---------:|---------:|-----------:|------------:|---------------:|----------:|
| precision | 1    | 0.25     |    0 |    1 |  0.5 |    0 | 0.333333 | 0.666667 |   0.444444 |    0.46875  |       0.527778 |   1.32742 |
| recall    | 0.25 | 0.5      |    0 |    1 |  0.5 |    0 | 0.5      | 1        |   0.444444 |    0.46875  |       0.444444 |   1.32742 |
| f1-score  | 0.4  | 0.333333 |    0 |    1 |  0.5 |    0 | 0.4      | 0.8      |   0.444444 |    0.429167 |       0.425926 |   1.32742 |
| support   | 4    | 2        |    2 |    2 |  2   |    2 | 2        | 2        |   0.444444 |   18        |      18        |   1.32742 |


## Confusion matrix
|                 |   Predicted as AA |   Predicted as BA |   Predicted as BB |   Predicted as CB |   Predicted as CC |   Predicted as DC |   Predicted as DD |   Predicted as Fail |
|:----------------|------------------:|------------------:|------------------:|------------------:|------------------:|------------------:|------------------:|--------------------:|
| Labeled as AA   |                 1 |                 3 |                 0 |                 0 |                 0 |                 0 |                 0 |                   0 |
| Labeled as BA   |                 0 |                 1 |                 1 |                 0 |                 0 |                 0 |                 0 |                   0 |
| Labeled as BB   |                 0 |                 0 |                 0 |                 0 |                 0 |                 0 |                 1 |                   1 |
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
