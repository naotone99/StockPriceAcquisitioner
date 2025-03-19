import LatestDate
import Monthly
from datetime import datetime, timedelta
import tkinter

# メインウィンドウ
root = tkinter.Tk()
root.title("StockPriceAcquisitioner")
root.geometry("300x150")

label = tkinter.Label(root, text = "検索したい銘柄を入力")
label.pack(pady = 5)
entry = tkinter.Entry(root, width = 30)
entry.pack(pady = 5)

# ダイアログの管理
dialogs = []

# カスタムダイアログ
def create_dialog(title, maxValue, close, yesterday):
    dialog = tkinter.Toplevel(root) #新ウィンドウ
    dialog.title(title)
    dialog.geometry("200x100")

    rate = (float(close) / float(maxValue)) * 100 - 100
    label_rate = tkinter.Label(dialog, text = f'騰落率: {rate}', wraplength = 180)
    label_maxValue = tkinter.Label(dialog, text = f"最大値: {maxValue}", wraplength = 180) 
    label_close = tkinter.Label(dialog, text = f"終値: {close}({yesterday})", wraplength = 180)
    #wraplength を設定することで、テキストの折り返しを有効に
    label_rate.pack(pady = 10)
    label_maxValue.pack()
    label_close.pack()
    dialogs.append(dialog)

# ボタンが押されたときの処理
def execute():
    user_input = entry.get()
    if user_input:
        # データの取得
        maxValue = Monthly.get_maxValue(user_input)
        close = LatestDate.get_close(user_input)

        # 前日の日付を計算
        yesterday = datetime.now() - timedelta(days=1)
        yesterday = yesterday.strftime('%Y-%m-%d')

        create_dialog(user_input, maxValue, close, yesterday)

    entry.delete(0, tkinter.END)

# 送信ボタン
button = tkinter.Button(root, text = "検索", command = execute)
button.pack(pady = 10)
root.bind('<Return>', lambda event: execute())
# enterで送信。lambdaを使う理由は、キーイベントオブジェクト(Enter)を受け取る必要があるため

# メインループ開始
root.mainloop()
# GUIアプリケーションは、常にユーザーの操作（クリック、キー入力など）を待ち受けています。
# このループがなければ、GUIウィンドウは一度表示された後すぐ終了してしまいます。
# ユーザーがウィンドウを閉じる、ボタンをクリックする、キーを押すなどの操作を行った際に、それに対応するイベントを処理します。
# アプリケーションが終了される（例: ウィンドウが閉じられる）まで、このループは続きます。