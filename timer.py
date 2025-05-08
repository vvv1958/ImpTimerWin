import tkinter as tk
from tkinter import ttk
import time

class IntervalTimer:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Interval Timer")
        self.window.geometry("300x250")
        
        # Настройки таймера
        self.is_running = False
        self.time_left = 0
        
        # Стиль интерфейса
        self.style = ttk.Style()
        self.style.configure("TButton", font=("Arial", 12), padding=10)
        self.style.configure("TLabel", font=("Arial", 20), background="#f0f0f0")
        
        # Элементы интерфейса
        self.label = ttk.Label(self.window, text="00:00")
        self.label.pack(pady=20)
        
        self.entry_frame = ttk.Frame(self.window)
        self.entry_frame.pack(pady=10)
        
        self.minutes_entry = ttk.Entry(self.entry_frame, width=3, font=("Arial", 14))
        self.minutes_entry.insert(0, "1")
        self.minutes_entry.pack(side="left", padx=5)
        
        ttk.Label(self.entry_frame, text="мин").pack(side="left", padx=5)
        
        self.seconds_entry = ttk.Entry(self.entry_frame, width=3, font=("Arial", 14))
        self.seconds_entry.insert(0, "0")
        self.seconds_entry.pack(side="left", padx=5)
        
        ttk.Label(self.entry_frame, text="сек").pack(side="left", padx=5)
        
        self.start_button = ttk.Button(self.window, text="Старт", command=self.start_timer)
        self.start_button.pack(pady=5)
        
        self.stop_button = ttk.Button(self.window, text="Стоп", command=self.stop_timer, state=tk.DISABLED)
        self.stop_button.pack(pady=5)
        
    def start_timer(self):
        if not self.is_running:
            try:
                minutes = int(self.minutes_entry.get())
                seconds = int(self.seconds_entry.get())
                self.time_left = minutes * 60 + seconds
                self.is_running = True
                self.start_button.config(state=tk.DISABLED)
                self.stop_button.config(state=tk.NORMAL)
                self.update_timer()
            except:
                self.label.config(text="Ошибка!")
        
    def stop_timer(self):
        self.is_running = False
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)
        self.label.config(text="00:00")
        
    def update_timer(self):
        if self.is_running and self.time_left > 0:
            mins = self.time_left // 60
            secs = self.time_left % 60
            self.label.config(text=f"{mins:02d}:{secs:02d}")
            self.time_left -= 1
            self.window.after(1000, self.update_timer)
        elif self.time_left == 0:
            self.stop_timer()
            self.label.config(text="Время вышло! ⏰")

app = IntervalTimer()
app.window.mainloop()