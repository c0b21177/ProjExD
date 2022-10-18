import tkinter as tk
import tkinter.messagebox as tkm
import maze_maker

def count_up():
    global tmr
    tmr = tmr + 1
    root.after(1000, count_up)

def key_down(event):
    key = event.keysym
    #tkm.showinfo("キー押下", f"{key}キーが押されました")
    root.after(1000, count_up)

def key_up(event):
    key = ""
    #tkm.showinfo("キー押下", f"{key}キーが押されました")
    root.after(1000, count_up)

def main_proc():
    global key, cx, cy
    if key == "Up":
        cy -= 20
    elif key == "Down":
        cy += 20
    elif key == "Left":
        cx -= 20
    elif key == "Right":
        cx += 20
    canvas.coords("pic", cx, cy)
    root.after(1000, main_proc)

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("1500x900")
    root.title("迷えるこうかとん")

    cx, cy = 300, 400
    key = ""
    tmr = 0

    canvas = tk.Canvas(root, width = 1500, height = 900, bg = "BLACK")
    pic = tk.PhotoImage(file = "c:/Users/nokur/Desktop/ProjExD2022/ex03/fig/9.png")
    canvas.create_image(cx, cy, image = pic, tag = "pic")
    canvas.pack()

    #maze = maze_maker.make_maze(15,9)
    #maze_maker.show_maze(canvas, maze)

    root.bind("<KeyPress>", key_down)
    root.bind("<KeyRelease>", key_up)

    root.mainloop()