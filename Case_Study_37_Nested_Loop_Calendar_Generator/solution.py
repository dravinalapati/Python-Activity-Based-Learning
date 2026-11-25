"""
Case Study 37: Nested Loop Calendar Generator
Syllabus Used: Variables, data types, operators, conditionals, loops,
strings, pattern generation, lists, tuples, tuple operations, and unpacking.
"""

print("=" * 68)
print("CASE STUDY 37: NESTED LOOP CALENDAR GENERATOR")
print("=" * 68)

WEEKDAYS = ("SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT")
VALID_MONTH_LENGTHS = (28, 29, 30, 31)

# Test cases: (case_title, month_label, start_weekday_code, num_days)
test_cases = [
    ("Test Case 1: 31-Day Month Starting Wednesday", "January 2026", "WED", 31),
    ("Test Case 2: 28-Day Non-Leap February Starting Sunday", "February 2026", "SUN", 28),
    ("Test Case 3: 30-Day Month Starting Friday (6-row span)", "May 2026 (30d test)", "FRI", 30),
    ("Test Case 4: Invalid Month Length (32 days)", "Invalid Month A", "MON", 32),
    ("Test Case 5: Invalid Starting Weekday ('XYZ')", "Invalid Month B", "XYZ", 30),
]

for case_title, month_label, start_code, num_days in test_cases:
    print("\n" + "-" * 68)
    print(f"{case_title} -> {month_label}")
    print("-" * 68)

    code_clean = start_code.strip().upper()
    start_idx = -1
    for i in range(len(WEEKDAYS)):
        if WEEKDAYS[i] == code_clean:
            start_idx = i
            break

    if start_idx == -1:
        print(f"ERROR: Invalid starting weekday '{start_code}'. Expected one of {WEEKDAYS}.")
        continue

    if num_days not in VALID_MONTH_LENGTHS:
        print(f"ERROR: Invalid month length ({num_days}). Allowed lengths: 28, 29, 30, 31.")
        continue

    # Header
    print(f"\n          {month_label}")
    header_line = "  "
    for day_name in WEEKDAYS:
        header_line += f"{day_name:>4}"
    print(header_line)
    print("  " + "-" * 28)

    # Nested loop calendar grid generation
    current_day = 1
    week_count = 0
    end_weekday_idx = (start_idx + num_days - 1) % 7

    while current_day <= num_days:
        week_row = "  "
        for col in range(7):
            if week_count == 0 and col < start_idx:
                week_row += "    "
            elif current_day <= num_days:
                week_row += f"{current_day:>4}"
                current_day += 1
            else:
                week_row += "    "
        print(week_row.rstrip())
        week_count += 1

    print("  " + "-" * 28)
    print(
        f"  Summary: Total Days = {num_days} | Weeks Spanned = {week_count} | "
        f"Starts = {WEEKDAYS[start_idx]} | Ends = {WEEKDAYS[end_weekday_idx]}"
    )

print("\n" + "=" * 68)
print("END OF CASE STUDY 37")
print("=" * 68)
