import os
import sys
import pandas as pd
import unittest

# Add the project's root directory to PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

from src.main import main

class TestMainQA(unittest.TestCase):
    def test_main_output(self):
        # Execute the script and retrieve the generated DataFrames
        actual_people_df, actual_sales_df = main()
        
        # Ensure the DataFrames are not None
        self.assertIsNotNone(actual_people_df, "People DataFrame was not generated correctly")
        self.assertIsNotNone(actual_sales_df, "Sales DataFrame was not generated correctly")
        
        # Determine the root directory of the project
        project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../.."))
        
        # Load expected results from CSV files
        expected_people_file = os.path.join(project_root, "data", "expected_people.csv")
        expected_sales_file = os.path.join(project_root, "data", "expected_sales.csv")
        
        # Ensure the files exist (optional)
        self.assertTrue(os.path.exists(expected_people_file), "Expected people file does not exist")
        self.assertTrue(os.path.exists(expected_sales_file), "Expected sales file does not exist")
        
        # Load the expected DataFrames
        expected_people_df = pd.read_csv(expected_people_file, dtype={
            "person_id": "int64",
            "first_name": "string",
            "last_name": "string",
            "birth_place": "string",
            "birth_date": "string",
            "email": "string",
            "residence": "string"
        })
        
        expected_sales_df = pd.read_csv(expected_sales_file, dtype={
            "sales_id": "int64",
            "item": "string",
            "price": "float64",
            "sale_date": "string",
            "person_id": "int64"
        })
        
        # Compare the actual and expected DataFrames
        pd.testing.assert_frame_equal(actual_people_df, expected_people_df)
        pd.testing.assert_frame_equal(actual_sales_df, expected_sales_df)

if __name__ == "__main__":
    unittest.main()