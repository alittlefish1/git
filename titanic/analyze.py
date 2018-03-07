# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
from pandas import Series,DataFrame
from IPython.display import display
import matplotlib.pyplot as plt

data_train = pd.read_csv('train.csv')
# display(data_train.head(10))
print(data_train.columns.values)
# display(data_train)

# data_train.info()
# display(data_train.describe())
def each_analyze():
    fig = plt.figure()
    fig.set(alpha = 0.2)

    plt.subplot2grid((2,3),(0,0))
    data_train.Survived.value_counts().plot(kind='bar')
    plt.title(u"获救情况(1为获救)")
    plt.ylabel(u"person")

    plt.subplot2grid((2,3),(0,1))
    data_train.Pclass.value_counts().plot(kind='bar')
    plt.title(u'乘客等级')
    plt.ylabel(u'人数')

    plt.subplot2grid((2,3),(0,2))
    plt.scatter(data_train.Survived,data_train.Age)
    plt.ylabel('age')
    plt.grid(b=True,which='major',axis='y')
    plt.title('survived distribution')

    plt.subplot2grid((2,3),(1,0),colspan=2)
    data_train.Age[data_train.Pclass == 1].plot(kind='kde')
    data_train.Age[data_train.Pclass == 2].plot(kind='kde')
    data_train.Age[data_train.Pclass == 3].plot(kind='kde')
    plt.xlabel('age')
    plt.ylabel('density')
    plt.title('age distribution in each class')
    plt.legend(('fist class','second class','third class'),loc='best')

    plt.subplot2grid((2,3),(1,2))
    data_train.Embarked.value_counts().plot(kind='bar')
    plt.title('people counting in each embarked')
    plt.ylabel('number of people')

    plt.show()


#查看各等级的乘客获救的情况

def class_infulence():
    """阶级对存活的影响"""
    fig = plt.figure()
    fig.set(alpha=0.2)
    #查看各个信息的与获救情况的关联
    #查看各个等级的获救情况
    survived_0 = data_train.Pclass[data_train.Survived == 0].value_counts()
    survived_1 = data_train.Pclass[data_train.Survived == 1].value_counts()
    df=pd.DataFrame({'saved':survived_1, 'unsaved':survived_0})
    # print(df)
    df.plot(kind='bar', stacked=True)
    plt.title("situation of passenger saved")
    plt.xlabel("class of passenger")
    plt.ylabel("number of people")
    plt.savefig('class_infulence.png')
    plt.show()
class_infulence()
def gender_infulence():
    """性别的影响"""
    fig = plt.figure()
    fig.set(alpha=0.2)

    survived_f = data_train.Survived[data_train.Sex == 'female'].value_counts()
    survived_m = data_train.Survived[data_train.Sex == 'male'].value_counts()
    df =pd.DataFrame({'female':survived_f,'male':survived_m})
    print(df)
    df.plot(kind='bar',stacked=True)
    plt.title('situation of passenger saved')
    plt.xlabel('gender')
    plt.ylabel('number of people')
    plt.show()


# gender_infulence()
def dif_class_of_dif_gender():
    """不同阶级不同性别的获救情况"""

    fig = plt.figure()
    fig.set(alpha=0.65)
    plt.title('situation of different class and gender')

    #男性高级场
    ax1 = fig.add_subplot(141)
    df1 = data_train.Survived[data_train.Sex == 'female'][data_train.Pclass == 3].value_counts()
    df1.plot(kind='bar', label="female ,low class", color='#FA2479')
    ax1.set_xticklabels(['saved','unsaved'],rotation=0)
    plt.legend(['female/lowclass'],loc='best')
    #男性非高级场
    ax2 = fig.add_subplot(142)
    df2 = data_train.Survived[data_train.Sex == 'female'][data_train.Pclass != 3].value_counts()
    df2.plot(kind='bar', label='female, highclass', color='pink')
    ax2.set_xticklabels(['saved', 'unsaved'],rotation=0)
    plt.legend(['female/highclass'], loc='best')
    #
    ax3 = fig.add_subplot(143)
    df3 = data_train.Survived[data_train.Sex == 'male'][data_train.Pclass == 3].value_counts()
    df3.plot(kind = 'bar',label='male ,low class',color='lightblue')
    ax3.set_xticklabels(['saved', 'unsaved'],rotation=0)
    ax3.legend(['male/low class'], loc='best')

    ax4 = fig.add_subplot(144)
    df4=data_train.Survived[data_train.Sex == 'male'][data_train.Pclass != 3].value_counts()
    df4.plot(kind = 'bar',label='male ,high class',color='steelblue')
    ax4.set_xticklabels(['saved', 'unsaved'],rotation=0)
    ax4.legend(['male/high class'], loc='best')
    plt.savefig('dif_class_of_dif_gender.png')
    plt.show()
    # plt.savefig('dif_class_of_dif_gender.png')
# dif_class_of_dif_gender()
def situation_of_embarked():
    fig = plt.figure()
    fig.set(alpha=0.4)

    survived_0 = data_train.Embarked[data_train.Survived == 0].value_counts()
    survived_1 = data_train.Embarked[data_train.Survived == 1].value_counts()
    df = pd.DataFrame({'saved':survived_1,'unsaved':survived_0})
    df.plot(kind = 'bar',stacked = True)

    plt.title('saved situation of different embarked')
    plt.xlabel('different embarked')
    plt.ylabel('number of people')
    plt.savefig('situation_of_embarked.png')
    plt.show()

# situation_of_embarked()

# def situation_of_relations():
# g = data_train.groupby(['SibSp','Survived'])
#
# df = pd.DataFrame(g.count()['PassengerId'])
# print (df)
#
# g = data_train.groupby(['Parch','Survived'])
# df = pd.DataFrame(g.count()['PassengerId'])
# print(df)

# print(data_train.Cabin.value_counts())

def statistics_of_cabin():
    """统计船舱对获救的影响，数据缺少都认为是获救"""

    fig = plt.figure()
    fig.set(alpha=0.3)

    survived_h = data_train.Survived[pd.notnull(data_train.Cabin)].value_counts()
    survived_n = data_train.Survived[pd.isnull(data_train.Cabin)].value_counts()

    df = pd.DataFrame({'have':survived_h,'null':survived_n}).transpose()
    df.plot(kind='bar',stacked=True)
    plt.title('statistics_of_cabin')
    plt.xlabel('num of p')
    plt.ylabel('cabin')
    plt.savefig('statistics_of_cabin.png')
    plt.show()
# statistics_of_cabin()
