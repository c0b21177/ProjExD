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
    cx = mx*100 + 50
    cy = my*100 + 50

    if key == "Shift_L":
        mx = 1
        my = 1

    canvas.coords("pic", cx, cy)
    root.after(100, main_proc)

def count_down():
    global tmr
    tmr = tmr-1
    label["text"] = tmr
    if tmr <= 0:
        label["text"] = "TIME OVER"
        root.unbind("<KeyPress>")
        root.unbind("<KeyRelease>")
    elif mx == 13 and my == 7:
        label["text"] = "GAME CLEAR"
        root.unbind("<KeyPress>")
        root.unbind("<KeyRelease>")
        return()
    root.after(1000, count_down)


if __name__ == "__main__":
    root = tk.Tk()
    #root.geometry("1500x900")
    root.title("迷えるこうかとん")

    mx, my = 1, 1
    cx, cy = mx*100 + 50, my*100 + 50
    key = ""
    ask = ""
    tmr = 11

    canvas = tk.Canvas(root, width = 1500, height = 900, bg = "BLACK")
    maze = maze_maker.make_maze(15,9)
    maze_maker.show_maze(canvas, maze)
    pic = tk.PhotoImage(file = "fig/9.png")
    canvas.create_image(cx, cy, image = pic, tag = "pic")
    label = tk.Label(root, font = ("", 80))
    label.pack()
    root.after(1000, count_down)
    canvas.pack()

    root.bind("<KeyPress>", key_down)
    root.bind("<KeyRelease>", key_up)

    main_proc()

    root.mainloop()