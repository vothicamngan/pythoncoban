import tkinter as tk

root = tk.Tk()

entry = tk.Entry(root)
entry.pack()

# Now you can use entry.get() without encountering 'NoneType' error
entry_value = entry.get()

print(entry_value)

root.mainloop()