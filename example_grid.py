import tkinter as tk


def print_number(number):
    print(f"Clicked button {number}")


root = tk.Tk()

# Set window size
window_width = 400
window_height = 300
root.geometry(f"{window_width}x{window_height}")

# Calculate button dimensions based on window width
button_width = window_width // 2
button_height = window_height // 3

button1 = tk.Button(root, text="Click here for number 1", command=lambda: print_number(1))
button1.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

button2 = tk.Button(root, text="Click here for number 2", command=lambda: print_number(2))
button2.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

button3 = tk.Button(root, text="Click here for number 3", command=lambda: print_number(3))
button3.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")

# Configure grid weights to make buttons resizable
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_columnconfigure(0, weight=1)

# Set button dimensions
button1.config(width=button_width, height=button_height)
button2.config(width=button_width, height=button_height)
button3.config(width=button_width, height=button_height)

root.mainloop()
