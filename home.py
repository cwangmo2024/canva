import tkinter as tk

root = tk.Tk()
root.title("My House")

canvas = tk.Canvas(root, width=400, height=400, bg="skyblue")
canvas.pack()

# Square body of the house
canvas.create_rectangle(100, 180, 300, 340, fill="khaki", outline="black", width=2)

# Triangle roof (three points: left, top, right)
canvas.create_polygon(80, 180, 200, 80, 320, 180, fill="firebrick", outline="black", width=2)

# Two small square windows
canvas.create_rectangle(120, 210, 160, 250, fill="lightyellow", outline="black", width=2)
canvas.create_rectangle(240, 210, 280, 250, fill="lightgreen", outline="black", width=2)

# Door
canvas.create_rectangle(175, 270, 225, 340, fill="saddlebrown", outline="black", width=2)

root.mainloop()