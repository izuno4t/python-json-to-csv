# coding:utf-8

#Pandasをインポート
import pandas as pd
import json

#変換したいJSONファイルを読み込む
df = pd.read_json('HAC_SERDEV_LIST_20171130_365.json', lines=True)
print(df)

# read_jsonした結果だとネストしたjsonを展開できないのでnormalizeで展開させる
# df_json = pd.json_normalize(df)
# df.to_csv("out.csv", encoding='utf-8')

