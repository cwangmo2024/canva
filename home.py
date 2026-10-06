import tkinter as tk

root = tk.Tk()
root.title("My House")

canvas = tk.Canvas(root, width=600, height=450, bg="skyblue")
canvas.pack()

# ---------- Ground (drawn first so everything sits on top) ----------
canvas.create_rectangle(0, 380, 600, 450, fill="forestgreen", outline="")

# ---------- Sun ----------
canvas.create_oval(30, 20, 110, 100, fill="gold", outline="orange", width=2)

# ---------- Cloud (overlapping white ovals) ----------
canvas.create_oval(380, 50, 450, 90, fill="white", outline="")
canvas.create_oval(420, 35, 500, 85, fill="white", outline="")
canvas.create_oval(465, 50, 535, 90, fill="white", outline="")
canvas.create_oval(410, 60, 490, 100, fill="white", outline="")

# ---------- House ----------
# Square body (200 x 200)
canvas.create_rectangle(100, 180, 300, 380, fill="khaki", outline="black", width=2)

# Triangle roof
canvas.create_polygon(80, 180, 200, 80, 320, 180, fill="firebrick", outline="black", width=2)

# Two small square windows (different colors)
canvas.create_rectangle(120, 210, 160, 250, fill="lightyellow", outline="black", width=2)
canvas.create_rectangle(240, 210, 280, 250, fill="lightgreen", outline="black", width=2)

# Door
canvas.create_rectangle(175, 310, 225, 380, fill="saddlebrown", outline="black", width=2)

# ---------- Dog house ----------
# Body
canvas.create_rectangle(340, 330, 420, 380, fill="peru", outline="black", width=2)
# Roof
canvas.create_polygon(330, 330, 380, 295, 430, 330, fill="sienna", outline="black", width=2)
# Entrance
canvas.create_rectangle(368, 350, 392, 380, fill="black", outline="black")

# ---------- Tree ----------
# Trunk
canvas.create_rectangle(480, 300, 510, 380, fill="saddlebrown", outline="black", width=2)
# Leaves
canvas.create_oval(445, 200, 545, 320, fill="darkgreen", outline="black", width=2)

root.mainloop()