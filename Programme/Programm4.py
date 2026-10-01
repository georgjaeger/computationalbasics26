import numpy as np
import matplotlib.pyplot as plt


# ----------------------------------------
# 1. Daily electricity consumption (list)
# ----------------------------------------
# We store the daily electricity consumption (in kWh)
# for 4 weeks = 28 days in a simple Python list.

daily_consumption_kwh = [8.0, 7.5, 7.8, 8.2, 12.0, 5.5, 5.0,8.1, 7.6, 7.9, 8.3, 12.5, 5.3, 5.1,8.2, 7.4, 7.7, 8.4, 12.2, 5.4, 5.2,8.3, 7.7, 7.6, 8.1, 12.7, 5.2, 5.3]


# ----------------------------------------
# 2. Convert list to array and compute costs
# ----------------------------------------
# We convert the list to a NumPy array so that we can
# multiply all values with the electricity price at once.

price_per_kwh_eur = 0.30  # price in EUR per kWh

daily_consumption_array = np.array(daily_consumption_kwh)

# Element-wise multiplication: costs for each day
daily_costs_eur = daily_consumption_array * price_per_kwh_eur


# ----------------------------------------
# 3. Plot daily costs (using day index)
# ----------------------------------------
# For now we simply plot the costs against the day index
# (0 for the first day, 1 for the second day, ...).

plt.figure(figsize=(10, 4))
plt.plot(daily_costs_eur, color="navy", marker="o")
plt.title("Daily electricity costs")
plt.xlabel("Day index")
plt.ylabel("Costs (EUR)")
plt.grid(True)
plt.tight_layout()



# ----------------------------------------
# 4. Weekday lookup table (list)
# ----------------------------------------
# We create a list that maps numbers 0–6 to weekday names.
# We use the convention:
# 0 = Monday, 1 = Tuesday, ..., 4 = Friday, 5 = Saturday, 6 = Sunday.

weekday_lookup = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]



weekday_names = 4 * weekday_lookup



# ----------------------------------------
# 5. Plot daily costs with weekday labels
# ----------------------------------------
# We use the weekday names as tick labels on the x-axis.

plt.figure(figsize=(12, 4))
plt.plot(daily_costs_eur, color="darkgreen", marker="o")
plt.title("Daily electricity costs with weekday labels")
plt.xlabel("Day (weekday)")
plt.ylabel("Costs (EUR)")
plt.grid(True)

# We set one tick for each day index and use the weekday label list.
plt.xticks(
    ticks=list(range(28)),
    labels=weekday_names,
    rotation=45
)

plt.tight_layout()



# ----------------------------------------
# 6. Compute average costs for Fridays
#    and for other weekdays (without Fridays)
# ----------------------------------------
# We want two averages:
# - average costs on Fridays
# - average costs on all other days (without Fridays)
#
# We use a for-loop over all 28 days.
# For each day we compute the weekday index (0–6) with modulo.
# Then we use the weekday_lookup dictionary to get the weekday name.
# With an if/else we decide whether the cost goes into the Friday sum
# or into the sum for all non-Friday days.

friday_sum_eur = 0.0
other_days_sum_eur = 0.0


for it in range(28):
    weekday_name = weekday_names[it]

    # Costs for this day
    cost_for_this_day = daily_costs_eur[it]

    # Decide if this is a Friday or not
    if weekday_name == "Friday":
        friday_sum_eur += cost_for_this_day
    else:
        other_days_sum_eur += cost_for_this_day

# Compute averages

average_friday_cost_eur = friday_sum_eur / 4 #(4 Fridays in 4 weeks)
average_other_days_cost_eur = other_days_sum_eur / (28-4) #all other days are not fridays

print("Average costs on Fridays (EUR):", average_friday_cost_eur)
print("Average costs on non-Friday days (EUR):", average_other_days_cost_eur)

#compact avg calculation:
print(sum(daily_costs_eur[4::7]/4))


events = [
    "Waschmaschine",
    "Computer1",
    "Waschmaschine",
    "Computer2",
    "Trockner",
    "Laufband",
    "Computer2",
    "Waschmaschine",
    "Brotbackmaschine",
    "Computer1",
    "Trockner",
    "Laptop",
    "Computer2",
    "Trockner",
    "Waschmaschine",
    "Trockner",
]

device_to_person = {

    "Computer1":    "Alice",
    "Laufband":          "Alice",

    "Computer2":      "Bob",
    "Brotbackmaschine":  "Bob",

    "Waschmaschine":     "Carol",
    "Trockner":          "Carol",
    "Laptop":      "Carol",
}

usage_per_person_wh = {
    "Alice": 0,
    "Bob":0,
    "Carol":0,
}

for it in range(len(events)) :
    person = device_to_person[events[it]]  # direct lookup via key

    usage_per_person_wh[person] += 10  # 10 Wh per entry

print(usage_per_person_wh)


plt.show()