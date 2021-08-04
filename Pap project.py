from tkinter import *
units_value = {
    "cm" : 0.01,"m" : 1.0,"km": 1000.0,"feet": 0.3048,"miles": 1609.344,"inches": 0.0254,
    "grams" : 1.0,"kg" : 1000.0,"pounds" : 453.592,
    "sq. m" : 1.0,"sq. km": 1000000.0,"hectare" : 10000.0,"acre": 4046.856,
    "sq. mile" : 2590000.0,"sq. foot" : 0.0929,"cu. cm" : 0.001,"Litre" : 1.0,"ml" : 0.001
}

UNITS = ["SELECT","LENGTH","WEIGHT","TEMPERATURE","AREA","VOLUME"]

len_units = ["select unit","cm", "m", "km", "feet", "miles", "inches"]
weight_units = ["select unit","kg", "grams", "pounds",]
temp_units = ["select unit","Celsius", "Fahrenheit"]
area_units = ["select unit","sq. m", "sq. km", "hectare", "acre", "sq. mile", "sq. foot"]
volume_units = ["select unit","cu. cm", "Litre", "ml"]



tk_window = Tk()
tk_window.geometry("400x470")
tk_window.title("Unit Converter")
tk_window['bg'] = '#358597'



def un():
    unit = unitoption.get()
    if unit=="LENGTH":
        inputmenu = OptionMenu(tk_window, ipoption, *len_units)
        inputmenu.grid(row = 3, column = 1)
        inputmenu.config(font = "Arial 10", bg='#fcc3b6')

        outputmenu = OptionMenu(tk_window, opoption, *len_units)
        outputmenu.grid(row = 5, column = 1)
        outputmenu.config(font = "Arial 10", bg='#fcc3b6')

    elif unit == "WEIGHT":
        inputmenu = OptionMenu(tk_window, ipoption, *weight_units)
        inputmenu.grid(row = 3, column = 1)
        inputmenu.config(font = "Arial 10", bg='#fcc3b6')

        outputmenu = OptionMenu(tk_window, opoption, *weight_units)
        outputmenu.grid(row = 5, column = 1)
        outputmenu.config(font = "Arial 10", bg='#fcc3b6')

    elif unit == "TEMPERATURE":
        inputmenu = OptionMenu(tk_window, ipoption, *temp_units)
        inputmenu.grid(row = 3, column = 1)
        inputmenu.config(font = "Arial 10", bg='#fcc3b6')

        outputmenu = OptionMenu(tk_window, opoption, *temp_units)
        outputmenu.grid(row = 5, column = 1)
        outputmenu.config(font = "Arial 10", bg='#fcc3b6')

    elif unit == "AREA":
        inputmenu = OptionMenu(tk_window, ipoption, *area_units)
        inputmenu.grid(row = 3, column = 1)
        inputmenu.config(font = "Arial 10", bg='#fcc3b6')

        outputmenu = OptionMenu(tk_window, opoption, *area_units)
        outputmenu.grid(row = 5, column = 1)
        outputmenu.config(font = "Arial 10", bg='#fcc3b6')

    elif unit == "VOLUME":
        inputmenu = OptionMenu(tk_window, ipoption, *volume_units)
        inputmenu.grid(row = 3, column = 1)
        inputmenu.config(font = "Arial 10", bg='#fcc3b6')

        outputmenu = OptionMenu(tk_window, opoption, *volume_units)
        outputmenu.grid(row = 5, column = 1)
        outputmenu.config(font = "Arial 10", bg='#fcc3b6')
    


def ok():
    inp = float(inputentry.get())
    inp_unit = ipoption.get()
    out_unit = opoption.get()

    if inp_unit == "Celsius" and out_unit == "Fahrenheit":
            outputentry.delete(0, END)
            outputentry.insert(0, (inp * 1.8) + 32)
    elif inp_unit == "Fahrenheit" and out_unit == "Celsius":
            outputentry.delete(0, END)
            outputentry.insert(0, (inp - 32) * (5/9))
    else:
            outputentry.delete(0, END)
            outputentry.insert(0, round(inp * units_value[inp_unit]/units_value[out_unit], 5))

ipoption = StringVar()
ipoption.set(UNITS[0])

opoption = StringVar()
opoption.set(UNITS[0])
unitoption = StringVar()
unitoption.set(UNITS[0])

unitlabel = Label(tk_window, text = "Select Measurement Type", bg ='#fcc3b6', font ='Arial')
unitlabel.grid(row = 0, column = 0, pady = 20)

unitmenu = OptionMenu(tk_window, unitoption, *UNITS)
unitmenu.grid(row = 0, column = 1)
unitmenu.config(font = "Arial 10", bg='#fcc3b6')



unitbtn = Button(tk_window, text = "OK", command = un, padx = 100, pady = 2,bg='#fcc3b6')
unitbtn.grid(row = 1, column = 0, columnspan = 2, pady = 50)



inputlabel = Label(tk_window, text = "Input",bg ='#fcc3b6',font ='italic')
inputlabel.grid(row = 2, column = 0, pady = 10)

inputentry = Entry(tk_window, justify = "center", font = "bold",bg='#c2fbfc')
inputentry.grid(row = 3, column = 0, padx = 35, ipady = 5)



outputlabel = Label(tk_window, text = "Output",bg ='#fcc3b6',font ='italic')
outputlabel.grid(row = 4, column = 0, pady = 10)

outputentry = Entry(tk_window, justify = "center", font = "bold",bg='#c2fbfc')
outputentry.grid(row = 5, column = 0, padx = 35, ipady = 5)



okbtn = Button(tk_window, text = "CONVERT", command = ok, padx = 80, pady = 2, bg='#fcc3b6')
okbtn.grid(row = 6, column = 0, columnspan = 2, pady = 50)

tk_window.mainloop()