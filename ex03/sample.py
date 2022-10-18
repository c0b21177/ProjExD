from itertools import count
import tkinter as tk

def count_up():
    global tmr
    tmr = tmr+1
    label["text"] = tmr
    root.after(1000, count_up)

if __name__ == "__main__":
    root = tk.Tk()
    label = tk.Label(root, font = ("", 80))
    label.pack()

    tmr = 0
    root.after(1000, count_up)
    root.mainloop()