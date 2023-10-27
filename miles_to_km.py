import tkinter

window = tkinter.Tk()
window.minsize(height=100, width=300)
window.title("Miles to Km Converter")
window.config(padx=50, pady=50)

km_conversion = 0


def miles_to_km():
    miles = int(miles_entry.get())
    miles_to_km.km_conversion = round(miles*1.6, 2)
    conversion_label.config(text=miles_to_km.km_conversion)


miles_entry = tkinter.Entry(width=10)
miles_entry.grid(column=1, row=0)

miles_label = tkinter.Label(text="Miles")
miles_label.grid(column=2, row=0)

equal_label = tkinter.Label(text="is equal to:")
equal_label.grid(column=0, row=1)

conversion_label = tkinter.Label(text=f"{km_conversion}")
conversion_label.grid(column=1, row=1)

km_label = tkinter.Label(text="Km")
km_label.grid(column=2, row=1)

calc_button = tkinter.Button(text="Calculate", command=miles_to_km)
calc_button.grid(column=1, row=2)

window.mainloop()
