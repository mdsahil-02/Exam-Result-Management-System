# Summary: Exam Result Management System (PS No. 43)

**University:** Rungta International Skills University
**Program:** B.Tech Computer Science and Engineering
**Language:** Python 3

## 1. Project Overview

The Exam Result Management System is a console program that manages student exam records. For each student it stores a roll number, a name and marks in three subjects (Maths, Physics and Chemistry, each out of 100). The program then works out the total, the percentage and the Pass/Fail result.

**What the program can do**

- **Add** a student record, with checks on the roll number and the marks.
- **View all** saved records.
- **Rank list**: show students sorted by total marks, highest first.
- **Exit** the program.

**How it works**

- Each student is stored as a **dictionary**, and all students are kept in a **list**.
- Calculations are done by separate **functions**: `calculate_total`, `calculate_percentage` and `get_result`.
- A student **passes only if every subject has 40 or more marks**.
- Records are saved to `results.txt` after every addition and loaded again when the program starts, so data is not lost.
- The rank list uses `sorted()` with `reverse=True` on the total marks.

**Concepts used:** lists and dictionaries, functions, sorting, file handling, input validation, exception handling.

**Files in this project**

| File | Purpose |
|------|---------|
| `exam_result_system.py` | The main program |
| `results.txt` | Saved records (created automatically) |
| `README.md` | How to run the project |
| `Summary.md` | This report |
| `Screenshots/` | Images of the 4 test cases |

## 2. Difficulties Faced and How They Were Solved

| # | Difficulty | How it was solved |
|---|-----------|-------------------|
| 1 | **Pass rule was easy to get wrong.** A student with a high total can still fail if one subject is below 40. | The result function checks each subject separately with `and`, instead of using the total or percentage. |
| 2 | **Percentage calculation.** It was not clear whether to divide by 100 or 300. | There are 3 subjects of 100 marks each, so the maximum is 300. The formula is `total / 300 * 100`. This gives 80.00% for 240 and 40.00% for 120, matching the test cases. |
| 3 | **Program crashed on wrong input**, for example when letters were typed instead of numbers. | `int(input(...))` was wrapped in `try/except ValueError`, so the program prints a clear message and returns to the menu. |
| 4 | **Crash on the first run** because `results.txt` does not exist yet. | `load_records()` uses `try/except FileNotFoundError`, so a missing file is treated as "no records yet". |
| 5 | **Duplicate roll numbers.** | A `roll_exists()` function loops through the list. It is checked first, before asking for the name and marks, so no time is wasted on a record that will be rejected. |
| 6 | **Marks outside 0 to 100**, such as 105. | A `valid_marks()` function checks each mark and the program prints `Marks must be between 0 and 100.` |
| 7 | **A name with a comma would break the file.** Records are saved as comma-separated lines, so a name like `Singh, Raj` would be split into the wrong number of values when loading. This was found while reviewing the code. | The program now rejects names that contain a comma and shows a message. |
| 8 | **Repeating the same calculation code** in two places (when adding and when loading from the file). | A single `make_student()` function builds the dictionary, and both places call it. This keeps the logic in one place. |
| 9 | **Testing was slow** because every test needed many typed inputs. | The test cases were run with scripted inputs, and the output was compared with the expected output in the assignment. |

## 3. Test Cases and Screenshots

All 4 test cases give the expected output.

### Test Case 1: Normal Input
Add roll 101, Aman, marks 80, 70, 90.
**Expected:** `Record added: 101 | Aman` and `Total: 240 | Percentage: 80.00% | Result: Pass`

![Test Case 1]

### Test Case 2: Boundary / Minimum Input
Add roll 102, Riya, marks 40, 40, 40 (the pass limit).
**Expected:** `Record added: 102 | Riya` and `Total: 120 | Percentage: 40.00% | Result: Pass`

![Test Case 2]

### Test Case 3: Invalid Input
(a) Add roll 101 when it already exists. **Expected:** `Roll number 101 already exists.`
(b) Add roll 103, Ravi, marks 105, 60, 60. **Expected:** `Marks must be between 0 and 100.`

![Test Case 3]

### Test Case 4: Different Valid Scenario (Rank List)
Records: 101 Aman (80, 70, 90), 102 Riya (40, 40, 40), 103 Karan (60, 60, 60). Then menu option 3.
**Expected:** Rank 1 is 101 Aman 240, Rank 2 is 103 Karan 180, Rank 3 is 102 Riya 120.

![Test Case 4]

## 4. Conclusion

The project meets all the bare minimum requirements: it is one Python 3 file, stores each record as a dictionary inside a list, uses functions for the calculations, sorts the rank list in descending order, validates the roll number and marks, and loads and saves records using a file. It also passes all 4 assigned test cases.
