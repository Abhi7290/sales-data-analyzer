# Sales Data Analyzer

A beginner-friendly Python project that reads sales records from a CSV file and produces a simple summary report.

## Features

- Reads sales data from a CSV file
- Calculates total revenue, number of orders, and average order value
- Finds the best-selling product by quantity
- Summarizes revenue by month
- Works with the included fictional sample dataset
- Uses only the Python standard library

## Requirements

- Python 3.9 or newer
- No third-party packages required

## Run the project

1. Download or clone this repository.
2. Open a terminal in the project folder.
3. Run:

   ```bash
   python sales_analyzer.py
   ```

To analyze another CSV file:

```bash
python sales_analyzer.py path/to/your_sales.csv
```

The CSV must contain these columns:

- `date` (YYYY-MM-DD)
- `product`
- `quantity`
- `unit_price`

## Example output

The program prints overall sales metrics, the best-selling product, and monthly revenue. Exact values depend on the input CSV.

## Sample data

The file `data/sample_sales.csv` contains fictional demonstration records. It does not contain real customer or company data.

## Project status

This is an educational starter project. Contributions, bug reports, and suggestions are welcome.

## License

This project is released under the MIT License. See [LICENSE](LICENSE).
