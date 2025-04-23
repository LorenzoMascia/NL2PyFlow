# tests/test_block_parser.py
import unittest
from core.block_parser import parse_blocks

class TestBlockParser(unittest.TestCase):

    def test_parse_blocks_with_numbers(self):
        input_text = """
### Block 1: Load data
Load CSV "sales.csv" into a list of records.

### Block 2: Filter high-value
Filter records with amount > 1000.

### Block 3: Compute total
Sum all amounts and store in context["total_sales"].
"""
        expected = [
            {"name": "block_1", "title": "Load data", "description": 'Load CSV "sales.csv" into a list of records.'},
            {"name": "block_2", "title": "Filter high-value", "description": "Filter records with amount > 1000."},
            {"name": "block_3", "title": "Compute total", "description": 'Sum all amounts and store in context["total_sales"].'},
        ]

        result = parse_blocks(input_text)
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()
