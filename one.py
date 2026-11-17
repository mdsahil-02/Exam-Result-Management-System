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