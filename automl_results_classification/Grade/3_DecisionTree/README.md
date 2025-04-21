# Summary of 3_DecisionTree

[<< Go back](../README.md)


## Decision Tree
- **n_jobs**: -1
- **criterion**: gini
- **max_depth**: 4
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

0.7 seconds

### Metric details
|           |       AA |   BA |   BB |   CB |       CC |       DC |   DD |   Fail |   accuracy |   macro avg |   weighted avg |   logloss |
|:----------|---------:|-----:|-----:|-----:|---------:|---------:|-----:|-------:|-----------:|------------:|---------------:|----------:|
| precision | 0.2      |    0 |    0 |    0 | 1        | 0.166667 |    0 |      0 |   0.166667 |    0.170833 |       0.174074 |   4.04011 |
| recall    | 0.25     |    0 |    0 |    0 | 0.5      | 0.5      |    0 |      0 |   0.166667 |    0.15625  |       0.166667 |   4.04011 |
| f1-score  | 0.222222 |    0 |    0 |    0 | 0.666667 | 0.25     |    0 |      0 |   0.166667 |    0.142361 |       0.151235 |   4.04011 |
| support   | 4        |    2 |    2 |    2 | 2        | 2        |    2 |      2 |   0.166667 |   18        |      18        |   4.04011 |


## Confusion matrix
|                 |   Predicted as AA |   Predicted as BA |   Predicted as BB |   Predicted as CB |   Predicted as CC |   Predicted as DC |   Predicted as DD |   Predicted as Fail |
|:----------------|------------------:|------------------:|------------------:|------------------:|------------------:|------------------:|------------------:|--------------------:|
| Labeled as AA   |                 1 |                 1 |                 0 |                 1 |                 0 |                 0 |                 0 |                   1 |
| Labeled as BA   |                 2 |                 0 |                 0 |                 0 |                 0 |                 0 |                 0 |                   0 |
| Labeled as BB   |                 0 |                 0 |                 0 |                 0 |                 0 |                 1 |                 0 |                   1 |
| Labeled as CB   |                 0 |                 0 |                 0 |                 0 |                 0 |                 2 |                 0 |                   0 |
| Labeled as CC   |                 0 |                 0 |                 0 |                 1 |                 1 |                 0 |                 0 |                   0 |
| Labeled as DC   |                 0 |                 0 |                 0 |                 1 |                 0 |                 1 |                 0 |                   0 |
| Labeled as DD   |                 0 |                 0 |                 0 |                 0 |                 0 |                 2 |                 0 |                   0 |
| Labeled as Fail |                 2 |                 0 |                 0 |                 0 |                 0 |                 0 |                 0 |                   0 |

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
