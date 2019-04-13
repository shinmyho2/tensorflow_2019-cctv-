import pandas as pd
import numpy as np
ctx = '../data/'
filename = ctx + 'CCTV_in_Seoul.csv'
df_cctv = pd.read_csv(filename, encoding='UTF-8')
# print(seoul_cctv.head())
seoul_cctv_idx = df_cctv.columns
"""
['기관명', '소계', '2013년도 이전', '2014년', '2015년', '2016년']
"""
df_cctv.rename(columns={df_cctv.columns[0]: '구별'}, inplace=True)
df_pop = pd.read_excel(ctx + 'pop_in_Seoul.xls', encoding="UTF-8",
                          header=2,usecols='B,D,G,J,N')
df_pop.rename(columns={df_pop.columns[0]: '구별'
    ,df_pop.columns[1]: '인구수'
    ,df_pop.columns[2]: '한국인'
    ,df_pop.columns[3]: '외국인'
    ,df_pop.columns[4]: '고령자'}, inplace=True)
df_cctv.sort_values(by='소계', ascending=True).head(5)
df_pop.drop([0], inplace=True)
df_pop['구별'].unique()
df_pop['구별'].isnull()
df_pop.drop([26], inplace=True)
df_pop['외국인비율'] = df_pop['외국인'] / df_pop['인구수'] * 100
df_pop['고령자비율'] = df_pop['고령자'] / df_pop['인구수'] * 100
df_cctv.drop(['2013년도 이전', '2014년', '2015년', '2016년'], 1, inplace=True)
df_cctv_pop = pd.merge(df_cctv, df_pop, on='구별')
df_cctv_pop.set_index('구별', inplace=True)
cor1 = np.corrcoef(df_cctv_pop['고령자비율'],df_cctv_pop['소계'])
cor2 = np.corrcoef(df_cctv_pop['외국인비율'],df_cctv_pop['소계'])
print('고령자비율 상관계수 {} \n 외국인비율 상관계수 {}'.format(cor1, cor2))
"""
r이 -1.0과 -0.7 사이이면, 강한 음적 선형관계,
r이 -0.7과 -0.3 사이이면, 뚜렷한 음적 선형관계,
r이 -0.3과 -0.1 사이이면, 약한 음적 선형관계,
r이 -0.1과 +0.1 사이이면, 거의 무시될 수 있는 선형관계,
r이 +0.1과 +0.3 사이이면, 약한 양적 선형관계,
r이 +0.3과 +0.7 사이이면, 뚜렷한 양적 선형관계,
r이 +0.7과 +1.0 사이이면, 강한 양적 선형관계
고령자비율 상관계수 [[ 1.         -0.28078554]
 [-0.28078554  1.        ]] 
 외국인비율 상관계수 [[ 1.         -0.13607433]
 [-0.13607433  1.        ]]
"""
df_cctv_pop.to_csv(ctx+'cctv_pop.csv')
