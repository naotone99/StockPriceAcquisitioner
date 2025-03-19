import requests
import pandas as pd
    # pd.set_option('display.max_rows', None)  # 全行を表示
    # pd.set_option('display.max_columns', None)  # 全列を表示


demo_url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=IBM&apikey=demo'
# もし変数を利用する場合
api_key = 'demo'
symbol = 'IBM'
    # 最初のfは文字列内に変数や式を埋め込める
    # functionの前に?がつくのは、クエリパラメータの開始を示すため
        # function=TIME_SERIES_DAILY：キー（function）と値（TIME_SERIES_DAILY）のペア。
url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={symbol}&apikey={api_key}'

# APIリクエストを送信
response = requests.get(url)
# レスポンスをJSONで取得
data = response.json()

# 必要なデータを取得
    # ここではTime Series (Daily)内要素を取得
time_series = data['Time Series (Daily)']
# データフレームに変換
    # JavaでいうMap<Key, Value>をTableの見た目に。Map = time_series, orientはKeyを行のID？に, dtypeはValueの型
df = pd.DataFrame.from_dict(time_series, orient='index', dtype=float)

# # カラム名をわかりやすく変更
    # もともと設定されているため今回は不要
# df.columns = ['Open', 'High', 'Low', 'Close', 'Volume']

# インデックスを日付として設定
    # Key(String)をKey(datatime)に変換
df.index = pd.to_datetime(df.index)

# head()はDataFrameの上位行を表示
    # 表示が自動省略される
    # len(df)で行数
print(df.head())

# ------------

# # 特定の行を取得（例: 最初の行）
    # row = df.iloc[0]
    # print(row)

# # 範囲指定して複数行を取得（例: 最初の2行）
    # rows = df.iloc[0:2]
    # print(rows)

# 最大値の取得
    # max_value = df['Close'].max()
    # print(f"Closeカラムの最大値: {max_value}")
# 各列の最大値
    # max_values = df.max()
    # print("各カラムの最大値:")
    # print(max_values)
# エラー発生時データ型確認
#     print(df.dtypes)  # 各カラムのデータ型を確認


# DataFrameにしない場合
# # 最初の1行（最新データ）のみを取得
# latestData_key = list(data["Time Series (Daily)"].keys())[0]
# latestData = data["Time Series (Daily)"][latestData_key]

# print("最新データ:", latestData_key, latestData)
# print("close", latestData["4. close"])