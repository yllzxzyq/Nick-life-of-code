# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 12:49:18 2019

@author: yllzxzyq
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import make_scorer
from sklearn.metrics import f1_score

scorer =  make_scorer(f1_score)
def gridfit(clf,parameter,X,y):
    grid_obj = GridSearchCV(clf,parameters,scoring=scorer)
    grid_fit = grid_obj.fit(X, y)
    best_clf = grid_fit.best_estimator_