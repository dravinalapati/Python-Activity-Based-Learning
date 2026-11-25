"""
Case Study 57: Smart Canteen Order and Stock Management
Syllabus Used: Variables, data types, operators, conditionals, loops,
strings, lists, nested lists, tuples, tuple operations, and unpacking.
"""

print("=" * 76)
print("CASE STUDY 57: SMART CANTEEN ORDER AND STOCK MANAGEMENT")
print("=" * 76)

LOW_STOCK_THRESHOLD = 5

# Initial inventory template: tuple of tuples (code, name, unit_price, stock_qty)
INITIAL_MENU = (
    ("M01", "Masala Dosa", 55.0, 12),
    ("M02", "Veg Sandwich", 40.0, 8),
    ("M03", "Filter Coffee", 25.0, 20),
    ("M04", "Paneer Roll", 75.0, 5),
    ("M05", "Mango Juice", 35.0, 6),
)

# Successive customer orders: (order_id, customer_name, items_list)
# Each item in items_list is a tuple: (item_code, requested_qty)
customer_orders = [
    ("ORD01", "Riya", [("M01", 4), ("M03", 5)]),
    ("ORD02", "Aditya", [("M04", 3), ("M02", 4)]),
    ("ORD03", "Sanya", [("M04", 4), ("M01", 2)]),      # M04 only has 2 left -> rejected item
    ("ORD04", "Kunal", [("M05", 6), ("M99", 1)]),      # M99 unknown item -> rejected item
    ("ORD05", "Megha", [("M01", -2), ("M03", 10)]),    # -2 invalid qty -> rejected item
    ("ORD06", "Tarun", [("M02", 4), ("M03", 5)]),
]

# Copy initial menu into mutable nested list for stock updates and sales tracking
# Format: [code, name, unit_price, current_stock, units_sold, revenue]
inventory = []
for code, name, price, stock in INITIAL_MENU:
    inventory.append([code, name, price, stock, 0, 0.0])

total_daily_revenue = 0.0
total_orders_fulfilled = 0
rejected_line_items = []

print("\nPROCESSING CUSTOMER ORDERS:")
print("-" * 76)

for order_id, customer, items in customer_orders:
    print(f"\nOrder {order_id} | Customer: {customer}")
    order_total = 0.0
    accepted_lines = 0

    for item_code, qty in items:
        if qty <= 0:
            msg = f"Invalid quantity ({qty}) for {item_code}"
            print(f"  [REJECTED] {msg}")
            rejected_line_items.append((order_id, item_code, qty, msg))
            continue

        # Search item in inventory nested list
        found_idx = -1
        for idx in range(len(inventory)):
            if inventory[idx][0] == item_code:
                found_idx = idx
                break

        if found_idx == -1:
            msg = f"Unknown item code '{item_code}'"
            print(f"  [REJECTED] {msg}")
            rejected_line_items.append((order_id, item_code, qty, msg))
            continue

        code, name, price, stock, sold, rev = inventory[found_idx]
        if qty > stock:
            msg = f"Insufficient stock for {name} (Requested: {qty}, Available: {stock})"
            print(f"  [REJECTED] {msg}")
            rejected_line_items.append((order_id, item_code, qty, msg))
            continue

        # Accept line item and update stock
        line_cost = qty * price
        inventory[found_idx][3] = stock - qty
        inventory[found_idx][4] = sold + qty
        inventory[found_idx][5] = rev + line_cost
        order_total += line_cost
        accepted_lines += 1
        print(f"  [ACCEPTED] {name:<15} x {qty:<3} @ Rs {price:>5.2f} = Rs {line_cost:>7.2f}")

    if accepted_lines > 0:
        total_orders_fulfilled += 1
        total_daily_revenue += order_total
    print(f"  -> Order Bill Total: Rs {order_total:.2f}")

print("\n" + "-" * 76)
print("DAILY SALES & REMAINING INVENTORY SUMMARY")
print("-" * 76)
print(
    f"  {'Code':<6} {'Item Name':<16} {'Price':>7} {'Sold':>6} {'Remaining':>10} {'Revenue':>10}  Stock Alert"
)
print("  " + "-" * 72)

for record in inventory:
    code, name, price, remaining, sold, rev = record
    if remaining == 0:
        alert = "OUT OF STOCK"
    elif remaining <= LOW_STOCK_THRESHOLD:
        alert = "LOW STOCK"
    else:
        alert = "OK"
    print(
        f"  {code:<6} {name:<16} {price:>7.2f} {sold:>6} {remaining:>10} {rev:>10.2f}  {alert}"
    )

print("  " + "-" * 72)
print(f"  Total Orders With Accepted Items : {total_orders_fulfilled} / {len(customer_orders)}")
print(f"  Total Rejected Line Items        : {len(rejected_line_items)}")
print(f"  Total Daily Sales Revenue        : Rs {total_daily_revenue:.2f}")
print("=" * 76)
