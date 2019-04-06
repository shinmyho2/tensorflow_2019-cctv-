import pandas as pd
import xlrd

ctx = "../data/"
seoul_cctv = pd.read_csv(ctx+"CCTV_in_Seoul.csv", encoding='utf-8')
print(seoul_cctv.head())

seoul_cctv_idx = seoul_cctv.columns
print(seoul_cctv_idx)

seoul_cctv.rename(columns={seoul_cctv.columns[0] : '구별'}, inplace=True)
print(seoul_cctv)

seoul_pop = pd.read_excel(ctx+"population_in_Seoul.xls", encoding='utf-8', header=2, usecols='B,D,G,J,N')
print(seoul_pop)

seoul_pop.rename(columns={seoul_pop.columns[0]: '구별',
                          seoul_pop.columns[1]: '인구수',
                          seoul_pop.columns[2]: '한국인',
                          seoul_pop.columns[3]: '외국인',
                          seoul_pop.columns[4]: '고령자'}, inplace=True)

print(seoul_pop.head())

import numpy as np

seoul_cctv.sort_values(by='소계', ascending=True).head(5)

seoul_pop.drop([0], inplace=True)
print(seoul_pop)

seoul_pop['구별'].unique()
print(seoul_pop)

seoul_pop[seoul_pop['구별'].isnull()]
seoul_pop.drop([26],inplace=True) # NaN 있는 행 삭제
print(seoul_pop)