import os
import logging
from src.extractions import read_json, read_csv
from src.transformations import (
    title_dataframe, 
    combine_name_and_surname, 
    generate_unique_id, 
    add_id_to_sales, 
    delete_columns,
    move_column_to_front
)

# Configuración del logger
def setup_logger():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        handlers=[logging.StreamHandler()],
    )
    return logging.getLogger(__name__)

logger = setup_logger()

def main():
    """
    Main function to execute the ETL-like pipeline for the project.
    """
    logger.info("Starting the ETL pipeline...")
    
    # Paths to the data
    data_dir = os.path.join(os.path.dirname(__file__), "..", "data")
    people_file = os.path.join(data_dir, "people.json")
    sales_file = os.path.join(data_dir, "sales.csv")
    
    # Extraction
    logger.info("Extracting data...")
    try:
        people_df = read_json(people_file)
        sales_df = read_csv(sales_file)

    except FileNotFoundError as e:
        logger.error("Error extracting data: %s", e)
        return None, None
    
    # Transformations
    try:
        logger.info("Transforming data...")
        
        # 1. Title case for names
        people_df = title_dataframe(people_df, ["first_name", "last_name"])
        sales_df = title_dataframe(sales_df, ["seller"])
        
        # 2. Combine first_name and last_name into full_name
        people_df = combine_name_and_surname(people_df, "first_name", "last_name", "full_name")
        
        # 3. Generate unique IDs for people
        people_df = generate_unique_id(people_df, "person_id")
        sales_df = generate_unique_id(sales_df, "sales_id")

        # # 4. Add IDs to sales based on seller names
        sales_df = add_id_to_sales(sales_df, people_df, "seller", "full_name", "person_id")
        
        # # 5. Delete the seller column from sales
        sales_df = delete_columns(sales_df, ["seller", "full_name"])
        people_df = delete_columns(people_df, ["full_name"])

        # # 6. Moves id columns to front
        people_df = move_column_to_front(people_df, "person_id")
        sales_df = move_column_to_front(sales_df, "sales_id")

    except Exception as e:
        logger.error("Error during transformation: %s", e)
        return None, None


    # # Log final results
    logger.info("ETL pipeline completed. Final transformed data:")
    logger.info("\n\nPeople DataFrame:\n%s", people_df)
    logger.info("\n\nSales DataFrame:\n%s", sales_df)

    return people_df, sales_df

if __name__ == "__main__":
    main()