import tkinter as tk
from datetime import datetime
import webbrowser

class NewYearCountdown:
    def __init__(self, root):
        self.root = root
        self.root.title("新年倒计时")

        window_width = 300
        window_height = 150

        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        x = (screen_width // 2) - (window_width // 2)
        y = (screen_height // 2) - (window_height // 2)

        self.root.geometry(f"{window_width}x{window_height}+{x}+{y}")

        self.label = tk.Label(root, text="", font=("Arial", 24))
        self.label.pack(expand=True)

        self.update_countdown()

    def update_countdown(self):
        now = datetime.now()

        if now.month == 1 and now.day == 1:
            self.label.config(text="Happy New Year! 🎉")
            self.open_webpage()  # 倒计时结束后打开网页
            return 0
        else:
            new_year = datetime(now.year + 0, 12, 31, 20, 32, 00)

            time_left = new_year - now

            days = time_left.days
            hours, remainder = divmod(time_left.seconds, 3600)
            minutes, seconds = divmod(remainder, 60)

            self.label.config(text=f"{days} 天 {hours} 小时 {minutes} 分钟 {seconds} 秒")

        self.root.after(1000, self.update_countdown)

    def open_webpage(self):
        # 在这里指定你想要打开的网页URL
        webbrowser.open("http://127.0.0.1:5000/")

if __name__ == "__main__":
    root = tk.Tk()
    app = NewYearCountdown(root)
    root.mainloop()