def wake_up(time, name):
    print(f"{name} wake up at {time}")


def breakfast(name, food, time):
    print(f"{name} eats {food} at {time}")


def shopping(name, market_name, time):
    print(f"{name} goes to {market_name} at {time}")

def daily_routine(name, food, market_name):
    wake_up("7:00", name)
    breakfast(name, food, "7.30")
    shopping(name, market_name, "11.00")

# def daily_routine_for_burak():
#     name = "burak"
#     food = "tr break"
#     market_name = "edeka"
#     wake_up("7:00", name)
#     breakfast(name, food, "7.30")
#     shopping(name, market_name, "11.00")

daily_routine("burak", "pazartesi", "edeka")
daily_routine("burak", "sali", "edeka")
