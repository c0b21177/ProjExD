import tkinter as tk
import tkinter.messagebox as tkm

def button_click(event):
    btn = event.widget
    txt = btn["text"]
    #tkm.showwarning("txt", f"{txt}のボタンがクリックされました")
    entry.insert(tk.END, txt)

def click_equal(event):
    eqn = entry.get()
    res = eval(eqn)
    entry.delete(0, tk.END)
    entry.insert(tk.END, res)

def allclear(event):
    entry.delete(0, tk.END)
    
root = tk.Tk()
root.geometry("340x500")
root.title("電卓")

num_r = 1
num_c = 0

numbers = list(range(9, 0, -1))
operators = [".","0","*","+","-","/"]
for i, num in enumerate(numbers + operators, 1):
    btn = tk.Button(root, text =f"{num}", font = ("", 30), width = "5", height = "1", command = button_click)
    btn.bind("<1>", button_click)
    btn.grid(row =num_r, column=num_c)
    num_c += 1

    if i%3 == 0:
        num_r += 1
        num_c = 0
    
btn = tk.Button(root, text= "=", font = ("", 30), width = "5", height = "1")
btn.bind("<1>", click_equal)
btn.grid(row = num_r, column = num_c)

acbtn = tk.Button(root, text = "AC", font = ("", 30), width = "5", height = "1")
acbtn.bind("<1>", allclear)
btn.grid(row = num_r, column = num_c)

entry = tk.Entry(root, bg = "BLACK", fg = "WHITE",  width = 10, font = (", 40"), justify = "right")
entry.grid(row = 0, column= 0,columnspan=3)

root.mainloop()
