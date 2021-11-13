from tkinter import *

window = Tk()
window.title("Unit Converter")
window.minsize(width=400, height=200)
window.config(padx=20, pady=20)

units = ["Mile", "Pound", "Feet", "Meter", "Gallon", "Kilometer", "Celsius" "Kilogram", "gram"]


def mile_kilo():
    result = float(data.get()) * 1.60934
    result_label.config(text=f"{result}")


def mile_feet():
    result = float(data.get()) * 1
    result_label.config(text=f"{result}")


def calculate():
    if input_variable.get() == "Mile" and output_variable.get() == "Kilometer":
        mile_kilo()
    elif input_variable.get() == "Mile" and output_variable.get() == "Feet":
        mile_feet()


convert_label = Label(text="Convert", font=("Arial", 15, "bold"))
convert_label.grid(row=0, column=0)
convert_label.config(padx=20, pady=20)

# User's input to convert
data = Entry(width=20)
data.grid(row=0, column=1)

# Label for unit to convert
input_variable = StringVar(window)
input_variable.set("Mile")  # Default Value
input_options = OptionMenu(window, input_variable, *units)
input_options.grid(row=0, column=2)
# unit_label = Label(text="Miles", font=("Arial", 15, "bold"))
# unit_label.grid(row=0, column=2)
# unit_label.config(padx=20, pady=20)

equal_label = Label(text="is equal to", font=("Arial", 15, "bold"))
equal_label.grid(row=1, column=0)

result_label = Label(text="0", font=("Arial", 15, "bold"))
result_label.grid(row=1, column=1)

output_variable = StringVar(window)
output_variable.set("Kilometer")  # Default Value
output_options = OptionMenu(window, output_variable, *units)
output_options.grid(row=1, column=2)
# km_label = Label(text="Km", font=("Arial", 15, "bold"))
# km_label.grid(row=1, column=2)

# Button
calculate_btn = Button(text="Calculate", command=calculate)
calculate_btn.grid(row=2, column=1)
calculate_btn.config(padx=10, pady=10)

window.mainloop()
