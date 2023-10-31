import tkinter as tk

def button_click(button_text):
    current = entry.get()
    entry.delete(0, tk.END)
    if(button_text != "="):
        entry.insert(tk.END, current + button_text)
    else:
        print(current)
        calculate(current)
    if(button_text == "Clear"):
        clear_entry()

def clear_entry():
    entry.delete(0, tk.END)

def calculate(value):
    try:
        result = eval(value)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        print(e)
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

root = tk.Tk()
root.geometry("300x200")
root.title("Calculator")

entry = tk.Entry(root, width=200, font=('Time', 16), justify='right')
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    '1', '2', '3', '+',
    '4', '5', '6', '-',
    '7', '8', '9', '*',
    '0', 'Clear', '=', '/',
    '.'
]

row_val = 1
col_val = 0

for button in buttons:
    tk.Button(root, text=button, width=5, height=2, command=lambda b=button: button_click(b)).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

for i in range(6):
    root.grid_rowconfigure(i, weight=1)
    root.grid_columnconfigure(i, weight=1)
    
root.mainloop()