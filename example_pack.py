import tkinter as tk


def print_number(number):
    print(f"Clicked button {number}")


root = tk.Tk()
window_width = 400
window_height = 300
root.geometry(f"{window_width}x{window_height}")

# Set button dimensions
button_width = 20
button_height = 2

button1 = tk.Button(
    root,
    text="Click here for number 1",
    width=button_width,
    height=button_height,
    command=lambda: print_number(1),
)
button1.pack()

button2 = tk.Button(
    root,
    text="Click here for number 2",
    width=button_width,
    height=button_height,
    command=lambda: print_number(2),
)
button2.pack()

button3 = tk.Button(
    root,
    text="Click here for number 3",
    width=button_width,
    height=button_height,
    command=lambda: print_number(3),
)
button3.pack()

root.mainloop()
