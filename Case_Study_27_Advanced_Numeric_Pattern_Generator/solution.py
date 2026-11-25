"""
Case Study 27: Advanced Numeric Pattern Generator
Syllabus Used: Variables, data types, operators, conditionals, loops,
strings, pattern generation, lists, tuples, and unpacking.
"""

print("=" * 68)
print("CASE STUDY 27: ADVANCED NUMERIC PATTERN GENERATOR")
print("=" * 68)

MAX_DIM = 9

# Test cases: (case_title, pattern_type, size)
test_cases = [
    ("Test Case 1: Hollow Numeric Diamond (size = 5)", "HOLLOW_DIAMOND", 5),
    ("Test Case 2: Symmetric Numeric Pyramid (size = 6)", "SYMMETRIC_PYRAMID", 6),
    ("Test Case 3: Minimum Valid Dimension (size = 1)", "HOLLOW_DIAMOND", 1),
    ("Test Case 4: Invalid Dimension (size = 0)", "HOLLOW_DIAMOND", 0),
    ("Test Case 5: Invalid Dimension Exceeding Limit (size = 12)", "SYMMETRIC_PYRAMID", 12),
    ("Test Case 6: Unknown Pattern Mode", "SPIRAL", 4),
]

for case_title, pattern_type, size in test_cases:
    print("\n" + "-" * 68)
    print(case_title)
    print("-" * 68)

    mode = pattern_type.strip().upper()
    if mode != "HOLLOW_DIAMOND" and mode != "SYMMETRIC_PYRAMID":
        print(f"ERROR: Unsupported pattern mode '{pattern_type}'.")
        continue

    if size < 1 or size > MAX_DIM:
        print(f"ERROR: Invalid dimension ({size}). Allowed range is 1 to {MAX_DIM}.")
        continue

    if mode == "HOLLOW_DIAMOND":
        # Upper half (1 to size)
        for row in range(1, size + 1):
            line = ""
            # Leading spaces for alignment
            for _ in range(size - row):
                line += "  "
            width = 2 * row - 1
            for col in range(1, width + 1):
                if col == 1 or col == width:
                    line += str(row) + " "
                else:
                    line += "  "
            print(line.rstrip())

        # Lower half (size - 1 down to 1)
        for row in range(size - 1, 0, -1):
            line = ""
            for _ in range(size - row):
                line += "  "
            width = 2 * row - 1
            for col in range(1, width + 1):
                if col == 1 or col == width:
                    line += str(row) + " "
                else:
                    line += "  "
            print(line.rstrip())

    elif mode == "SYMMETRIC_PYRAMID":
        # Symmetric palindrome pyramid: 1 / 1 2 1 / 1 2 3 2 1 ...
        for row in range(1, size + 1):
            line = ""
            for _ in range(size - row):
                line += "  "
            for asc in range(1, row + 1):
                line += str(asc) + " "
            for desc in range(row - 1, 0, -1):
                line += str(desc) + " "
            print(line.rstrip())

print("\n" + "=" * 68)
print("END OF CASE STUDY 27")
print("=" * 68)
