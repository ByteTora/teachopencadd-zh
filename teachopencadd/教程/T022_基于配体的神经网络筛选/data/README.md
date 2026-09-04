# 数据

此文件夹存储 Jupyter notebook 的输入和输出数据。

输入文件如下：

- `CHEMBL25_activities_EGFR.csv`：用于训练神经网络的数据集。
- `test.csv`：无标签数据集。包含我们将使用训练好的神经网络提供 pIC50 预测的化合物。

输出文件如下：
- `best_weights.hdf5`：存储神经网络训练完成后的最佳权重。
- `ANN_model.hdf5`：为结果可复现而保存的人工神经网络 (ANN)。
- `predicted_pIC50_df.csv`：包含使用训练好的神经网络对 `test.csv` 数据集中化合物进行 pIC50 预测值的 csv 文件。
