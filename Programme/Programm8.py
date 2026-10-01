import random
import matplotlib.pyplot as plt

random.seed(100)

def create_profile(
    work_start=9 * 60,
    work_end=17 * 60,
    commute=30,
):
    """
    One daily car-use profile (1440 minutes, 1=using car, 0=not using).
    """
    day_min = 24 * 60
    prof = [0] * day_min

    commute = commute + int(random.uniform(-20,40))

    # commute to work
    commute_to_start = work_start - commute
    commute_to_end = work_start
    for m in range(commute_to_start, commute_to_end):
        prof[m] = 1

    # commute back home
    commute_back_start = work_end
    commute_back_end =  work_end + commute
    for m in range(commute_back_start, commute_back_end):
        prof[m] = 1


    return prof


def create_pop_base():
    """
    100 default (9-17), 50 morning (8-12), 50 random.
    """
    pop = []

    # 100 default: 9-17
    for it in range(100):
        prof = create_profile()
        pop.append(prof)

    # 50 morning: 8-12
    for it in range(50):
        prof = create_profile(work_start=8 * 60,work_end=12 * 60)
        
        pop.append(prof)

    # 50 random patterns
    for it in range(50):
        prof = create_profile(
            work_start=int(random.uniform(7*60,11*60)),
            work_end=int(random.uniform(12*60,20*60)),
            commute=int(random.uniform(5,30)),
        )
        pop.append(prof)

    return pop


def efficiency(pop):
    """
    Average usage/idle minutes
    """
   
    total_use = 0

    for prof in pop:
        use = sum(prof)
        total_use += use
       
    return total_use / (60 * 24 * 200)


def car_use(pop):
    """
    How many cars are needed each minute
    """
    day_min = 24 * 60
    cars_per_min = [0] * day_min

    for minute in range(day_min):
        for person in pop:
            cars_per_min[minute] += person[minute]

    maxi = max(cars_per_min)

    return cars_per_min, maxi


def create_pop_flex():
   
    pop = []

    # 200 flexible: 
    for it in range(200):
        prof = create_profile(
            work_start=int(random.uniform(7*60,11*60)),
            work_end=int(random.uniform(12*60,20*60))
        )
        pop.append(prof)

    return pop

def make_plot(data,c="crimson"):
    plt.figure()
    plt.plot(data,c=c)
    plt.ylabel("cars needed")
    plt.xlabel("time (min after midnight)")


def make_pop(version="base"):
    if version == "base":
        pop= create_pop_base()
    elif version == "flex":
        pop= create_pop_flex()
    else:
        print("no such pop",version)
        pop=[[]]
    return pop




# base population
base_pop = make_pop()
eff = efficiency(base_pop)
print(eff)

usage,maxi=car_use(base_pop)
make_plot(usage)
print(maxi)


flex_pop = make_pop(version="flex")

usage,maxi=car_use(flex_pop)
make_plot(usage,c="forestgreen")
print(maxi)

plt.show()
    

