import tkinter as tk

root = tk.Tk()

root.geometry("600x450")
root.title("My First Canvas")

canvas = tk.Canvas(root, width=550, height=360, bg="skyblue")
canvas.pack()


# HOUSE
canvas.create_rectangle(180, 170, 350, 300, fill="coral")

canvas.create_polygon(
    160, 170,
    265, 90,
    370, 170,
    fill="brown"
)

canvas.create_rectangle(
    240, 230, 290, 300,
    fill="darkblue"
)


# DOG HOUSE
canvas.create_rectangle(
    390, 245, 490, 300,
    fill="orange"
)

canvas.create_polygon(
    375, 245,
    440, 195,
    505, 245,
    fill="red"
)

canvas.create_rectangle(
    425, 265, 455, 300,
    fill="brown"
)


# TREE
canvas.create_rectangle(
    70, 200, 100, 300,
    fill="brown"
)

canvas.create_oval(
    30, 130, 140, 230,
    fill="green"
)

canvas.create_oval(
    55, 100, 155, 200,
    fill="green"
)


# SUN
canvas.create_oval(
    460, 40, 530, 110,
    fill="yellow"
)


# CLOUD
canvas.create_oval(
    80, 40, 140, 85,
    fill="white"
)

canvas.create_oval(
    110, 25, 180, 85,
    fill="white"
)

canvas.create_oval(
    145, 40, 205, 85,
    fill="white"
)


root.mainloop()