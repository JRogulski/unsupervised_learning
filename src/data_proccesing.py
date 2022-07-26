import pandas as pd
from sklearn.preprocessing import PowerTransformer
from sklearn.feature_selection import VarianceThreshold
import seaborn as sns
from sklearn.preprocessing import PowerTransformer
from src import config
import numpy as np
import matplotlib.pyplot as plt
train_df = pd.read_csv(config.TRAIN_DATA)
feature_selector = VarianceThreshold(threshold=1.5)


best_data = ['f_07', 'f_08', 'f_09', 'f_10', 'f_11',
             'f_12', 'f_13', 'f_22', 'f_23', 'f_24',
             'f_25', 'f_26', 'f_27', 'f_28']

pt = PowerTransformer()
train_scaled = pt.fit_transform(train_df[best_data])
train_scaled = pd.DataFrame(train_scaled, columns=best_data)
train_scaled.to_csv(config.TRAIN_PREPROCESSED_DATA)