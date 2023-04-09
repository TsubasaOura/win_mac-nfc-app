from customtkinter import CTk, CTkButton
from src.components.settings import SettingsWindow


class App(CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("500x400")
        self.title("App")
        self.size()

        self.settings_button = CTkButton(self, text="open settings", command=self.open_settings)
        self.settings_button.pack(side="top", padx=20, pady=20)

        self.settings_window = None

    def open_settings(self):
        if self.settings_window is None or not self.settings_window.winfo_exists():
            self.settings_window = SettingsWindow(self)  # create window if its None or destroyed
        else:
            self.settings_window.focus()  # if window exists focus it
