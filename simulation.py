import json


money = 150
population = 10
power = 50
factories = 1
power_plants = 0
print("Starting simulation")
print("--------------------")

def show_stats(tick, money, population, power, factories, power_plants):
    print("\n==============================")
    print(f"📊 TICK {tick} STATUS")
    print("==============================")
    print(f"Money:        £{money}")
    print(f"Population:   {population}")
    print(f"Power:        {power}")
    print(f"Factories:   {factories}")
    print(f"Power plants:{power_plants}")
    print("==============================")

def show_help():
    print("\n========== HELP ==========")
    print("Goal:")
    print("- Grow your economy without running out of power")
    print()
    print("Resources:")
    print("- Money: Used to build things")
    print("- Population: Grows every tick, consumes power")
    print("- Power: Needed to support factories and people")
    print()
    print("Buildings:")
    print("- Factory (£100):")
    print("  + Produces £20 per tick")
    print("  - Uses 5 power per tick")
    print()
    print("- Power Plant (£80):")
    print("  + Produces 30 power per tick")
    print()
    print("Warnings:")
    print("- If power reaches 0, population will drop")
    print("==========================")

def save_game(money, population, power, factories, power_plants):
    data = {
        "money": money,
        "population": population,
        "power": power,
        "factories": factories,
        "power_plants": power_plants
    }

    with open("save.json", "w") as file:
        json.dump(data, file)

    print("💾 Game saved.")

def load_game():
    try:
        with open("save.json", "r") as file:
            data = json.load(file)

        print("📂 Game loaded.")
        return (
            data["money"],
            data["population"],
            data["power"],
            data["factories"],
            data["power_plants"]
        )
    except FileNotFoundError:
        print("No save file found.")
        return None





for tick in range(1, 11):
    show_stats(tick, money, population, power, factories, power_plants)
    print("\nChoose an action:")
    print("1. Do nothing")
    print("2. Build factory (£100)")
    print("3. Build power plant (£80)")
    print("4. Help / Rules")
    print("5. Save game")
    print("6. Load game")

    choice = input("Your choice: ")

    if choice == "2":
        if money >= 100:
            money -= 100
            factories += 1
            print("🏭 Built a factory.")
        else:
            print("Not enough money.")
    elif choice == "3":
        if money >= 80:
            money -= 80
            power += 30
            power_plants += 1
            print("⚡ Built a power plant.")
    elif choice == "4":
        show_help()
    elif choice == "5":
        save_game(money, population, power, factories, power_plants)

    elif choice == "6":
        loaded = load_game()
        if loaded:
            money, population, power, factories, power_plants = loaded

    print(f"\nTick {tick}")

    # Production
    money += factories * 20
    power -= factories * 5

    # Population growth
    population += 1

    # Power usage by population
    power -= population * 1

    # Check for power shortage
    if power < 10:
        print("⚠ WARNING: Power critically low!")

    elif power < 0:
        print("⚠ Power shortage! Population unhappy.")
        population -= 2
        power = 0


