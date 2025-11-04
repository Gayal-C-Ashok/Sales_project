"""
Sales project - starter

This is a minimal starter `main.py` used for the initial commit.
Feature implementations will be added on feature branches.
"""

def main():
    print("Sales project starter - running data processing demo")
    orders = process_data()
    # Print a short summary
    print(f"Loaded {len(orders)} orders")


def process_data():
    """Read `sales_data.csv` and return parsed orders list.

    Returns a list of dicts with keys: order_id, product, quantity, price, region
    """
    import csv

    orders = []
    with open('sales_data.csv', 'r', newline='') as fh:
        reader = csv.DictReader(fh)
        for row in reader:
            # basic parsing with defensive casts
            try:
                orders.append({
                    'order_id': int(row['order_id']),
                    'product': row['product'],
                    'quantity': int(row['quantity']),
                    'price': float(row['price']),
                    'region': row['region']
                })
            except Exception:
                # skip malformed rows
                continue

    # Calculate simple report values (not printed here)
    return orders


if __name__ == "__main__":
    main()