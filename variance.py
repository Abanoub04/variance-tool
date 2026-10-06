import csv
from pathlib import Path

DATA_FILE = Path(__file__).parent / "data.csv"


def main():
    total_budget = 0.0
    total_actual = 0.0

    with open(DATA_FILE, newline="") as f:
        for row in csv.DictReader(f):
            total_budget += float(row["budget"])
            total_actual += float(row["actual"])

    print(f"Total budget: ${total_budget:,.2f}")
    print(f"Total actual: ${total_actual:,.2f}")


if __name__ == "__main__":
    main()
