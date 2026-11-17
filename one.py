FILE_NAME = "results.txt"
PASS_MARKS = 40          # minimum marks needed in EVERY subject
students = []            # list that holds all student dictionaries

# Calculation Function
def calculate_total(maths, physics, chemistry):
    return maths + physics + chemistry


# 3 subjects, each out of 100 -> maximum is 300
def calculate_percentage(total):
    return total / 300 * 100


# Pass only if EVERY subject is 40 or more
def get_result(maths, physics, chemistry):
    if maths >= PASS_MARKS and physics >= PASS_MARKS and chemistry >= PASS_MARKS:
        return "Pass"
    return "Fail"

# Validation Function
def roll_exists(roll):
    for s in students:
        if s["roll"] == roll:
            return True
    return False


def valid_marks(mark):
    return 0 <= mark <= 100

# File Handling

def save_records():
    with open(FILE_NAME, "w") as f:
        for s in students:
            line = f"{s['roll']},{s['name']},{s['maths']},{s['physics']},{s['chemistry']}\n"
            f.write(line)


def load_records():
    try:
        with open(FILE_NAME, "r") as f:
            for line in f:
                line = line.strip()
                if line == "":
                    continue
                roll, name, m, p, c = line.split(",")
                students.append(make_student(int(roll), name, int(m), int(p), int(c)))
    except FileNotFoundError:
        pass   # first run: file doesn't exist yet, that's fine

# Core Function
def make_student(roll, name, maths, physics, chemistry):
    total = calculate_total(maths, physics, chemistry)
    return {
        "roll": roll,
        "name": name,
        "maths": maths,
        "physics": physics,
        "chemistry": chemistry,
        "total": total,
        "percentage": calculate_percentage(total),
        "result": get_result(maths, physics, chemistry),
    }


def add_student():
    try:
        roll = int(input("Enter roll number: "))
    except ValueError:
        print("Roll number must be a number.")
        return

    if roll_exists(roll):
        print(f"Roll number {roll} already exists.")
        return

    name = input("Enter name: ").strip()
    if name == "":
        print("Name cannot be empty.")
        return

    try:
        maths = int(input("Enter Maths marks: "))
        physics = int(input("Enter Physics marks: "))
        chemistry = int(input("Enter Chemistry marks: "))
    except ValueError:
        print("Marks must be numbers.")
        return

    if not (valid_marks(maths) and valid_marks(physics) and valid_marks(chemistry)):
        print("Marks must be between 0 and 100.")
        return

    student = make_student(roll, name, maths, physics, chemistry)
    students.append(student)
    save_records()

    print(f"Record added: {roll} | {name}")
    print(f"Total: {student['total']} | Percentage: {student['percentage']:.2f}% "
          f"| Result: {student['result']}")

def view_all():
    if len(students) == 0:
        print("No records found.")
        return
    for s in students:
        print(f"Roll: {s['roll']} | Name: {s['name']} | Maths: {s['maths']} | "
              f"Physics: {s['physics']} | Chemistry: {s['chemistry']} | "
              f"Total: {s['total']} | {s['percentage']:.2f}% | {s['result']}")

def rank_list():
    if len(students) == 0:
        print("No records found.")
        return
    ranked = sorted(students, key=lambda s: s["total"], reverse=True)
    rank = 1
    for s in ranked:
        print(f"Rank {rank} | {s['roll']} | {s['name']} | {s['total']} | "
              f"{s['percentage']:.2f}% | {s['result']}")
        rank += 1

# Main Menu
def main():
    load_records()
    while True:
        print("\n--- Exam Result Management System ---")
        print("1. Add")
        print("2. View all")
        print("3. Rank list")
        print("4. Exit")
        choice = input("Enter choice: ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            view_all()
        elif choice == "3":
            rank_list()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3 or 4.")


main()