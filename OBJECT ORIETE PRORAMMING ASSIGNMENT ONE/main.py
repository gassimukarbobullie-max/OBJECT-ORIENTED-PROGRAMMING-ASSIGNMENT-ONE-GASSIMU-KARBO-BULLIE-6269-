from models import Animal, Herd, SPECIES, HEALTH_STATUSES

def add_record(herd, tag_id, species, age_months):
    herd.add_animal(Animal(tag_id, species, age_months))
def display_records(herd):
    if len(herd) == 0:
        print("No animals registered yet.")
        return
    for animal in herd.all_animals():
        print("-" * 32)
        animal.display_info()
    print("-" * 32)
    print(f"Animals in this herd: {len(herd)}")

def choose(prompt, options):
    for number, option in enumerate(options, start=1):
        print(f"  {number}. {option}")
    while True:
        answer = input(prompt).strip()
        if answer.isdigit() and 1 <= int(answer) <= len(options):
            return options[int(answer) - 1]
        print(f"Please enter a number from 1 to {len(options)}.")

def ask_age():
    while True:
        answer = input("Age in months: ").strip()
        if answer.isdigit():
            return int(answer)
        print("Please enter a whole number, for example 18.")

MENU = """
1. Register an animal
2. View all animals
3. Update health record
4. Show animals due for a checkup
5. Quit
"""


def main():
    herd = Herd("FARM-001")
    # Sample data created from strings using the class method
    for text in ("COW-001, cattle, 36", "GOAT-07, goat, 14"):
        herd.add_animal(Animal.from_string(text))

    print("Welcome. No personal data is stored: animals are tracked by tag ID only.")
    while True:
        print(MENU)
        choice = input("Choose an option (1-5): ").strip()
        try:
            if choice == "1":
                tag = input("Tag ID (e.g. COW-002): ")
                print("Species:")
                species = choose("Choose species number: ", SPECIES)
                add_record(herd, tag, species, ask_age())
                print("Animal registered.")
            elif choice == "2":
                display_records(herd)
            elif choice == "3":
                animal = herd.get_animal(input("Tag ID: "))
                if animal is None:
                    print("No animal found with that tag.")
                    continue
                print("New health status:")
                status = choose("Choose status number: ", HEALTH_STATUSES)
                treatment = input("Treatment given (press Enter for none): ")
                animal.update_record(status, treatment)
                print("Record updated.")
            elif choice == "4":
                found = False
                for animal in herd.all_animals():
                    if animal.needs_checkup():
                        print(f"{animal.tag_id} - last checked {animal.days_since_checkup()} days ago")
                        found = True
                if not found:
                    print("All animals are up to date.")
            elif choice == "5":
                print(f"Goodbye. Total animals created this session: {Animal.get_total_animals()}")
                break
            else:
                print("Please choose a number from 1 to 5.")
        except ValueError as error:
            print(f"Problem: {error}")


if __name__ == "__main__":
    main()
