"""
Case Study 42: Student Marks Matrix Analysis
Syllabus Used: Variables, data types, operators, conditionals, loops,
strings, lists, nested lists, tuples, tuple operations, and unpacking.
"""

print("=" * 74)
print("CASE STUDY 42: STUDENT MARKS MATRIX ANALYSIS")
print("=" * 74)

PASS_MARK = 40
LOW_AVG_THRESHOLD = 65.0

# Test cases: (case_title, subjects_tuple, students_list, marks_matrix)
test_cases = [
    (
        "Test Case 1: Standard Class Marks Matrix (6 Students x 5 Subjects)",
        ("Math", "Physics", "Chem", "CS", "English"),
        ["S01-Ananya", "S02-Bharath", "S03-Charan", "S04-Divya", "S05-Eshan", "S06-Farah"],
        [
            [95, 88, 76, 98, 90],
            [62, 54, 48, 70, 68],
            [88, 92, 60, 96, 85],
            [95, 88, 76, 98, 90],   # Tied top performer with Ananya
            [45, 38, 42, 55, 60],
            [78, 65, 58, 84, 79],
        ],
    ),
    (
        "Test Case 2: Multiple Low-Average Subjects & Borderline Scores",
        ("DSA", "DBMS", "OS", "CN"),
        ["S11-Gaurav", "S12-Hema", "S13-Irfan"],
        [
            [72, 55, 49, 80],
            [68, 52, 61, 74],
            [70, 58, 55, 69],
        ],
    ),
]

for case_title, subjects, students, matrix in test_cases:
    print("\n" + "-" * 74)
    print(case_title)
    print("-" * 74)

    num_students = len(students)
    num_subjects = len(subjects)

    # Row-wise student analysis
    student_summaries = []
    highest_total = -1

    print("\n  ROW-WISE STUDENT STATISTICS:")
    print(f"  {'Student':<14} {'Total':>6} {'Avg(%)':>8} {'Min':>5} {'Max':>5} {'Status':<8}")
    print("  " + "-" * 52)

    for r in range(num_students):
        row = matrix[r]
        row_total = 0
        row_min = row[0]
        row_max = row[0]
        all_passed = True

        for c in range(num_subjects):
            val = row[c]
            row_total += val
            if val < row_min:
                row_min = val
            if val > row_max:
                row_max = val
            if val < PASS_MARK:
                all_passed = False

        row_avg = row_total / num_subjects
        status = "PASS" if all_passed else "FAIL"
        if row_total > highest_total:
            highest_total = row_total

        student_summaries.append((students[r], row_total, row_avg, row_min, row_max, status))
        print(
            f"  {students[r]:<14} {row_total:>6} {row_avg:>8.2f} {row_min:>5} {row_max:>5} {status:<8}"
        )

    # Identify top performers (including ties)
    top_performers = []
    for name, total, avg, _, _, _ in student_summaries:
        if total == highest_total:
            top_performers.append((name, total, avg))

    print("\n  TOP PERFORMER(S):")
    for name, total, avg in top_performers:
        print(f"    * {name} -> Total: {total}/{num_subjects * 100} (Avg: {avg:.2f}%)")

    # Column-wise subject analysis
    low_avg_subjects = []
    print("\n  COLUMN-WISE SUBJECT STATISTICS:")
    print(f"  {'Subject':<10} {'Avg(%)':>8} {'High':>6} {'Low':>6} {'Pass%':>8}  Performance")
    print("  " + "-" * 56)

    for c in range(num_subjects):
        col_total = 0
        col_high = matrix[0][c]
        col_low = matrix[0][c]
        pass_count = 0

        for r in range(num_students):
            val = matrix[r][c]
            col_total += val
            if val > col_high:
                col_high = val
            if val < col_low:
                col_low = val
            if val >= PASS_MARK:
                pass_count += 1

        col_avg = col_total / num_students
        pass_pct = (pass_count / num_students) * 100.0
        perf_flag = "LOW AVG" if col_avg < LOW_AVG_THRESHOLD else "OK"
        if col_avg < LOW_AVG_THRESHOLD:
            low_avg_subjects.append((subjects[c], col_avg))

        print(
            f"  {subjects[c]:<10} {col_avg:>8.2f} {col_high:>6} {col_low:>6} {pass_pct:>7.1f}%  {perf_flag}"
        )

    print(f"\n  SUBJECTS BELOW {LOW_AVG_THRESHOLD:.1f}% AVERAGE:")
    if len(low_avg_subjects) == 0:
        print("    None — all subjects meet the target average.")
    else:
        for subj_name, subj_avg in low_avg_subjects:
            print(f"    ! {subj_name}: {subj_avg:.2f}%")

print("\n" + "=" * 74)
print("END OF CASE STUDY 42")
print("=" * 74)
