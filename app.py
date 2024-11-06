import streamlit as st
import pandas as pd
import numpy as np

# サンプルデータの作成
data = {
    'ID': [1, 2, 3, 4, 5],
    '名前': ['山田太郎', '佐藤花子', '鈴木一郎', '田中美咲', '高橋健太'],
    '年齢': [28, 35, np.nan, 42, 31],
    '性別': ['男', '女', '男', '女', '男'],
    '売上': [100000, 150000, 120000, np.nan, 200000],
    '部門': ['営業', '管理', '営業', '企画', '営業'],
    '入社日': ['2020-04-01', '2018/07/15', '2019-09-30', '2017-12-25', '2021-01-10']
}

df = pd.DataFrame(data)

# Streamlitアプリの設定
st.title('データフレームの表示と欠損値の処理')

# 元のデータフレームの表示
st.subheader('元のデータフレーム')
st.dataframe(df)

# 欠損値を0で埋める
df_filled = df.fillna(0)

# 欠損値を含む行を削除
df_dropped = df.dropna()

# 欠損値を0で埋めた結果の表示
st.subheader('欠損値を0で埋めた結果')
st.dataframe(df_filled)

# 欠損値を含む行を削除した結果の表示
st.subheader('欠損値を含む行を削除した結果')
st.dataframe(df_dropped)

# 年齢と売上を数値型に変換
df['年齢'] = pd.to_numeric(df['年齢'], errors='coerce')
df['売上'] = pd.to_numeric(df['売上'], errors='coerce')

# データ型の表示
st.subheader('データ型')
st.write(df.dtypes)

# 名前の正規化（姓と名を分離）
df[['姓', '名']] = df['名前'].str.extract('(.+)(.{1})')

# 正規化された名前の表示
st.subheader('正規化された名前')
st.dataframe(df[['姓', '名']])

# 日付形式の統一
df['入社日'] = pd.to_datetime(df['入社日'], format='mixed')

# 年、月、日の抽出
df['入社年'] = df['入社日'].dt.year
df['入社月'] = df['入社日'].dt.month
df['入社日'] = df['入社日'].dt.day

# 日付形式の統一結果の表示
st.subheader('日付形式の統一結果')
st.dataframe(df[['入社年', '入社月', '入社日']])


