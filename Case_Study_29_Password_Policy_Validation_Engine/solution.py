"""
Case Study 29: Password Policy Validation Engine
Syllabus Used: Variables, data types, operators, conditionals, loops,
strings, lists, nested lists, tuples, tuple operations, and unpacking.
"""

print("=" * 74)
print("CASE STUDY 29: PASSWORD POLICY VALIDATION ENGINE")
print("=" * 74)

MIN_LENGTH = 8
SPECIAL_CHARS = "!@#$%^&*()-_=+[]{};:,.<>?"
PROHIBITED_SUBSTRINGS = ("password", "admin", "qwerty", "1234", "welcome", "user")

# Test cases: (label, password_string)
test_passwords = [
    ("TC1 (Strong Password)", "C@mpus#2026!"),
    ("TC2 (Too Short & Missing Special)", "Abc12"),
    ("TC3 (Contains Prohibited Substring)", "MyAdmin@2026"),
    ("TC4 (Repeated Characters)", "Securrr#99"),
    ("TC5 (Sequential Characters & Space)", "Test abc#12"),
    ("TC6 (Missing Uppercase & Digit)", "only_lower!"),
    ("TC7 (Strong Edge Case - Length 8)", "K9#mP2!q"),
]

valid_count = 0
invalid_count = 0

for label, pwd in test_passwords:
    print("\n" + "-" * 74)
    print(f"{label} -> Input: '{pwd}'")
    failures = []

    # 1. Minimum length check
    if len(pwd) < MIN_LENGTH:
        failures.append(f"Length is {len(pwd)} (minimum {MIN_LENGTH} required)")

    # 2. Character category & whitespace checks
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False
    has_space = False

    for ch in pwd:
        if ch.isupper():
            has_upper = True
        elif ch.islower():
            has_lower = True
        elif ch.isdigit():
            has_digit = True
        elif ch == " " or ch == "\t":
            has_space = True
        elif ch in SPECIAL_CHARS:
            has_special = True

    if has_space:
        failures.append("Contains whitespace character(s)")
    if not has_upper:
        failures.append("Missing at least one uppercase letter (A-Z)")
    if not has_lower:
        failures.append("Missing at least one lowercase letter (a-z)")
    if not has_digit:
        failures.append("Missing at least one digit (0-9)")
    if not has_special:
        failures.append("Missing at least one special character")

    # 3. Repetition check (3 or more identical consecutive characters)
    has_triple_repeat = False
    for idx in range(len(pwd) - 2):
        if pwd[idx] == pwd[idx + 1] and pwd[idx + 1] == pwd[idx + 2]:
            has_triple_repeat = True
            failures.append(f"3+ consecutive identical characters ('{pwd[idx:idx + 3]}')")
            break

    # 4. Sequential run check (3 ascending chars like abc or 123)
    pwd_lower = pwd.lower()
    for idx in range(len(pwd_lower) - 2):
        c1 = ord(pwd_lower[idx])
        c2 = ord(pwd_lower[idx + 1])
        c3 = ord(pwd_lower[idx + 2])
        if (pwd_lower[idx].isalnum() and pwd_lower[idx + 1].isalnum() and pwd_lower[idx + 2].isalnum()):
            if c2 == c1 + 1 and c3 == c2 + 1:
                failures.append(f"3-character sequential run ('{pwd[idx:idx + 3]}')")
                break

    # 5. Prohibited substring check (case-insensitive)
    for bad in PROHIBITED_SUBSTRINGS:
        if bad in pwd_lower:
            failures.append(f"Contains prohibited substring ('{bad}')")

    if len(failures) == 0:
        valid_count += 1
        strength = "STRONG" if len(pwd) >= 12 else "VALID (MODERATE)"
        print(f"  RESULT: PASS [{strength}] - All policy conditions satisfied.")
    else:
        invalid_count += 1
        print(f"  RESULT: FAIL ({len(failures)} violation(s))")
        for f_idx in range(len(failures)):
            print(f"    {f_idx + 1}. {failures[f_idx]}")

print("\n" + "-" * 74)
print(f"SUMMARY: Total Evaluated = {len(test_passwords)} | Passed = {valid_count} | Failed = {invalid_count}")
print("=" * 74)
