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
    global cx, cy, mx, my
    if key == "Up" and maze[my-1][mx] == 0:
        my -= 1
    elif key == "Down" and maze[my+1][mx] == 0:
        my += 1
    elif key == "Left" and maze[my][mx-1] == 0:
        mx -= 1
    elif key == "Right" and maze[my][mx+1] == 0:
        mx += 1
    cx = 50 + mx * 100
    cy = 50 + my * 100

    canvas.coords("pic", cx, cy)
    root.after(100, main_proc)

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("1500x900")
    root.title("迷えるこうかとん")

    mx, my = 1, 1
    cx, cy = 50 + mx * 100, 50 + my * 100
    key = ""

    canvas = tk.Canvas(root, width = 1500, height = 900, bg = "BLACK")
    maze = maze_maker.make_maze(15,9)
    print(maze)
    maze_maker.show_maze(canvas, maze)
    pic = tk.PhotoImage(file = "fig/9.png")
    canvas.create_image(cx, cy, image = pic, tag = "pic")
    canvas.pack()

    root.bind("<KeyPress>", key_down)
    root.bind("<KeyRelease>", key_up)

    main_proc()

    root.mainloop()