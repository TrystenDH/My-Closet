import tkinter as tk

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
    text="Add Item"
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
