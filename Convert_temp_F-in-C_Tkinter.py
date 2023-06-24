# Temperature conversion from Fahrenheit to Celsius - Tkinter

from tkinter import *

def convert():
	fahrenheit = ent_temperature.get()
	celsius = (5 / 9) * (float(fahrenheit) - 32)
	lbl_result['text'] = f'{round(celsius, 2)} \N{DEGREE CELSIUS}'

root = Tk()
root.title('TempConverter')

frm_entry = Frame(master=root)
frm_entry.grid(column=0, row=0, padx=10)
ent_temperature = Entry(master=frm_entry, width=10)
ent_temperature.grid(column=0, row=0, sticky='e')
lbl_fahrenheit = Label(master=frm_entry, text='\N{DEGREE FAHRENHEIT}')
lbl_fahrenheit.grid(column=1, row=0, sticky='w')

btn_convert = Button(text='\N{RIGHTWARDS BLACK ARROW}', command=convert)
btn_convert.grid(column=2, row=0, pady=10)

lbl_result = Label(text='\N{DEGREE CELSIUS}')
lbl_result.grid(column=3, row=0, padx=10)

root.mainloop()