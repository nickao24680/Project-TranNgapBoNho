import tkinter as tk
import random
import threading
import time

def dow():
    window = tk.Tk()
    width = window.winfo_screenwidth()
    height = window.winfo_screenheight()
    a = random.randrange(0, width)
    b = random.randrange(0, height)
    window.title('Nguyễn Văn Đức (ADMIN)')
    window.geometry("333x50" + "+" + str(a) + "+" + str(b))
    tk.Label(window,
             text='I LOVE YOU', # Label text
             bg='pink', # Background Color
             font=('Kaiti', 24), # Font and font size
             width=50, height=40 # Label length and width
             ).pack() # Fixed window position
    window.mainloop()

threads = []
for i in range(100): # The number of pop-ups required
    t = threading.Thread(target=dow)
    threads.append(t)
    time.sleep(0.01)
    threads[i].start()