import tkinter as tk

window = tk.Tk()
window.title("Electricity Cost Calc")

# input consumption (watts)
W = 0
tk.Label(window, text="Consumption (Watts):").grid(row=1, column=1, sticky="W")
watt_field = tk.Text(window, height=1, width=15)
watt_field.grid(row=1, column=2, sticky="W")

# input use (hours
H = 0
tk.Label(window, text="Use Per Day (Hours):").grid(row=2, column=1, sticky="W")
hours_field = tk.Text(window, height=1, width=15)
hours_field.grid(row=2, column=2, sticky="W")

# input kwh cost (dollars)
cost = 0
tk.Label(window, text="Cost per kWh (Dollars):").grid(row=3, column=1, sticky="W")
dollars_field = tk.Text(window, height=1, width=15)
dollars_field.grid(row=3, column=2, sticky="W")


kwh = 0
daily = 0
weekly = 0
yearly = 0


def calculate():
    try:
        w = watt_field.get(1.0, "end-1c")
        h = hours_field.get(1.0, "end-1c")
        cost = dollars_field.get(1.0, "end-1c")

        kwh = (float(w) * float(h)) / 1000
        daily = (float(kwh) * float(cost))
        weekly = daily * 7
        yearly = daily * 365

        tk.Label(window, text=str(kwh) + "kWh").grid(row=4, column=2, sticky="W")
        tk.Label(window, text="${:,.2f}".format(daily)).grid(row=5, column=2, sticky="W")
        tk.Label(window, text="${:,.2f}".format(weekly)).grid(row=6, column=2, sticky="W")
        tk.Label(window, text="${:,.2f}".format(yearly)).grid(row=7, column=2, sticky="W")
    except ValueError or NameError:
        tk.Label(window, text="At least one input is invalid.").grid(row=9, column=1, sticky="W")


# display daily consumption in kwh
tk.Label(window, text="Consumption per day:").grid(row=4, column=1, sticky="W")
tk.Label(window, text=str(kwh) + "kWh").grid(row=4, column=2, sticky="W")

# display daily cost
tk.Label(window, text="Electricity Cost Per Day:").grid(row=5, column=1, sticky="W")
tk.Label(window, text="${:,.2f}".format(daily)).grid(row=5, column=2, sticky="W")

# display weekly cost
tk.Label(window, text="Electricity Cost Per Week:").grid(row=6, column=1, sticky="W")
tk.Label(window, text="${:,.2f}".format(weekly)).grid(row=6, column=2, sticky="W")

# display yearly cost
tk.Label(window, text="Electricity Cost Per Year:").grid(row=7, column=1, sticky="W")
tk.Label(window, text="${:,.2f}".format(yearly)).grid(row=7, column=2, sticky="W")

# Calculate button to execute calculator
button = tk.Button(window, text="Calculate", width=10, command=lambda: calculate())
button.grid(row=8, column=2)

# exit button
exit_button = tk.Button(window, text="Exit", width=10, command=lambda: exit())
exit_button.grid(row=8, column=1)

window.mainloop()
