import tkinter as tk

window = tk.Tk ()
window.title ("my applications")


window.geometry ("400x200")


window ['bg'] = 'blue'



icon = tk.PhotoImage (file = 'download.png')
window.tk.call ('wm', 'iconphoto', window._w, icon)


label = tk.Label (text = "calculator")
label.pack ()
window.mainloop ()




























