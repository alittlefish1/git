import numpy as np
import pandas as pd
# import matplotlib.pyplot as plt
import pygal
# RMS Titanic data visualization code
# 数据可视化代码
# from titanic_visualizations import survival_stats
from IPython.display import display
# % matplotlib inline

# Load the dataset
# 加载数据集
in_file = 'train.csv'
full_data = pd.read_csv(in_file)

# Print the first few entries of the RMS Titanic data
# 显示数据列表中的前几项乘客数据

display(full_data.head())
full_data.head(10)

# Store the 'Survived' feature in a new variable and remove it from the dataset
# 从数据集中移除 'Survived' 这个特征，并将它存储在一个新的变量中。
outcomes = full_data['Survived']
data = full_data.drop('Survived', axis = 1)

# Show the new dataset with 'Survived' removed
# 显示已移除 'Survived' 特征的数据集
# display(data.head())

# for i in range(1,6):
#     print(outcomes[i])
def accuracy_score(truth, pred):
    """ Returns accuracy score for input truth and predictions. """

    # Ensure that the number of predictions matches number of outcomes
    # 确保预测的数量与结果的数量一致
    if len(truth) == len(pred):

        # Calculate and return the accuracy as a percent
        # 计算预测准确率（百分比）
        return "Predictions have an accuracy of {:.2f}%.".format((truth == pred).mean() * 100)

    else:
        return "Number of predictions does not match number of outcomes!"


# Test the 'accuracy_score' function
# 测试 'accuracy_score' 函数
# predictions = pd.Series(np.ones(5, dtype=int))
# print (accuracy_score(outcomes[:5], predictions))


def predictions_0(data):
    """ Model with no features. Always predicts a passenger did not survive. """

    predictions = []
    for _ in data.iterrows():
        # Predict the survival of 'passenger'
        # 预测 'passenger' 的生还率
        predictions.append(0)

    # Return our predictions
    # 返回预测结果
    return pd.Series(predictions)


# Make the predictions
# 进行预测
# predictions = predictions_0(data)
# print (accuracy_score(outcomes, predictions))
# survival_stats(data, outcomes, 'Sex')
def survival_stats(data,data_survived,feature,male,female):
    """把每个特征于是否幸存可视化"""
    male_count = 0
    female_count = 0
    analyze_data = data['feature']
    # if len(data_survived) == len(analyze_data):
        # for i in range(1,(len(data_survived)+1)):
        #     if data_survived[i]:
        #         if analyze_data[i] == male:
        #             male_count += 1
        #         if analyze_data[i] == female:
        #             female_count += 1
     





    hist = pygal.Bar()
