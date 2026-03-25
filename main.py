import os
import pandas as pd
import logging

# Import the different data processing functions that will handle
# the statistical computations for each dataset.
from processors import (
    calculate_column_mean,
    calculate_column_median,
    calculate_column_std_dev,
    generate_statistical_summary,
    correlation_analysis
)

# Import the visualization function separately since it is located
# in another module inside the processors folder.
from processors.generate_visualizations import generate_visualizations

# Define the folders where input CSV files will be placed
# and where the processed results will be saved.
INPUT_FOLDER = "input"
OUTPUT_FOLDER = "output"

# Set up the logging configuration so the program can display
# helpful messages during execution (like progress, warnings, or errors).
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

def main():
    # Make sure the output folder exists.
    # If it doesn't, Python will automatically create it.
    os.makedirs(OUTPUT_FOLDER, exist_ok=True)
    
   # Check if the input folder exists.
    # If it is missing, create it and notify the user.
    if not os.path.exists(INPUT_FOLDER):
        os.makedirs(INPUT_FOLDER)
        logging.warning(f"Created missing folder: {INPUT_FOLDER}")

    # Collect all CSV files from the input folder.
    # This allows the system to process multiple datasets automatically.
    files = [f for f in os.listdir(INPUT_FOLDER) if f.endswith(".csv")]

     # If no CSV files are found, display a warning and stop the program.
    if not files:
        logging.warning(f"No CSV files found in {INPUT_FOLDER}")
        return

    # Loop through each CSV file one by one.
    # This ensures every dataset inside the folder gets processed.
    for file in files:
        file_path = os.path.join(INPUT_FOLDER, file)
        try:
            logging.info(f"Processing: {file}")
            df = pd.read_csv(file_path)

            
            tasks = {
                "mean": calculate_column_mean,
                "median": calculate_column_median,
                "std": calculate_column_std_dev,
                "summary": generate_statistical_summary,
                "correlation": correlation_analysis
            }

            
            for prefix, func in tasks.items():
                result = func(df)
                output_name = f"{prefix}_{file}"
                result.to_csv(os.path.join(OUTPUT_FOLDER, output_name))
            
            
            
            generate_visualizations(df, OUTPUT_FOLDER, file)
            
            logging.info(f"Successfully processed {file} and generated chart.")

        except Exception as e:
            logging.error(f"Error processing {file}: {e}")

if __name__ == "__main__":
    main()
    
