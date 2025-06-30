import tkinter as tk
window = tk.Tk()
window.title("My Aplication")
window.geometry("400x200")


label = tk.Label(text = "Tkinter Button widget")
button = tk.Button(
    text = "Blue Button",
    bg ="blue", fg = "white",
    height= 5, width= 15,
    font= ("Arial",16),
)
label.pack()
button.pack()
# icon = tk.PhotoImage(file='download.png') 
# window.tk.call('wm', 'iconphoto', window._w, icon)
#  entry = tk.Entry (
#      font = ("Arial", 16)
# )
# entry.pack ()
# text_box = tk.Text (
#     font = ("Arial", 16),
#     width = 25,
#     height = 5
# )
# text_box.pack ()
# frame_title = tk.Frame (
#     master = window,
#     height = 100, width= 400,
#     bg = "blue"
# )
# frame_desc = tk.Frame (
#     master = window,
#     height = 50, width=250,
#     bg = "red"
# )
#label_title = tk.Label (
    #master = frame_title,
    #text = "my application",
    #font = ("Arial", 25),
#)
#label_title.pack ()
# label_disc = tk.Label (
#     master = window,
#     text = "descriptions here",
# )
# label_disc.pack ()
# frame_title.pack()
# frame_desc.pack()
# frame_title.pack (fill = tk.X)

frame_title = tk.Frame (
    width = 250,
    master = window,
    bg = "blue"
)
frame_desc = tk.Frame (
    width = 250,
    master = window,
    bg = "red"
)

frame_title.pack(fill= tk.Y,side= tk.LEFT)
frame_desc.pack(fill= tk.Y,side= tk.LEFT)
window.mainloop ()




