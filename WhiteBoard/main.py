import tkinter as tk

class Whiteboard:
    def __init__(self, master):
        self.master = master
        master.title("Whiteboard")

        self.canvas = tk.Canvas(master, width=500, height=400, bg="white")
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.pen_color = "black"
        self.eraser_on = False

        self.canvas.bind("<B1-Motion>", self.draw)  # Left mouse button for drawing

        self.create_tools()

    def create_tools(self):
        # Create a frame for tools
        tools_frame = tk.Frame(self.master)
        tools_frame.pack(side=tk.LEFT, fill=tk.Y)

        # Create buttons for pen, eraser, and color picker
        tk.Button(tools_frame, text="Pen", command=self.use_pen).pack()
        tk.Button(tools_frame, text="Eraser", command=self.use_eraser).pack()
        tk.Button(tools_frame, text="Color", command=self.choose_color).pack()

    def use_pen(self):
        self.eraser_on = False

    def use_eraser(self):
        self.eraser_on = True

    def choose_color(self):
        color = tk.colorchooser.askcolor()[1]
        if color:
            self.pen_color = color

    def draw(self, event):
        if self.eraser_on:
            self.canvas.create_rectangle(event.x - 5, event.y - 5,
                                          event.x + 5, event.y + 5,
                                          fill="white", outline="white")
        else:
            self.canvas.create_oval(event.x - 5, event.y - 5,
                                    event.x + 5, event.y + 5,
                                    fill=self.pen_color, outline=self.pen_color)

root = tk.Tk()
whiteboard = Whiteboard(root)
root.mainloop()