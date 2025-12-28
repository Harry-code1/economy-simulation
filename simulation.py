import json


state = {
    "money": 150,
    "population": 10,
    "power": 50,
    "factories": 1,
    "power_plants": 0
}

power_plants = 0
print("Starting simulation")
print("--------------------")

def show_stats(tick, state):
    print("\n==============================")
    print(f"📊 TICK {tick} STATUS")
    print("==============================")
    print(f"Money:        £{state['money']}")
    print(f"Population:   {state['population']}")
    print(f"Power:        {state['power']}")
    print(f"Factories:   {state['factories']}")
    print(f"Power plants:{state['power_plants']}")
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

def save_game(state):
    with open("save.json", "w") as file:
        json.dump(state, file)
    print("💾 Game saved.")


def load_game():
    try:
        with open("save.json", "r") as file:
            state = json.load(file)
        print("📂 Game loaded.")
        return state
    except FileNotFoundError:
        print("No save file found.")
        return None

def run_tick(state):
    state["money"] += state["factories"] * 20
    state["power"] += state["power_plants"] * 30
    state["power"] -= state["factories"] * 5

    state["population"] += 1
    state["power"] -= state["population"]

    if state["power"] < 0:
        print("⚠ Power shortage! Population unhappy.")
        state["population"] -= 2
        state["power"] = 0

def handle_choice(choice, state):
    if choice == "2" and state["money"] >= 100:
        state["money"] -= 100
        state["factories"] += 1
        print("🏭 Built a factory.")

    elif choice == "3" and state["money"] >= 80:
        state["money"] -= 80
        state["power"] += 30
        state["power_plants"] += 1
        print("⚡ Built a power plant.")

    elif choice == "4":
        show_help()

    elif choice == "5":
        save_game(state)

    elif choice == "6":
        loaded = load_game()
        if loaded:
            state.clear()
            state.update(loaded)




for tick in range(1, 21):
    show_stats(tick, state)

    print("\nChoose an action:")
    print("1. Do nothing")
    print("2. Build factory (£100)")
    print("3. Build power plant (£80)")
    print("4. Help / Rules")
    print("5. Save game")
    print("6. Load game")

    choice = input("Your choice: ")
    handle_choice(choice, state)

    run_tick(state)


