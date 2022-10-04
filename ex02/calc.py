import tkinter as tk
import tkinter.messagebox as tkm

def button_click(event):
    btn = event.widget
    txt = btn["text"]
    #tkm.showwarning("txt", f"{txt}のボタンがクリックされました")
    entry.insert(tk.END, txt)

root = tk.Tk()
root.geometry("300x500")
root.title("電卓")


num_r = 1
num_c = 0

numbers = list(range(9, -1, -1))
operators = ["+", "="]
for i, num in enumerate(numbers + operators, 1):
    btn = tk.Button(root, text =f"{num}", font = ("", 30), width = "4", height = "2", command = button_click)
    btn.bind("<1>", button_click)
    btn.grid(row =num_r, column=num_c)
    num_c += 1
    if i%3 == 0:
        num_r += 1
        num_c = 0

entry = tk.Entry(root,  width = 10, font = (", 40"), justify = "right")
entry.grid(row = 0, column= 0,columnspan=3)

root.mainloop()
