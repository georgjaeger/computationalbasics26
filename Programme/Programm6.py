import csv
import matplotlib.pyplot as plt
import numpy as np


def read_labor_market_file(filename):
    all_incomes = []

    with open(filename, mode="r") as file:
        reader = csv.reader(file)
        # Outer loop: Go through the CSV line by line (year by year)
        for row in reader:  
            # Create an empty list to store numbers for just THIS year
            year_incomes = []
            # Inner loop: Go through every individual text entry in the current row
            for entry in row:
                # Convert text to a decimal number
                income = float(entry)
                # Add the number to this year's list
                year_incomes.append(income)

            # Add this person's completed list to the main master list
            all_incomes.append(year_incomes)
    return all_incomes




def unemployment_benefits(all_incomes):
    incomes=all_incomes[9]
    number_unemployed = 0
    total_tax_base = sum(incomes)

    for income in incomes:
        if income == 0:
            number_unemployed += 1

    total_needed = number_unemployed * 1200

    tax_rate = total_needed / total_tax_base
 
    new_incomes = []

    for income in incomes:
   
        if income != 0:
            income = income - tax_rate * income
        else:
            income = 1200

        new_incomes.append(income)

    return new_incomes


def ubi(all_incomes):
    incomes=all_incomes[9]

    number_persons = len(incomes)
    total_ubi_needed = number_persons * 1200

    total_tax_base = sum(incomes)

   
    tax_rate = total_ubi_needed / total_tax_base
  

    new_incomes = []

    for income in incomes:
  
        tax_paid = tax_rate * income
        new_income = income - tax_paid + 1200
        new_incomes.append(new_income)

    return new_incomes


all_incomes = read_labor_market_file("labormarket.csv")
all_avgs=[]
for year in all_incomes:
    all_avgs.append(np.mean(year))

plt.plot(all_avgs)
plt.title("Avg income")
plt.show()


# Baseline: all employed:
incomes_base = all_incomes[0]
incomes_base = sorted(incomes_base)
plt.figure()
plt.bar(list(range(len(incomes_base))),incomes_base)
plt.title("full employment")

# last year:
incomes_base = all_incomes[9]
incomes_base = sorted(incomes_base)
plt.figure()
plt.bar(list(range(len(incomes_base))),incomes_base)
plt.title("low employment")
plt.show()



# Variant 1: unemployment benefits up to poverty line
incomes_ueb = unemployment_benefits(all_incomes)
incomes_ueb=sorted(incomes_ueb)
plt.figure()
plt.bar(list(range(len(incomes_ueb))),incomes_ueb)
plt.title("unemployment benefit")


# Variant 2: everyone gets UBI
incomes_ubi= ubi(all_incomes)

incomes_ubi = sorted(incomes_ubi)
plt.figure()
plt.bar(list(range(len(incomes_ubi))),incomes_ubi)
plt.title("UBI")
plt.show()


print("Simulation finished.")


