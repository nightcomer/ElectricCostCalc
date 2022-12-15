W = input("Consumption (Watts): ")
H = input("Use Per Day (Hours): ")
cost = input("Cost per kWh (Dollars): ")

kwh = (float(W) * float(H)) / 1000
daily = (float(kwh) * float(cost))
weekly = daily * 7
yearly = daily * 365

print("Consumption per day: " + str(kwh) + "kWh")
print("Electricity Cost Per Day: " + "${:,.2f}".format(daily))
print("Electricity Cost Per Week: " + "${:,.2f}".format(weekly))
print("Electricity Cost Per Year: " + "${:,.2f}".format(yearly))
