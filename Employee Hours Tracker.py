import os

FILENAME = "work_hours.txt"

def load_records():
    records = {}
    if os.path.exists(FILENAME):
        try:
            with open(FILENAME, 'r') as file:
                for line in file:
                    name, hours = line.strip().split(', ')
                    records[name] = float(hours)
        except Exception as e:
            print(f"Error loading records: {e}")
    return records

def save_records(records):
    try:
        with open(FILENAME, 'w') as file:
            for name, hours in records.items():
                file.write(f"{name}, {hours}\n")
    except Exception as e:
        print(f"Error saving records: {e}")

def add_hours(records):
    name = input("Enter employee name: ").strip()
    while not name:
        name = input("Name cannot be empty. Try again: ").strip()

    try:
        hours = float(input(f"Enter hours worked by {name}: ").strip())
        while hours < 0 or hours > 168:
            hours = float(input("Enter a realistic number of hours (0-168): ").strip())
    except ValueError:
        print("Invalid input. Hours must be a numeric value.")
        return

    if name in records:
        records[name] += hours
    else:
        records[name] = hours

    save_records(records)
    print(f"{name}'s hours updated.")

def view_records(records):
    if not records:
        print("No employee records found.")
        return

    print("\nEmployee Work Hours:")
    total = 0
    for name, hours in records.items():
        print(f"{name}: {hours:.2f} hours")
        total += hours
    print(f"\nTotal hours worked by all employees: {total:.2f} hours")

def remove_record(records):
    name = input("Enter employee name to remove: ").strip()
    if name in records:
        del records[name]
        save_records(records)
        print(f"Removed {name}'s record.")
    else:
        print("Employee not found.")

def main():
    records = load_records()

    options = {
        '1': ("Add/Update work hours", add_hours),
        '2': ("View all records", view_records),
        '3': ("Remove an employee record", remove_record),
        '4': ("Exit", None)
    }

    while True:
        print("\nEmployee Work Hours Tracker")
        for key, (desc, _) in options.items():
            print(f"{key}. {desc}")
        choice = input("Select an option: ").strip()

        if choice == '4':
            print("Exiting.")
            break
        elif choice in options:
            _, action = options[choice]
            action(records)
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
