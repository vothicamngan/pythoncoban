import tkinter as tk

def menu_item_clicked(item):
    # Replace this with the action you want to perform for each menu item
    print(f"Clicked: {item}")

# Create the main window
root = tk.Tk()
root.title("Left Menu Example")

# Create a left menu frame
left_menu = tk.Frame(root, width=150, bg='lightgray')
left_menu.pack(side=tk.LEFT, fill=tk.Y)

# Add menu items (buttons in this case)
menu_items = ["Item 1", "Item 2", "Item 3", "Item 4"]

for item in menu_items:
    button = tk.Button(left_menu, text=item, width=15, command=lambda i=item: menu_item_clicked(i))
    button.pack(pady=5)

# Create a content frame to display the main content
content_frame = tk.Frame(root, width=400, height=300, bg='white')
content_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

# Add content to the content frame (replace this with your actual content)
label = tk.Label(content_frame, text="Main Content Area", font=('Helvetica', 16))
label.pack(pady=50)

# Start the Tkinter event loop
root.mainloop()
