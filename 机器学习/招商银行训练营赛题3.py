# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 10:40:43 2019

@author: yllzxzyq
"""

import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import cross_val_score
import pandas as pd
import xgboost as xgb
from xgboost.sklearn import XGBRegressor
import matplotlib.pyplot as plt
import seaborn as sns
import copy
import datetime
import time
from dateutil.parser import parse
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import pickle
import xlab
import operator
from sklearn import preprocessing
from sklearn.ensemble import ExtraTreesRegressor

# def comple(train_data):
#     create_date = pd.date_range('2017-01-01','2019-02-28',freq='D')
#     complement = pd.DataFrame(index = pd.MultiIndex.from_product([
#                                     create_date,
#                                     list(range(1,101)),
#                                     ['typ1','typ2','typ3','typ4','typ5','typ6']
#                                 ]))
#     complement.reset_index(inplace=True)
#     complement.columns = ['date','id','type']
#     train_data['date'] = pd.to_datetime(train_data['date'],infer_datetime_format=True)
#     completed = pd.merge(complement,train_data, on=['date','id','type'], how='outer')
#     completed['counter_volume'] = completed['counter_volume'].fillna(0)
#     return completed

def getDateType():
    date=pd.read_table('data/da0030/LV35_T_TDW_BOPR_OPR_T80_WKD_PARM_INF_20190130_000AH000.DAT',engine='python',sep = '|',header=None)
    date[0]=pd.to_datetime(date[0])
    date=date.set_index(0,drop=False)
    valid=date['2017':'2019.2.28'].iloc[:,:2].values
    d={'date':valid[:,0],'type':valid[:,1]}
    df=pd.DataFrame(data=d)
    df=df.sort_values(by='date')
    df=df.reset_index(drop=True)
    df=pd.get_dummies(df,columns=['type'])
    df.rename(columns={column:column[:5]+column[6:] for column in df.columns},inplace=True)
    return df

def build_features(raw_data):
    X_raw = copy.deepcopy(raw_data)
    X_raw['date']=pd.to_datetime(X_raw['date'],infer_datetime_format=True)
    X_raw['type'] = X_raw['type'].apply(lambda x:x[-1])
    X_raw['weekday'] = X_raw['date'].dt.weekday
    X_raw['is_month_start'] = X_raw['date'].dt.is_month_start
    X_raw['is_month_end'] = X_raw['date'].dt.is_month_end
    X_raw['ith_week'] = X_raw['date'].dt.week
    X_raw['month'] = X_raw['date'].dt.month
    lbl = preprocessing.LabelEncoder()
    X_raw['id'] = lbl.fit_transform(X_raw['id'].astype(str))#将提示的包含错误数据类型这一列进行转换
    X_raw['type'] = lbl.fit_transform(X_raw['type'].astype(str))
    return X_raw
	
def add_day(X_raw):
    return X_raw['date'].split('/')[-1]

def add_block(X_raw):
    year_month='/'.join(X_raw['date'].split('/')[:-1])
    d={
        '2017/1':0,
        '2017/2':1,
        '2017/3':2,
        '2017/4':3,
        '2017/5':4,
        '2017/6':5,
        '2017/7':6,
        '2017/8':7,
        '2017/9':8,
        '2017/10':9,
        '2017/11':10,
        '2017/12':11,
        '2018/1':12,
        '2018/2':13,
        '2018/3':14,
        '2018/4':15,
        '2018/5':16,
        '2018/6':17,
        '2018/7':18,
        '2018/8':19,
        '2018/9':20,
        '2018/10':21,
        '2018/11':22,
        '2018/12':23,
        '2019/1':24,
        '2019/2':25
    }
    return d[year_month]

def shift_i_week(X_raw,week_list):
    for j in week_list:
        X_raw["lag_{}".format(j)] = X_raw.counter_volume.shift(j*7)
    return X_raw      

def shift_i_month(X_raw,target,tags):
    X_raw['day']=X_raw.apply(add_day,axis=1)
    target['day']=target.apply(add_day,axis=1)
    for i in tags:
        X_raw['date_block']=X_raw.apply(add_block,axis=1)
        target['date_block']=target.apply(add_block,axis=1)
        shifted=X_raw[['id','date_block','counter_volume','type','day']].copy()
        shifted['date_block']+=i
        shifted.rename(columns={'counter_volume':'counter_volume_shift_'+str(i)},inplace=True)
        target=target.merge(shifted,how='left',on=['id','date_block','type','day'])
    return target


# 读取训练数据
train_data = pd.read_csv('./data/da0030/train.csv', encoding='utf-8')
train_shift_mon = shift_i_month(train_data,train_data, range(2,13)) 
# train_shift_mon_week = shift_i_week(train_shift_mon,[8,9,10,11,12])
# 读取测试数据,先不管周了
test_data = pd.read_csv('./data/da0030/predict.csv', encoding='utf-8')
test_shift_mon = shift_i_month(train_data,test_data, range(2,13)) 
# test_shift_mon_week = shift_i_week(test_shift_mon,[8,9,10,11,12])
others = getDateType()
train_more = build_features(train_shift_mon)
test_more = build_features(test_shift_mon)
train_plus=train_more.merge(others, on='date',how='left')
test_plus = test_more.merge(others, on ='date',how='left')

train_plus=train_plus.fillna(0)
X_train=copy.deepcopy(train_plus)
X_train.drop(['VTM_volume','ATM_volume','counter_volume','date'],axis=1,inplace=True)
Y_train=train_data['counter_volume']

test_plus=test_plus.fillna(0)
X_test=copy.deepcopy(test_plus)

VA_train=train_data[['VTM_volume','ATM_volume']]
from sklearn.ensemble import RandomForestRegressor, ExtraTreesRegressor, GradientBoostingRegressor
etr = RandomForestRegressor(max_depth=11, min_samples_split=3, min_samples_leaf=1)
etr.fit(X_train, VA_train.fillna(0))
etr_VA_predict = etr.predict(test_plus)
VA_predict = pd.DataFrame(etr_VA_predict)

X_test.insert(2,'VTM_volume',VA_predict[0])
X_test.insert(3,'ATM_volume',VA_predict[1])
X_train2=copy.deepcopy(train_plus)
X_train2.drop(['date','counter_volume'],axis=1,inplace=True)
X_train2.head()
Model2 = RandomForestRegressor(max_depth=11, min_samples_split=3, min_samples_leaf=1)
Model2.fit(X_train2,Y_train)
Y_predict = Model2.predict(X_test)