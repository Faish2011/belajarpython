import tkinter as tk
window = tk.Tk()
window.title("My Aplication")
window.geometry("400x200")
icon = tk.PhotoImage(file='download.png') 
window.tk.call('wm', 'iconphoto', window._w, icon)
label = tk.Label(text = "Tkinter Button widget")
button = tk.Button(
    text = "Blue Button",
    bg ="blue", fg = "white",
    height= 5, width= 15,
    font= ("Arial",16),
    )
label.pack()
button.pack()


entry = tk.Entry (
    font = ("Arial", 16)
)

entry.pack ()


text_box = tk.Text (
    font = ("Arial", 16),
    width = 25,
    height = 5
)
text_box.pack ()


frame_title = tk.Frame ()
frame_disc = tk.Frame ()

label_title = tk.Label (
    master = frame_title,
    text = "my application",
    font = ("Arial", 25),
)

label_title.pack ()

label_disc = tk.Label (
    master = frame_disc,
    text = "descriptions here",
)
label_disc.pack ()

frame_title.pack ()
frame_disc.pack ()
window.mainloop()
















