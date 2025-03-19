import requests
import pandas

def get_close(symbol) :
    url = f'https://www.alphavantage.co/query'
    # デイリーの取得
    params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": "",
        "apikey": "demo",
    }
    params["symbol"] = symbol
    
    try:
        # APIリクエストを送信、レスポンスをJSONで取得
        response = requests.get(url, params=params)
        data = response.json()

        # エラーが含まれるか確認
        if "Error Message" in data:
            return f"エラー: 指定されたシンボル '{symbol}' が無効です。"
        elif "Note" in data:
            return"注意: APIの呼び出し制限を超えています。少し時間を空けて再試行してください。"

        # 必要なデータを取得
        time_series = data['Time Series (Daily)']
        if not time_series:
            return "エラー: データが見つかりません。time_seriesが間違っている可能性があります。"

        # 最初の1行（最新データ）のみを取得
        latestData_key = next(iter(time_series.keys()))
        latestData = time_series[latestData_key]

        # データフレームを使用する場合
        # df = pandas.DataFrame.from_dict(time_series, orient='index', dtype=float)

        # # 前日のデータのみ取得
        # latestData = df.iloc[0]
        # print(latestData)
        # print("close", latestData["4. close"])
        
        return latestData["4. close"]
    
    except requests.exceptions.RequestException as e:
        # ネットワークエラーなどの例外をキャッチ
        return f"リクエストエラーが発生しました: {e}"
    except KeyError as e:
        # 必要なデータが存在しない場合のエラーをキャッチ
        return f"データエラー: 必要な情報が見つかりません。詳細: {e}"