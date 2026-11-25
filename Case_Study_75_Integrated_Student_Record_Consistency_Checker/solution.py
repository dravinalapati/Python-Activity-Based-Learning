"""
Case Study 75: Integrated Student Record Consistency Checker
Syllabus Used: Variables, data types, operators, conditionals, loops,
strings, lists, nested lists, tuples, tuple operations, and unpacking.
"""

print("=" * 78)
print("CASE STUDY 75: INTEGRATED STUDENT RECORD CONSISTENCY CHECKER")
print("=" * 78)

VALID_COURSES = ("CSE", "ECE", "EEE", "MECH", "CIVIL")
EXPECTED_SUBJECTS = 4
PASS_MARK = 40
MIN_ATTENDANCE = 75.0
HONORS_AVG = 85.0

# Student records: (student_id, name, course, marks_list, attendance, declared_status)
student_records = [
    ("STU-2026-001", "Aarav Nair", "CSE", [88, 91, 84, 92], 92.5, "HONORS"),
    ("STU-2026-002", "Priya Sharma", "ECE", [72, 68, 75, 80], 84.0, "PASS"),
    ("STU-2026-001", "Aarav Clone", "CSE", [80, 82, 85, 88], 90.0, "PASS"),   # Duplicate ID
    ("STU-26-004", "Rohan123", "BIO", [95, 105, -5], None, "PASS"),          # Multiple field errors
    ("STU-2026-005", "", "MECH", [60, 55, 70, 65], 80.0, "PASS"),            # Missing name
    ("STU-2026-006", "Sneha Iyer", "EEE", [35, 80, 78, 82], 88.0, "PASS"),   # Failed subject vs PASS
    ("STU-2026-007", "Karan Verma", "CSE", [90, 88, 86, 84], 68.0, "HONORS"),# Low attendance vs HONORS
    ("STU-2026-008", "Divya Menon", "CIVIL", [78, 74, 80, 76], 82.0, "HONORS"), # Avg < 85 vs HONORS
]

seen_ids = []
valid_count = 0
inconsistent_count = 0

for rec_idx in range(len(student_records)):
    stu_id, name, course, marks, attendance, declared_status = student_records[rec_idx]
    issues = []

    # 1. Validate Student ID format: STU-YYYY-NNN (length 12)
    id_valid = True
    if stu_id is None or len(stu_id) != 12:
        id_valid = False
    else:
        parts = stu_id.split("-")
        if len(parts) != 3 or parts[0] != "STU" or not parts[1].isdigit() or not parts[2].isdigit():
            id_valid = False
        elif len(parts[1]) != 4 or len(parts[2]) != 3:
            id_valid = False
    if not id_valid:
        issues.append(f"Invalid ID format ('{stu_id}', expected STU-YYYY-NNN)")

    # 2. Duplicate ID check
    if stu_id in seen_ids:
        issues.append(f"Duplicate Student ID ('{stu_id}')")
    else:
        seen_ids.append(stu_id)

    # 3. Validate Name (non-empty, letters and spaces only)
    if name is None or name.strip() == "":
        issues.append("Missing student name")
    else:
        name_ok = True
        for ch in name:
            if not (ch.isalpha() or ch == " "):
                name_ok = False
                break
        if not name_ok:
            issues.append(f"Invalid characters in name ('{name}')")

    # 4. Validate Course Code
    if course not in VALID_COURSES:
        issues.append(f"Unknown course code ('{course}')")

    # 5. Validate Marks List
    marks_valid = True
    total_marks = 0
    has_failed_subject = False

    if marks is None or len(marks) != EXPECTED_SUBJECTS:
        marks_valid = False
        issues.append(f"Expected {EXPECTED_SUBJECTS} subject marks, found {0 if marks is None else len(marks)}")
    else:
        for m in marks:
            if m is None:
                marks_valid = False
                issues.append("Missing mark entry (None)")
            elif m < 0 or m > 100:
                marks_valid = False
                issues.append(f"Out-of-range mark ({m})")
            else:
                total_marks += m
                if m < PASS_MARK:
                    has_failed_subject = True

    # 6. Validate Attendance
    att_valid = True
    if attendance is None:
        att_valid = False
        issues.append("Missing attendance value")
    elif attendance < 0.0 or attendance > 100.0:
        att_valid = False
        issues.append(f"Out-of-range attendance ({attendance})")

    # 7. Academic Consistency Check (declared status vs actual metrics)
    if marks_valid and att_valid:
        avg_mark = total_marks / EXPECTED_SUBJECTS
        if declared_status == "PASS":
            if has_failed_subject:
                issues.append("Inconsistent status: declared PASS despite subject mark < 40")
            if attendance < MIN_ATTENDANCE:
                issues.append(f"Inconsistent status: declared PASS with attendance {attendance:.1f}% < 75%")
        elif declared_status == "HONORS":
            if has_failed_subject:
                issues.append("Inconsistent status: declared HONORS despite subject mark < 40")
            if attendance < MIN_ATTENDANCE:
                issues.append(f"Inconsistent status: declared HONORS with attendance {attendance:.1f}% < 75%")
            if avg_mark < HONORS_AVG:
                issues.append(f"Inconsistent status: declared HONORS with avg {avg_mark:.2f}% < 85%")
        elif declared_status != "FAIL":
            issues.append(f"Unknown declared status '{declared_status}'")

    print(f"\nRecord #{rec_idx + 1}: {stu_id} | {name if name else '<EMPTY>'} | Course: {course}")
    if len(issues) == 0:
        valid_count += 1
        avg_val = total_marks / EXPECTED_SUBJECTS
        print(f"  [CONSISTENT] Avg: {avg_val:.2f}% | Att: {attendance:.1f}% | Status: {declared_status}")
    else:
        inconsistent_count += 1
        print(f"  [FLAGGED - {len(issues)} issue(s)]")
        for issue in issues:
            print(f"    - {issue}")

print("\n" + "-" * 78)
print(
    f"AUDIT SUMMARY: Total Records = {len(student_records)} | "
    f"Consistent = {valid_count} | Flagged = {inconsistent_count}"
)
print("=" * 78)
