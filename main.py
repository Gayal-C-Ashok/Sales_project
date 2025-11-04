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
    # Run threaded simulation (if any orders present)
    if orders:
        process_orders_threaded(orders)


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


def process_order(order, worker_id):
    """Simulate a worker processing an order (tiny delay)."""
    import time, random

    time.sleep(random.uniform(0.05, 0.15))
    print(f"Worker-{worker_id} processed Order {order['order_id']}: {order['product']} x{order['quantity']}")


def process_orders_threaded(orders):
    """Process a list of orders concurrently using threads."""
    import threading

    threads = []
    for i, order in enumerate(orders):
        t = threading.Thread(target=process_order, args=(order, i+1))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print("All orders processed (threaded).")


if __name__ == "__main__":
    main()