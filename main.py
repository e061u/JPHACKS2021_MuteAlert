''' Quoted from https://qiita.com/hima_zin331/items/97fc5c9093057bb06572 '''

from pywinauto import Application
import pywinauto

import time
from tkinter import messagebox

def captureZoom():
    while True:
        try:
            # Zoomミーティングウィンドウ情報取得
            zoom = Application(backend="uia").connect(best_match=u"Zoom ミーティング")
            break
        except pywinauto.findbestmatch.MatchError: # Zoomミーティング入室していない -> 再取得
            continue

    messagebox.showinfo('確認', 'ミュートを確認してください．')

    # Zoom Client閉じる
    zoom = Application(backend="uia").connect(best_match=u"Zoom ミーティング")
    if zoom[u"Zoom ミーティング"].exists():
        zoom[u"Zoom ミーティング"].set_focus()
        pywinauto.keyboard.send_keys("%{F4}")
        pywinauto.keyboard.send_keys("{ENTER}")

def main():
    try:
        captureZoom()
    except pywinauto.findbestmatch.MatchError: # ターゲットが見つからなかった -> 再試行
        print("The dialog was not found. Retrying...")
        main()
    except pywinauto.findwindows.ElementNotFoundError: # ターゲットが見つからなかった -> 再試行
        print("The dialog was not found. Retrying...")
        main()

if __name__ == '__main__':
    main()