# main.py
import threading

from src.app import App
from src.nfc_reader import Reader


class Run:
    def __init__(self):
        self.app = App()
        # self.reader_thread_start()
        # self.update_label()
        self.app.mainloop()

    def reader_thread_start(self):
        self.reader = Reader()
        self.reader_thread = threading.Thread(target=self.reader.check_loop)
        self.reader_thread.start()

    def update_label(self):
        try:
            if self.reader.on is True:
                App.main_text.set(self.reader.txt)
                print("on")
            else:
                App.main_text.set("タッチしてください")
                print("off")
        except Exception:
            App.main_text.set("ボタンを押してください")
        self.app.after(100, self.update_label)


if __name__ == "__main__":
    run = Run()
