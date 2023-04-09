# main.py
import threading
import tkinter as tk

import src.nfc_reader as nfc_reader

FONT = "Noto Sans JP"


class App:
    def __init__(self):
        self.root = tk.Tk()
        # ラベルの設定--------------------------------
        self.labe_text = tk.StringVar()
        self.labe_text.set("表示ラベル")
        self.label = tk.Label(textvariable=self.labe_text, font=(FONT, 48))
        # ------------------------------------------
        self.label.pack()
        # NFCリーダーをチェックするスレッド
        self.reader_thread_start()
        self.update_label()
        self.root.mainloop()

    def reader_thread_start(self):
        self.reader = nfc_reader.Reader()
        self.reader_thread = threading.Thread(target=self.reader.check_loop)
        self.reader_thread.start()
        self.labe_text.set("タッチしてください")

    def update_label(self):
        try:
            if self.reader.on is True:
                self.labe_text.set(self.reader.txt)
                print("on")
            else:
                self.labe_text.set("タッチしてください")
                print("off")
        except Exception:
            self.labe_text.set("ボタンを押してください")
        self.root.after(100, self.update_label)


app = App()
