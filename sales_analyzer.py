"""Analyze sales records from a CSV file using only Python's standard library."""

import csv
import sys
from collections import defaultdict
from datetime import datetime
from pathlib import Path


DEFAULT_FILE = Path(__file__).parent / "data" / "sample_sales.csv"


def load_sales(file_path):
    """Load and validate sales rows from a CSV file."""
    records = []
    with open(file_path, newline="", encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)
        required = {"date", "product", "quantity", "unit_price"}
        if not reader.fieldnames or not required.issubset(reader.fieldnames):
            raise ValueError(
                "CSV must contain: date, product, quantity, unit_price"
            )

        for line_number, row in enumerate(reader, start=2):
            try:
                date = datetime.strptime(row["date"], "%Y-%m-%d").date()
                product = row["product"].strip()
                quantity = int(row["quantity"])
                unit_price = float(row["unit_price"])
                if not product or quantity < 0 or unit_price < 0:
                    raise ValueError
            except (TypeError, ValueError):
                raise ValueError(f"Invalid data on CSV line {line_number}")

            records.append({
                "date": date,
                "product": product,
                "quantity": quantity,
                "unit_price": unit_price,
                "revenue": quantity * unit_price,
            })
    return records


def summarize_sales(records):
    """Return overall, product, and monthly sales metrics."""
    if not records:
        raise ValueError("The CSV contains no sales records.")

    total_revenue = sum(row["revenue"] for row in records)
    total_orders = len(records)
    total_quantity = sum(row["quantity"] for row in records)

    product_quantity = defaultdict(int)
    monthly_revenue = defaultdict(float)

    for row in records:
        product_quantity[row["product"]] += row["quantity"]
        month = row["date"].strftime("%Y-%m")
        monthly_revenue[month] += row["revenue"]

    best_product = max(product_quantity, key=product_quantity.get)

    return {
        "total_revenue": total_revenue,
        "total_orders": total_orders,
        "average_order_value": total_revenue / total_orders,
        "total_quantity": total_quantity,
        "best_product": best_product,
        "best_product_quantity": product_quantity[best_product],
        "monthly_revenue": dict(sorted(monthly_revenue.items())),
    }


def print_report(summary):
    """Print a readable sales report."""
    print("\nSALES SUMMARY")
    print("=" * 32)
    print(f"Total revenue:       {summary['total_revenue']:.2f}")
    print(f"Number of orders:    {summary['total_orders']}")
    print(f"Average order value: {summary['average_order_value']:.2f}")
    print(f"Units sold:          {summary['total_quantity']}")
    print(
        f"Best-selling product: {summary['best_product']} "
        f"({summary['best_product_quantity']} units)"
    )

    print("\nMONTHLY REVENUE")
    print("-" * 32)
    for month, revenue in summary["monthly_revenue"].items():
        print(f"{month}: {revenue:.2f}")


def main():
    file_path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_FILE
    try:
        records = load_sales(file_path)
        summary = summarize_sales(records)
        print_report(summary)
    except (OSError, ValueError) as error:
        print(f"Error: {error}", file=sys.stderr)
        raise SystemExit(1)


if __name__ == "__main__":
    main()
