import tkinter as tk

# Create window
window = tk.Tk()
window.title("My House")
window.geometry("900x600")

# Create Canvas
canvas = tk.Canvas(window, width=900, height=600, bg="skyblue")
canvas.pack()

# -------------------------
# GROUND
# -------------------------
canvas.create_rectangle(
    0, 450, 900, 600,
    fill="lightgreen",
    outline=""
)

# -------------------------
# HOUSE BODY
# -------------------------
canvas.create_rectangle(
    250, 250, 650, 450,
    fill="lightyellow",
    outline="black",
    width=3
)

# -------------------------
# ROOF
# -------------------------
canvas.create_polygon(
    200, 250,
    450, 100,
    700, 250,
    fill="red",
    outline="black",
    width=3
)

# -------------------------
# DOOR
# -------------------------
canvas.create_rectangle(
    400, 340, 500, 450,
    fill="brown",
    outline="black",
    width=3
)

# Door knob
canvas.create_oval(
    475, 395, 485, 405,
    fill="yellow",
    outline="black"
)

# -------------------------
# LEFT WINDOW
# -------------------------
canvas.create_rectangle(
    290, 300, 370, 370,
    fill="lightblue",
    outline="black",
    width=3
)

# Window cross
canvas.create_line(
    330, 300, 330, 370,
    fill="black",
    width=2
)

canvas.create_line(
    290, 335, 370, 335,
    fill="black",
    width=2
)

# -------------------------
# RIGHT WINDOW
# -------------------------
canvas.create_rectangle(
    530, 300, 610, 370,
    fill="lightblue",
    outline="black",
    width=3
)

# Window cross
canvas.create_line(
    570, 300, 570, 370,
    fill="black",
    width=2
)

canvas.create_line(
    530, 335, 610, 335,
    fill="black",
    width=2
)




# CLOUDS
# -------------------------
canvas.create_oval(150, 100, 210, 145, fill="white", outline="")
canvas.create_oval(180, 80, 250, 145, fill="white", outline="")
canvas.create_oval(220, 100, 280, 145, fill="white", outline="")


# TITLE
# -------------------------
canvas.create_text(
    450, 40,
    text="MY HOUSE",
    font=("Arial", 24, "bold"),
    fill="black"
)

# Keep window open
window.mainloop()