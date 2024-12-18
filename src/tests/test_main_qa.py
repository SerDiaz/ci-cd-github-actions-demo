import os
import sys
import pandas as pd
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from src.main import main

def test_main_output():
    # Ejecutar el script y obtener los DataFrames generados
    actual_people_df, actual_sales_df = main()
    
    # Verificar que los DataFrames no son None
    assert actual_people_df is not None, "People DataFrame no fue generado correctamente"
    assert actual_sales_df is not None, "Sales DataFrame no fue generado correctamente"
    
    # Cargar los resultados esperados directamente
    data_dir = os.path.join(os.path.dirname(__file__), "..", "data")
    expected_people_file = os.path.join(data_dir, "expected_people.csv")
    expected_sales_file = os.path.join(data_dir, "expected_sales.csv")
    
    expected_people_df = pd.read_csv(expected_people_file)
    expected_sales_df = pd.read_csv(expected_sales_file)
    
    # Comparar los DataFrames
    pd.testing.assert_frame_equal(actual_people_df, expected_people_df)
    pd.testing.assert_frame_equal(actual_sales_df, expected_sales_df)