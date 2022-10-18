import tkinter as tk
import tkinter.messagebox as tkm
import maze_maker

def key_down(event):
    global key
    key = event.keysym
    #tkm.showinfo("キー押下", f"{key}キーが押されました")

def key_up(event):
    global key
    key = ""
    #tkm.showinfo("キー押下", f"{key}キーが押されました")

def main_proc():
    global cx, cy
    if key == "Up":
        cy -= 20
    elif key == "Down":
        cy += 20
    elif key == "Left":
        cx -= 20
    elif key == "Right":
        cx += 20
    canvas.coords("pic", cx, cy)
    root.after(100, main_proc)

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("1500x900")
    root.title("迷えるこうかとん")

    cx, cy = 300, 400
    key = ""

    canvas = tk.Canvas(root, width = 1500, height = 900, bg = "BLACK")
    pic = tk.PhotoImage(file = "fig/9.png")
    canvas.create_image(cx, cy, image = pic, tag = "pic")
    canvas.pack()

    maze = maze_maker.make_maze(15,9)
    maze_maker.show_maze(canvas, maze)

    root.bind("<KeyPress>", key_down)
    root.bind("<KeyRelease>", key_up)

    main_proc()

    root.mainloop()