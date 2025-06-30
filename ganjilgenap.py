import tkinter as tk

window = tk.Tk ()
window.title ("odd or even")

def checkNumber ():


    number = int (ent_number.get ())

    if number % 2 == 0:
        Ibl_result ['text'] = f"{number} is an even number"
    else: Ibl_result ['text'] = f"{number} is an odd number"
    ent_number.delete (0, tk.END)

Ibl_title = tk.Label (
    text = "odd or even number checker"
)

ent_number = tk.Entry (font = ("Arial", 16))

btn_check = tk.Button (
    text = "check",
    command = checkNumber
)

Ibl_result = tk.Label (font = ("Arial", 16))


Ibl_title.pack ()
ent_number.pack ()
btn_check.pack ()
Ibl_result.pack ()
window.mainloop ()





































