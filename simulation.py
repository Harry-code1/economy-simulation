import json

class Game:
    def __init__(self):
        self.money = 150
        self.population = 10
        self.power = 50
        self.factories = 1
        self.power_plants = 0

    def show_stats(self, tick):
        print("\n==============================")
        print(f"📊 TICK {tick} STATUS")
        print("==============================")
        print(f"Money:        £{self.money}")
        print(f"Population:   {self.population}")
        print(f"Power:        {self.power}")
        print(f"Factories:   {self.factories}")
        print(f"Power plants:{self.power_plants}")
        print("==============================")

    def run_tick(self):
        self.money += self.factories * 20
        self.power += self.power_plants * 30
        self.power -= self.factories * 5

        self.population += 1
        self.power -= self.population

        if self.power < 0:
            print("⚠ Power shortage! Population unhappy.")
            self.population -= 2
            self.power = 0

    def save(self):
        with open("save.json", "w") as file:
            json.dump(self.__dict__, file)
        print("💾 Game saved.")

    def load(self):
        try:
            with open("save.json", "r") as file:
                data = json.load(file)
            self.__dict__.update(data)
            print("📂 Game loaded.")
        except FileNotFoundError:
            print("No save file found.")

    def handle_choice(self, choice):
        if choice == "2" and self.money >= 100:
            self.money -= 100
            self.factories += 1
            print("🏭 Built a factory.")

        elif choice == "3" and self.money >= 80:
            self.money -= 80
            self.power += 30
            self.power_plants += 1
            print("⚡ Built a power plant.")

        elif choice == "4":
            show_help()

        elif choice == "5":
            self.save()

        elif choice == "6":
            self.load()







power_plants = 0
print("Starting simulation")
print("--------------------")



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



game = Game()

for tick in range(1, 21):
    game.show_stats(tick)

    print("\nChoose an action:")
    print("1. Do nothing")
    print("2. Build factory (£100)")
    print("3. Build power plant (£80)")
    print("4. Help / Rules")
    print("5. Save game")
    print("6. Load game")

    choice = input("Your choice: ")
    game.handle_choice(choice)

    game.run_tick()



