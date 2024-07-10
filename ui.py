import tkinter as tk

from structures import Storage


class Application(tk.Tk):
    def __init__(self, storage: Storage):
        super().__init__()

        self.title("Статистика заявок")
        self.geometry("300x80")
        self.storage = storage
        self.total_label = tk.Label(self, text="-")
        self.total_label.pack(pady=10)

        self.hourly_label = tk.Label(self, text="-")
        self.hourly_label.pack()
        self.protocol("WM_DELETE_WINDOW", self.__on_closing)
        self.__value_handler()

    def __value_handler(self):
        self.update_labels(*self.storage.get())
        self.after(1000, self.__value_handler)

    def update_labels(self, total_count: int, hourly_count: int):
        self.total_label.config(text=f"Общее количество заявок: {total_count}")
        self.hourly_label.config(text=f"Заявок по текущему часу: {hourly_count}")

    def __on_closing(self):
        self.destroy()

