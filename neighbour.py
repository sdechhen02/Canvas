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

root.mainloop()