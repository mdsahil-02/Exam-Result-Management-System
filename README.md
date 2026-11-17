# Exam Result Management System

A console-based Python 3 program that stores student records with marks in three subjects, calculates total, percentage and result, and displays a rank list sorted by total marks. Records are saved in a file so they are still available the next time the program runs.

## Features

- Add a student record (roll number, name, marks in Maths, Physics and Chemistry)
- Automatically calculate total, percentage and Pass/Fail result
- View all saved records
- Show a rank list sorted by total marks (highest first)
- Validate the roll number (must be unique) and the marks (must be 0 to 100)
- Save records to `results.txt` and load them automatically on startup

## Concepts Used

Python 3, lists and dictionaries, functions, sorting (`sorted` with `lambda`), file handling, input validation, exception handling (`try/except`).

## Rules

- Marks are out of 100 in each of Maths, Physics and Chemistry (maximum total is 300).
- A student **passes only if every subject has 40 or more marks**. Otherwise the result is Fail.
- Roll numbers must be unique.
- Percentage = total / 300 x 100.

## How to Run

1. Install Python 3.
2. Put `exam_result_system.py` in a folder.
3. Open a terminal in that folder and run:

```bash
python exam_result_system.py
```

On some systems use `python3` instead of `python`.

## Menu

```
--- Exam Result Management System ---
1. Add
2. View all
3. Rank list
4. Exit
```

| Option | What it does |
|--------|--------------|
| 1 | Add a new student record |
| 2 | Show all stored records |
| 3 | Show the rank list sorted by total marks |
| 4 | Exit the program |

## Data File

Records are stored in `results.txt`, one student per line:

```
roll,name,maths,physics,chemistry
101,Aman,80,70,90
```

The file is created automatically when the first record is added.

## Test Cases

| # | Scenario | Input | Expected Output |
|---|----------|-------|-----------------|
| 1 | Normal input | Option 1: `101, Aman, 80, 70, 90` | `Record added: 101 \| Aman` and `Total: 240 \| Percentage: 80.00% \| Result: Pass` |
| 2 | Boundary / minimum | Option 1: `102, Riya, 40, 40, 40` | `Record added: 102 \| Riya` and `Total: 120 \| Percentage: 40.00% \| Result: Pass` |
| 3a | Invalid: duplicate roll | Add `101, Neha, 70, 70, 70` | `Roll number 101 already exists.` |
| 3b | Invalid: marks out of range | Add `103, Ravi, 105, 60, 60` | `Marks must be between 0 and 100.` |
| 4 | Rank list | Records: 101 Aman (80,70,90), 102 Riya (40,40,40), 103 Karan (60,60,60); Option 3 | Rank 1: 101 Aman 240 80.00% Pass; Rank 2: 103 Karan 180 60.00% Pass; Rank 3: 102 Riya 120 40.00% Pass |

All four test cases pass.

## Sample Output

```
Enter choice: 3
Rank 1 | 101 | Aman | 240 | 80.00% | Pass
Rank 2 | 103 | Karan | 180 | 60.00% | Pass
Rank 3 | 102 | Riya | 120 | 40.00% | Pass
```

## Project Structure

```
.
├── exam_result_system.py   # main program
├── results.txt             # saved records (created automatically)
└── README.md               # project documentation
```

## How the Code Is Organised

| Part | Purpose |
|------|---------|
| `calculate_total`, `calculate_percentage`, `get_result` | Calculation functions |
| `roll_exists`, `valid_marks` | Validation functions |
| `save_records`, `load_records` | File handling |
| `make_student` | Builds one student dictionary |
| `add_student`, `view_all`, `rank_list` | Menu features |
| `main` | Menu loop |

## Author
Name: Md Sahil, roll number: RU-26-01729 and section: M
