import tkinter as tk


def add_item(name_entry, category_variable):
    item_name = name_entry.get()
    category = category_variable.get()

    print("Clothing item:", item_name)
    print("Category:", category)


def open_add_item():
    add_window = tk.Toplevel(window)

    add_window.title("Add Clothing Item")
    add_window.geometry("400x400")

    label = tk.Label(
        add_window,
        text="Add a Clothing Item",
        font=("Arial", 18)
    )

    label.pack(pady=20)

    name_label = tk.Label(
        add_window,
        text="Name:"
    )

    name_label.pack()

    name_entry = tk.Entry(add_window)

    name_entry.pack()

    category_label = tk.Label(
        add_window,
        text="Category:"
    )

    category_label.pack()

    categories = [
        "Shirt",
        "Pants",
        "Dress",
        "Jacket",
        "Shoes",
        "Accessory"
    ]

    category_variable = tk.StringVar(add_window)

    category_variable.set("Shirt")

    category_menu = tk.OptionMenu(
        add_window,
        category_variable,
        *categories
    )

    category_menu.pack()

    add_button = tk.Button(
        add_window,
        text="Add Item",
        command=lambda: add_item(name_entry, category_variable)
    )

    add_button.pack(pady=10)
window = tk.Tk()
window .title("My Closet")
window.geometry("800x600")
#---------
#Header
#---------


header = tk.Frame(window)
header.pack(fill="x")

title = tk.Label(
    header,
    text="MY CLOSET",
    font=("Arial", 24)
)

title.pack(pady=20)

#---------
#Navigation
#---------

navigation = tk.Frame(window)
navigation.pack(fill="x")

clothes_button = tk.Button(
    navigation,
    text="My Clothes"
)

clothes_button.pack(side="left", padx=10)

outfits_button = tk.Button(
    navigation,
    text="Outfits"
)

outfits_button.pack(side="left", padx=10)

add_button = tk.Button(
    navigation,
    text="Add Item",
    command=open_add_item
)

add_button.pack(side="left", padx=10)

#---------
#Content
#---------
content = tk.Frame(window)
content.pack(fill="both", expand=True)

welcome = tk.Label(
    content,
    text="Your clothing collection will appear here.",
    font=("Arial", 16)
)

welcome.pack(pady=100)
#--------
#start the main loop
#--------
window.mainloop()
