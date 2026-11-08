import unittest
from sales_analyzer import summarize_sales


class SalesAnalyzerTests(unittest.TestCase):
    def test_summary_calculations(self):
        records = [
            {"date": __import__("datetime").date(2026, 1, 1),
             "product": "Pen", "quantity": 2, "unit_price": 5.0,
             "revenue": 10.0},
            {"date": __import__("datetime").date(2026, 1, 2),
             "product": "Book", "quantity": 1, "unit_price": 20.0,
             "revenue": 20.0},
        ]
        result = summarize_sales(records)
        self.assertEqual(result["total_revenue"], 30.0)
        self.assertEqual(result["total_orders"], 2)
        self.assertEqual(result["average_order_value"], 15.0)
        self.assertEqual(result["best_product"], "Pen")

    def test_empty_records_raise_error(self):
        with self.assertRaises(ValueError):
            summarize_sales([])


if __name__ == "__main__":
    unittest.main()
