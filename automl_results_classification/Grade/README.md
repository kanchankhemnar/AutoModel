# AutoML Leaderboard

| Best model   | name                                                               | model_type    | metric_type   |   metric_value |   train_time |
|:-------------|:-------------------------------------------------------------------|:--------------|:--------------|---------------:|-------------:|
|              | [1_DecisionTree](1_DecisionTree/README.md)                         | Decision Tree | logloss       |        1.72988 |         2.69 |
|              | [2_DecisionTree](2_DecisionTree/README.md)                         | Decision Tree | logloss       |        4.04011 |         2.07 |
|              | [3_DecisionTree](3_DecisionTree/README.md)                         | Decision Tree | logloss       |        4.04011 |         2.1  |
|              | [4_Linear](4_Linear/README.md)                                     | Linear        | logloss       |        1.96024 |        20.16 |
|              | [14_LightGBM](14_LightGBM/README.md)                               | LightGBM      | logloss       |        1.68199 |         2.69 |
|              | [5_Xgboost](5_Xgboost/README.md)                                   | Xgboost       | logloss       |        1.70127 |         3.23 |
|              | [5_Xgboost_categorical_mix](5_Xgboost_categorical_mix/README.md)   | Xgboost       | logloss       |        1.7307  |         3.52 |
|              | [14_LightGBM_KMeansFeatures](14_LightGBM_KMeansFeatures/README.md) | LightGBM      | logloss       |        1.50112 |         3.24 |
|              | [15_LightGBM](15_LightGBM/README.md)                               | LightGBM      | logloss       |        1.50112 |         1.93 |
|              | [16_LightGBM](16_LightGBM/README.md)                               | LightGBM      | logloss       |        1.68199 |         1.33 |
|              | [17_Xgboost](17_Xgboost/README.md)                                 | Xgboost       | logloss       |        1.70489 |         1.57 |
|              | [18_Xgboost](18_Xgboost/README.md)                                 | Xgboost       | logloss       |        1.71091 |         1.45 |
|              | [19_DecisionTree](19_DecisionTree/README.md)                       | Decision Tree | logloss       |        2.1686  |         1.15 |
|              | [20_LightGBM](20_LightGBM/README.md)                               | LightGBM      | logloss       |        1.41144 |         1.65 |
|              | [21_LightGBM](21_LightGBM/README.md)                               | LightGBM      | logloss       |        1.41144 |         1.65 |
|              | [22_LightGBM](22_LightGBM/README.md)                               | LightGBM      | logloss       |        1.4546  |         1.55 |
| **the best** | [Ensemble](Ensemble/README.md)                                     | Ensemble      | logloss       |        1.32742 |         1.65 |

### AutoML Performance
![AutoML Performance](ldb_performance.png)

### AutoML Performance Boxplot
![AutoML Performance Boxplot](ldb_performance_boxplot.png)

### Spearman Correlation of Models
![models spearman correlation](correlation_heatmap.png)

