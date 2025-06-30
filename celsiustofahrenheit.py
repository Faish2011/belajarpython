import tkinter as tk

window = tk.Tk()
window.title("Temperature Converter")
window.geometry("300x200")

def convert_temperature ():
    try:
        celsius = float (entry_temperature.get())
        fahrenheit = (celsius * 9/5) + 32
        label_result ['text'] = f"{celsius}C = {fahrenheit:.2f}F"
    except ValueError:
        label_result ['text'] = "please enter a valid number"
    entry_temperature.delete (0, tk.END)

label_title = tk.Label (text ="celsius to fahrenheit", font = ("Arial", 14))
entry_temperature = tk.Entry (font = ("Arial, 12"))
button_convert = tk.Button (
    text = "convert",
    command = convert_temperature,
    font = ("Arial", 12)
)

label_result = tk.Label (font = ("Arial", 12))
label_title.pack (pady = 10)
entry_temperature.pack (pady = 5)
button_convert.pack (pady = 5)
label_result.pack (pady = 10)
window.mainloop ()







































