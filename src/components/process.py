

# %%

import json

# 打开并读取JSON文件
import geopandas as gpd

# 读取GeoJSON文件
gdf = gpd.read_file('./USA.json')

# 打印GeoDataFrame的前几行
print(gdf.head())


import pandas as pd 
df = pd.read_csv('./president.csv')
df_max_votes = df.loc[df.groupby(['year', 'state'])['candidatevotes'].idxmax()]
df_max_votes = df_max_votes[['year', 'state', 'candidate', 'candidatevotes', 'party_simplified']]
# %%
# 使用pivot_table将year列转为列标题
# 保留 'state' 列并将 'year' 设置为索引，按 'state' 和 'year' 分组
df_pivot = df_max_votes.set_index(['year', 'state']).unstack(level='year')

# 将列名转换为类似 'candidate_1976', 'candidate_1980' 的格式
df_pivot.columns = [f'{col[0]}_{col[1]}' for col in df_pivot.columns]

# 重置索引，以便 'state' 不再作为索引列，而是恢复为普通列
df_pivot.reset_index(inplace=True)
# %%
# 确保df_pivot和gdf中用于匹配的字段是小写字母，避免大小写不一致的问题
df_pivot['state_lower'] = df_pivot['state'].str.lower()
gdf['name_lower'] = gdf['name'].str.lower()

# 使用merge方法进行连接
merged_gdf = gdf.merge(df_pivot, left_on='name_lower', right_on='state_lower', how='left')

# 打印合并后的结果
print(merged_gdf.head())
merged_gdf = merged_gdf.drop(columns=['name_lower', 'state'])
# %%
merged_gdf.to_file('./USA.geojson', driver='GeoJSON')
# %%
