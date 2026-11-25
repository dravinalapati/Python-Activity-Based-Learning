"""
Case Study 01: University Scholarship Allocation
Syllabus Used: Variables, data types, operators, conditionals, loops,
strings, lists, nested lists, tuples, tuple operations, and unpacking.
"""

print("=" * 72)
print("CASE STUDY 01: UNIVERSITY SCHOLARSHIP ALLOCATION SYSTEM")
print("=" * 72)

# Policy constants
MIN_SUBJECT_MARK = 50
MIN_AGGREGATE_PCT = 75.0
MIN_ATTENDANCE_PCT = 80.0
MAX_ANNUAL_INCOME = 500000
SUBJECT_NAMES = ("Math", "Physics", "Chemistry", "English", "CS")

# Each test case is a tuple: (case_title, applicants_list)
# Each applicant is a tuple: (app_id, name, marks_list, attendance_pct, income)
test_cases = [
    (
        "Test Case 1: Standard Cohort with Tie-Breaking Scenarios",
        [
            ("APP101", "Aarav Sharma", [92, 88, 85, 80, 95], 91.5, 320000),
            ("APP102", "Diya Nair", [90, 90, 88, 82, 90], 94.0, 280000),
            ("APP103", "Rohan Verma", [92, 88, 85, 80, 95], 91.5, 250000),
            ("APP104", "Sneha Iyer", [45, 95, 92, 88, 90], 89.0, 200000),
            ("APP105", "Kabir Mehta", [80, 78, 76, 75, 81], 74.0, 300000),
            ("APP106", "Meera Joshi", [85, 84, 82, 80, 89], 88.0, 620000),
        ],
    ),
    (
        "Test Case 2: Boundary Threshold Verification",
        [
            ("APP201", "Vikram Rao", [50, 75, 80, 85, 85], 80.0, 500000),
            ("APP202", "Ananya Das", [49, 90, 90, 90, 90], 95.0, 150000),
            ("APP203", "Karan Patel", [74, 75, 75, 75, 75], 85.0, 400000),
            ("APP204", "Pooja Kulkarni", [82, 80, 78, 84, 86], 79.9, 350000),
        ],
    ),
    (
        "Test Case 3: No Eligible Applicants Scenario",
        [
            ("APP301", "Nikhil Sen", [60, 62, 65, 68, 70], 70.0, 550000),
            ("APP302", "Tara Bose", [40, 80, 82, 79, 85], 85.0, 200000),
        ],
    ),
]

for tc_index in range(len(test_cases)):
    case_title, applicants = test_cases[tc_index]
    print("\n" + "-" * 72)
    print(case_title)
    print("-" * 72)

    eligible_records = []
    ineligible_records = []

    for applicant in applicants:
        app_id, name, marks, attendance, income = applicant

        # Compute aggregate and subject checks
        total_marks = 0
        failed_subjects = []
        valid_marks = True

        if len(marks) != len(SUBJECT_NAMES):
            valid_marks = False
        else:
            for idx in range(len(marks)):
                score = marks[idx]
                if score < 0 or score > 100:
                    valid_marks = False
                total_marks += score
                if score < MIN_SUBJECT_MARK:
                    failed_subjects.append((SUBJECT_NAMES[idx], score))

        reasons = []
        aggregate_pct = 0.0
        math_cs_total = 0

        if not valid_marks:
            reasons.append("Invalid marks record")
        else:
            aggregate_pct = total_marks / len(marks)
            math_cs_total = marks[0] + marks[4]

            if len(failed_subjects) > 0:
                subj_text = ""
                for s_idx in range(len(failed_subjects)):
                    s_name, s_score = failed_subjects[s_idx]
                    if s_idx > 0:
                        subj_text += ", "
                    subj_text += s_name + "(" + str(s_score) + ")"
                reasons.append("Subject score < 50: " + subj_text)

            if aggregate_pct < MIN_AGGREGATE_PCT:
                reasons.append(f"Aggregate {aggregate_pct:.2f}% < {MIN_AGGREGATE_PCT:.1f}%")

        if attendance < MIN_ATTENDANCE_PCT:
            reasons.append(f"Attendance {attendance:.1f}% < {MIN_ATTENDANCE_PCT:.1f}%")

        if income > MAX_ANNUAL_INCOME:
            reasons.append(f"Income {income} > {MAX_ANNUAL_INCOME}")

        if len(reasons) == 0:
            # Tuple packing for sorting and reporting
            eligible_records.append(
                (aggregate_pct, math_cs_total, attendance, income, app_id, name)
            )
        else:
            ineligible_records.append((app_id, name, aggregate_pct, reasons))

    # Deterministic tie-breaking bubble sort:
    # 1. Higher aggregate_pct
    # 2. Higher math_cs_total
    # 3. Higher attendance
    # 4. Lower annual income
    # 5. Lexicographically smaller app_id
    n = len(eligible_records)
    for i in range(n):
        for j in range(0, n - i - 1):
            agg1, mc1, att1, inc1, id1, _ = eligible_records[j]
            agg2, mc2, att2, inc2, id2, _ = eligible_records[j + 1]

            swap_needed = False
            if agg1 < agg2:
                swap_needed = True
            elif agg1 == agg2:
                if mc1 < mc2:
                    swap_needed = True
                elif mc1 == mc2:
                    if att1 < att2:
                        swap_needed = True
                    elif att1 == att2:
                        if inc1 > inc2:
                            swap_needed = True
                        elif inc1 == inc2 and id1 > id2:
                            swap_needed = True

            if swap_needed:
                eligible_records[j], eligible_records[j + 1] = (
                    eligible_records[j + 1],
                    eligible_records[j],
                )

    print("\nELIGIBLE & RANKED APPLICANTS:")
    if len(eligible_records) == 0:
        print("  None of the applicants met all scholarship criteria.")
    else:
        print(
            f"  {'Rank':<5} {'ID':<8} {'Name':<16} {'Agg(%)':>7} {'Math+CS':>8} {'Att(%)':>7} {'Income':>10}"
        )
        print("  " + "-" * 65)
        for rank_idx in range(len(eligible_records)):
            agg, mc, att, inc, app_id, name = eligible_records[rank_idx]
            print(
                f"  {rank_idx + 1:<5} {app_id:<8} {name:<16} {agg:>7.2f} {mc:>8} {att:>7.1f} {inc:>10}"
            )

    print("\nINELIGIBLE APPLICANTS:")
    if len(ineligible_records) == 0:
        print("  All applicants were eligible.")
    else:
        for rec in ineligible_records:
            app_id, name, agg, reasons = rec
            reason_str = "; ".join(reasons)
            print(f"  - {app_id} ({name}, Agg: {agg:.2f}%): {reason_str}")

print("\n" + "=" * 72)
print("END OF CASE STUDY 01")
print("=" * 72)
