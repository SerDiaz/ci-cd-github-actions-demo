import unittest
import pandas as pd
from src.transformations import (
    title_dataframe,
    generate_unique_id,
    move_column_to_front
)

class TestTransformations(unittest.TestCase):
    def test_title_dataframe(self):
        # Arrange
        df = pd.DataFrame({"name": ["alice", "bob"], "surname": ["johnson", "smith"]})
        columns = ["name", "surname"]

        # Act
        result = title_dataframe(df, columns)

        # Assert
        expected = pd.DataFrame({"name": ["Alice", "Bob"], "surname": ["Johnson", "Smith"]})
        pd.testing.assert_frame_equal(result, expected)


if __name__ == "__main__":
    unittest.main()
