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