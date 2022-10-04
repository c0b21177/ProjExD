import tkinter as tk
import tkinter.messagebox as tkm

def button_click(event):
    btn = event.widget
    txt = btn["text"]
    tkm.showwarning("txt", f"{txt}のボタンがクリックされました")

root = tk.Tk()
root.geometry("300x500")
root.title("電卓")

num_r = 0
num_c = 0

for i in range(9, -1, -1):
    btn = tk.Button(root, text =f"{i}", font = ("Times New Roman", 30), width = "4", height = "2", command = button_click)
    btn.grid(row = num_r+4*i, column= num_c+2*i)
    if num_r > 12:
        num_r = 0
    if num_c > 4:
        num_c = 0


#button_9 = tk.Button(root, text = "9", font = ("Times New Roman", 30), width = "4", height = "2", command = button_click)
#button_9.grid(row = "0", column = "0")

#button_8 = tk.Button(root, text = "8", font = ("Times New Roman", 30), width = "4", height = "2", command = button_click)
#button_8.grid(row = "0", column = "2")

#button_7 = tk.Button(root, text = "7", font = ("Times New Roman", 30), width = "4", height = "2", command = button_click)
#button_7.grid(row = "0", column = "4")

#button_6 = tk.Button(root, text = "6", font = ("Times New Roman", 30), width = "4", height = "2", command = button_click)
#button_6.grid(row = "4", column = "0")

#button_5 = tk.Button(root, text = "5", font = ("Times New Roman", 30), width = "4", height = "2", command = button_click)
#button_5.grid(row = "4", column = "2")

#button_4 = tk.Button(root, text = "4", font = ("Times New Roman", 30), width = "4", height = "2", command = button_click)
#button_4.grid(row = "4", column = "4")

#button_3 = tk.Button(root, text = "3", font = ("Times New Roman", 30), width = "4", height = "2", command = button_click)
#button_3.grid(row = "8", column = "0")

#button_2 = tk.Button(root, text = "2", font = ("Times New Roman", 30), width = "4", height = "2", command = button_click)
#button_2.grid(row = "8", column = "2")

#button_1 = tk.Button(root, text = "1", font = ("Times New Roman", 30), width = "4", height = "2", command = button_click)
#button_1.grid(row = "8", column = "4")

#button_0 = tk.Button(root, text = "0", font = ("Times New Roman", 30), width = "4", height = "2", command = button_click)
#button_0.grid(row = "12", column = "0")


root.mainloop()
