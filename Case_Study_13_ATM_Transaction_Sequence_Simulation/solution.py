"""
Case Study 13: ATM Transaction Sequence Simulation
Syllabus Used: Variables, data types, operators, conditionals, loops,
strings, lists, nested lists, tuples, tuple operations, and unpacking.
"""

print("=" * 72)
print("CASE STUDY 13: ATM TRANSACTION SEQUENCE SIMULATION")
print("=" * 72)

MIN_BALANCE = 500.0
MAX_PER_WITHDRAWAL = 10000.0
MAX_DAILY_WITHDRAWAL = 25000.0
DENOMINATION_UNIT = 100

# Test scenarios: (case_title, initial_balance, transactions_list)
# Transaction tuple: (txn_id, txn_type, amount)
test_cases = [
    (
        "Test Case 1: Mixed Deposits, Valid Withdrawals, and Limit/Balance Rejections",
        12000.0,
        [
            ("TXN01", "WITHDRAW", 4000.0),
            ("TXN02", "DEPOSIT", 5500.0),
            ("TXN03", "WITHDRAW", 12000.0),   # Exceeds per-transaction limit (10000)
            ("TXN04", "WITHDRAW", 2550.0),    # Not a multiple of 100
            ("TXN05", "WITHDRAW", 9000.0),
            ("TXN06", "WITHDRAW", 5000.0),    # Leaves 500 (exact min balance)
            ("TXN07", "WITHDRAW", 100.0),     # Would breach min balance 500
            ("TXN08", "DEPOSIT", -500.0),     # Negative amount
        ],
    ),
    (
        "Test Case 2: Cumulative Daily Withdrawal Limit Enforcement",
        40000.0,
        [
            ("TXN11", "WITHDRAW", 10000.0),
            ("TXN12", "WITHDRAW", 10000.0),
            ("TXN13", "WITHDRAW", 5000.0),
            ("TXN14", "WITHDRAW", 1000.0),    # Exceeds daily 25000 limit
            ("TXN15", "TRANSFER", 500.0),     # Unsupported transaction type
        ],
    ),
]

for case_title, initial_balance, transactions in test_cases:
    print("\n" + "-" * 72)
    print(case_title)
    print(f"Opening Balance: Rs {initial_balance:.2f}")
    print("-" * 72)

    balance = initial_balance
    daily_withdrawn = 0.0
    total_deposited = 0.0
    approved_count = 0
    rejected_count = 0

    audit_log = []

    for txn in transactions:
        txn_id, txn_type, amount = txn
        txn_type_clean = txn_type.strip().upper()
        status = "REJECTED"
        note = ""

        if amount <= 0:
            note = "Amount must be positive"
        elif txn_type_clean == "DEPOSIT":
            balance += amount
            total_deposited += amount
            approved_count += 1
            status = "APPROVED"
            note = "Cash deposited"
        elif txn_type_clean == "WITHDRAW":
            if amount % DENOMINATION_UNIT != 0:
                note = f"Amount must be a multiple of Rs {DENOMINATION_UNIT}"
            elif amount > MAX_PER_WITHDRAWAL:
                note = f"Exceeds per-txn limit (Rs {MAX_PER_WITHDRAWAL:.0f})"
            elif daily_withdrawn + amount > MAX_DAILY_WITHDRAWAL:
                note = f"Exceeds daily limit (Rs {MAX_DAILY_WITHDRAWAL:.0f})"
            elif balance - amount < MIN_BALANCE:
                note = f"Violates minimum balance (Rs {MIN_BALANCE:.0f})"
            else:
                balance -= amount
                daily_withdrawn += amount
                approved_count += 1
                status = "APPROVED"
                note = "Cash dispensed"
        else:
            note = f"Unsupported type '{txn_type}'"

        if status == "REJECTED":
            rejected_count += 1

        audit_log.append((txn_id, txn_type_clean, amount, status, balance, note))

    print(
        f"  {'ID':<7} {'Type':<10} {'Amount':>10} {'Status':<10} {'Balance':>11}  Note"
    )
    print("  " + "-" * 68)
    for log_entry in audit_log:
        tid, ttype, amt, stat, bal, msg = log_entry
        print(
            f"  {tid:<7} {ttype:<10} {amt:>10.2f} {stat:<10} {bal:>11.2f}  {msg}"
        )

    print("\n  TRANSACTION SUMMARY:")
    print(f"    Total Transactions Processed : {len(transactions)}")
    print(f"    Approved Transactions        : {approved_count}")
    print(f"    Rejected Transactions        : {rejected_count}")
    print(f"    Total Deposited              : Rs {total_deposited:.2f}")
    print(f"    Total Withdrawn              : Rs {daily_withdrawn:.2f}")
    print(f"    Closing Balance              : Rs {balance:.2f}")

print("\n" + "=" * 72)
print("END OF CASE STUDY 13")
print("=" * 72)
