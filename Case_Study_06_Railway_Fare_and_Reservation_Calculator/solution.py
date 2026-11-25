"""
Case Study 06: Railway Fare and Reservation Calculator
Syllabus Used: Variables, data types, operators, conditionals, loops,
strings, lists, nested lists, tuples, tuple operations, and unpacking.
"""

print("=" * 76)
print("CASE STUDY 06: RAILWAY FARE AND RESERVATION CALCULATOR")
print("=" * 76)

# Travel class definitions as tuples: (class_code, multiplier, reservation_fee)
CLASS_CATALOG = (
    ("SL", 1.0, 20.0),
    ("3A", 2.2, 40.0),
    ("2A", 3.0, 50.0),
    ("1A", 4.5, 60.0),
)

# Flat cancellation fees for >= 48 hours before departure: (class_code, flat_fee)
FLAT_CANCEL_FEES = (
    ("SL", 60.0),
    ("3A", 120.0),
    ("2A", 150.0),
    ("1A", 200.0),
)

# Test cases: (case_title, distance_km, travel_class, passengers_list)
# Passenger tuple: (name, age, cancel_hours)  -> cancel_hours = -1 means active (not cancelled)
test_cases = [
    (
        "Test Case 1: Family Booking (450 km, 3A) with Mixed Concessions & Cancellation",
        450.0,
        "3A",
        [
            ("Ramesh Gupta", 65, -1),
            ("Sunita Gupta", 61, 36),
            ("Arjun Gupta", 34, -1),
            ("Kavya Gupta", 8, -1),
            ("Baby Avi", 3, -1),
        ],
    ),
    (
        "Test Case 2: Long-Distance First AC Booking (820 km, 1A) with Varied Cancellations",
        820.0,
        "1A",
        [
            ("Neha Kapoor", 29, 72),
            ("Siddharth Roy", 41, 8),
            ("Mohan Lal", 70, 2),
        ],
    ),
    (
        "Test Case 3: Validation Check (Invalid Distance, Class, and Age)",
        120.0,
        "SL",
        [
            ("Valid Passenger", 25, -1),
            ("Invalid Age Passenger", -4, -1),
        ],
    ),
    (
        "Test Case 4: Invalid Travel Class and Distance Check",
        -50.0,
        "XX",
        [("Test User", 30, -1)],
    ),
]

for case_title, distance_km, travel_class, passengers in test_cases:
    print("\n" + "-" * 76)
    print(case_title)
    print("-" * 76)

    # Validate distance
    if distance_km <= 0:
        print(f"ERROR: Invalid journey distance ({distance_km} km). Must be > 0.")
        continue

    # Lookup travel class
    class_found = False
    multiplier = 0.0
    reservation_fee = 0.0
    flat_cancel_fee = 0.0

    for code, mult, res_fee in CLASS_CATALOG:
        if code == travel_class:
            class_found = True
            multiplier = mult
            reservation_fee = res_fee
            break

    if not class_found:
        print(f"ERROR: Invalid travel class '{travel_class}'. Allowed: SL, 3A, 2A, 1A.")
        continue

    for code, c_fee in FLAT_CANCEL_FEES:
        if code == travel_class:
            flat_cancel_fee = c_fee
            break

    # Progressive distance slab base fare (per adult before class multiplier)
    # 0 - 100 km   : Rs 1.20 / km
    # 101 - 300 km : Rs 1.00 / km
    # 301 - 600 km : Rs 0.85 / km
    # > 600 km     : Rs 0.70 / km
    remaining_km = distance_km
    slab_fare = 0.0

    if remaining_km > 600:
        slab_fare += (remaining_km - 600) * 0.70
        remaining_km = 600
    if remaining_km > 300:
        slab_fare += (remaining_km - 300) * 0.85
        remaining_km = 300
    if remaining_km > 100:
        slab_fare += (remaining_km - 100) * 1.00
        remaining_km = 100
    slab_fare += remaining_km * 1.20

    base_class_fare = slab_fare * multiplier

    print(
        f"Distance: {distance_km:.1f} km | Class: {travel_class} | "
        f"Base Class Fare: Rs {base_class_fare:.2f} | Reservation Fee: Rs {reservation_fee:.2f}"
    )
    print(
        f"\n  {'Passenger':<18} {'Age':>4} {'Concession':<12} {'Ticket':>9} "
        f"{'Status':<11} {'Penalty':>9} {'Net/Refund':>10}"
    )
    print("  " + "-" * 74)

    total_collected = 0.0
    total_penalties = 0.0
    total_refunds = 0.0
    valid_count = 0

    for passenger in passengers:
        p_name, age, cancel_hours = passenger

        if age < 0 or age > 120:
            print(f"  {p_name:<18} {age:>4}  [REJECTED: Invalid passenger age]")
            continue

        valid_count += 1
        # Age-based concession
        if age < 5:
            concession_rate = 1.0
            concession_label = "Child Free"
            p_res_fee = 0.0
        elif age <= 11:
            concession_rate = 0.50
            concession_label = "Child 50%"
            p_res_fee = reservation_fee
        elif age >= 60:
            concession_rate = 0.40
            concession_label = "Senior 40%"
            p_res_fee = reservation_fee
        else:
            concession_rate = 0.0
            concession_label = "None"
            p_res_fee = reservation_fee

        ticket_fare = base_class_fare * (1.0 - concession_rate) + p_res_fee

        if cancel_hours < 0:
            status_label = "CONFIRMED"
            penalty = 0.0
            refund = 0.0
            total_collected += ticket_fare
            net_display = f"{ticket_fare:>10.2f}"
        else:
            status_label = f"CANCEL({cancel_hours}h)"
            if ticket_fare == 0.0:
                penalty = 0.0
            elif cancel_hours >= 48:
                penalty = flat_cancel_fee
                if penalty > ticket_fare:
                    penalty = ticket_fare
            elif cancel_hours >= 12:
                pct_penalty = 0.25 * ticket_fare
                penalty = pct_penalty if pct_penalty > flat_cancel_fee else flat_cancel_fee
                if penalty > ticket_fare:
                    penalty = ticket_fare
            elif cancel_hours >= 4:
                penalty = 0.50 * ticket_fare
            else:
                penalty = ticket_fare

            refund = ticket_fare - penalty
            total_penalties += penalty
            total_refunds += refund
            net_display = f"{refund:>10.2f}"

        print(
            f"  {p_name:<18} {age:>4} {concession_label:<12} {ticket_fare:>9.2f} "
            f"{status_label:<11} {penalty:>9.2f} {net_display}"
        )

    print("  " + "-" * 74)
    print(
        f"  Summary ({valid_count} valid passengers): "
        f"Confirmed Revenue = Rs {total_collected:.2f} | "
        f"Penalties Retained = Rs {total_penalties:.2f} | "
        f"Refunds Issued = Rs {total_refunds:.2f}"
    )

print("\n" + "=" * 76)
print("END OF CASE STUDY 06")
print("=" * 76)
