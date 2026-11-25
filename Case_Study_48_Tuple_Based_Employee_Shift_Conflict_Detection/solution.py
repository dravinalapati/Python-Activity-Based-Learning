"""
Case Study 48: Tuple-Based Employee Shift Conflict Detection
Syllabus Used: Variables, data types, operators, conditionals, loops,
strings, lists, nested lists, tuples, tuple operations, and unpacking.
"""

print("=" * 76)
print("CASE STUDY 48: TUPLE-BASED EMPLOYEE SHIFT CONFLICT DETECTION")
print("=" * 76)

# Each shift is a tuple: (shift_id, emp_id, emp_name, day, start_hhmm, end_hhmm)
test_cases = [
    (
        "Test Case 1: Overlapping, Back-to-Back (Valid), and Invalid Shift Intervals",
        [
            ("SH01", "E101", "Asha Menon", "Mon", "09:00", "13:00"),
            ("SH02", "E101", "Asha Menon", "Mon", "12:30", "16:30"),  # Overlaps SH01
            ("SH03", "E101", "Asha Menon", "Tue", "09:00", "17:00"),
            ("SH04", "E102", "Dev Kumar", "Mon", "08:00", "12:00"),
            ("SH05", "E102", "Dev Kumar", "Mon", "12:00", "16:00"),   # Back-to-back, NO overlap
            ("SH06", "E103", "Ritu Shah", "Wed", "10:00", "14:00"),
            ("SH07", "E103", "Ritu Shah", "Wed", "11:00", "12:00"),   # Contained inside SH06
            ("SH08", "E103", "Ritu Shah", "Wed", "13:30", "18:00"),   # Overlaps SH06
            ("SH09", "E104", "Zaid Khan", "Thu", "15:00", "14:00"),   # Invalid end <= start
        ],
    ),
    (
        "Test Case 2: Conflict-Free Schedule",
        [
            ("SH11", "E201", "Nisha Verma", "Mon", "09:00", "13:00"),
            ("SH12", "E201", "Nisha Verma", "Mon", "14:00", "18:00"),
            ("SH13", "E202", "Omkar Joshi", "Mon", "09:00", "17:00"),
        ],
    ),
]

for case_title, raw_shifts in test_cases:
    print("\n" + "-" * 76)
    print(case_title)
    print("-" * 76)

    valid_shifts = []
    invalid_shifts = []

    for shift in raw_shifts:
        shift_id, emp_id, emp_name, day, start_str, end_str = shift

        # Parse HH:MM strings using string split and arithmetic
        s_parts = start_str.split(":")
        e_parts = end_str.split(":")
        valid_format = (
            len(s_parts) == 2
            and len(e_parts) == 2
            and s_parts[0].isdigit()
            and s_parts[1].isdigit()
            and e_parts[0].isdigit()
            and e_parts[1].isdigit()
        )

        if not valid_format:
            invalid_shifts.append((shift_id, emp_id, "Malformed time string"))
            continue

        s_hr = int(s_parts[0])
        s_min = int(s_parts[1])
        e_hr = int(e_parts[0])
        e_min = int(e_parts[1])

        if s_hr > 23 or s_min > 59 or e_hr > 23 or e_min > 59:
            invalid_shifts.append((shift_id, emp_id, "Time out of 24-hour range"))
            continue

        start_total = s_hr * 60 + s_min
        end_total = e_hr * 60 + e_min

        if end_total <= start_total:
            invalid_shifts.append((shift_id, emp_id, f"End time ({end_str}) <= start time ({start_str})"))
            continue

        # Store enriched tuple using tuple concatenation
        valid_shifts.append(shift + (start_total, end_total))

    conflicts = []
    conflicted_employees = []

    # Pairwise comparison via nested loops
    for i in range(len(valid_shifts)):
        sid1, eid1, ename1, day1, s1_str, e1_str, s1_min, e1_min = valid_shifts[i]
        for j in range(i + 1, len(valid_shifts)):
            sid2, eid2, ename2, day2, s2_str, e2_str, s2_min, e2_min = valid_shifts[j]

            if eid1 == eid2 and day1 == day2:
                # Strict interval overlap: start1 < end2 and start2 < end1
                if s1_min < e2_min and s2_min < e1_min:
                    overlap_start = s1_min if s1_min > s2_min else s2_min
                    overlap_end = e1_min if e1_min < e2_min else e2_min
                    overlap_mins = overlap_end - overlap_start
                    conflicts.append(
                        (
                            eid1,
                            ename1,
                            day1,
                            sid1,
                            s1_str + "-" + e1_str,
                            sid2,
                            s2_str + "-" + e2_str,
                            overlap_mins,
                        )
                    )
                    emp_tag = (eid1, ename1)
                    if emp_tag not in conflicted_employees:
                        conflicted_employees.append(emp_tag)

    print(f"  Valid Shifts Checked: {len(valid_shifts)} | Invalid Shifts Flagged: {len(invalid_shifts)}")
    if len(invalid_shifts) > 0:
        print("\n  INVALID SHIFT RECORDS:")
        for sid, eid, reason in invalid_shifts:
            print(f"    ! {sid} ({eid}): {reason}")

    print("\n  DETECTED SHIFT CONFLICTS:")
    if len(conflicts) == 0:
        print("    None — all valid employee shifts are conflict-free.")
    else:
        for eid, ename, day, sid1, r1, sid2, r2, mins in conflicts:
            print(
                f"    * {eid} ({ename}) on {day}: {sid1} [{r1}] overlaps {sid2} [{r2}] "
                f"by {mins} mins"
            )

    print("\n  EMPLOYEES WITH CONFLICTING SCHEDULES:")
    if len(conflicted_employees) == 0:
        print("    None.")
    else:
        for eid, ename in conflicted_employees:
            print(f"    - {eid}: {ename}")

print("\n" + "=" * 76)
print("END OF CASE STUDY 48")
print("=" * 76)
