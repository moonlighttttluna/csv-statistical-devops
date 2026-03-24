import os
import pandas as pd
import logging
from processors import (
    calculate_column_mean,
    calculate_column_median,
    calculate_column_std_dev,
    generate_statistical_summary,
    correlation_analysis
)
# 1. Import the new visualization processor
from processors.generate_visualizations import generate_visualizations

INPUT_FOLDER = "input"
OUTPUT_FOLDER = "output"
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

def main():
    os.makedirs(OUTPUT_FOLDER, exist_ok=True)
    
    # Ensure the input folder exists to avoid errors
    if not os.path.exists(INPUT_FOLDER):
        os.makedirs(INPUT_FOLDER)
        logging.warning(f"Created missing folder: {INPUT_FOLDER}")
    
    files = [f for f in os.listdir(INPUT_FOLDER) if f.endswith(".csv")]
    
    if not files:
        logging.warning(f"No CSV files found in {INPUT_FOLDER}")
        return

    for file in files:
        file_path = os.path.join(INPUT_FOLDER, file)
        try:
            logging.info(f"Processing: {file}")
            df = pd.read_csv(file_path)

            # Map operations to their functions
            tasks = {
                "mean": calculate_column_mean,
                "median": calculate_column_median,
                "std": calculate_column_std_dev,
                "summary": generate_statistical_summary,
                "correlation": correlation_analysis
            }

            # Run all statistical tasks
            for prefix, func in tasks.items():
                result = func(df)
                output_name = f"{prefix}_{file}"
                result.to_csv(os.path.join(OUTPUT_FOLDER, output_name))
            
            # 2. Run the Visualization task
            # We pass 'file' so the PNG name matches the CSV name
            generate_visualizations(df, OUTPUT_FOLDER, file)
            
            logging.info(f"Successfully processed {file} and generated chart.")

        except Exception as e:
            logging.error(f"Error processing {file}: {e}")

if __name__ == "__main__":
    main()
    
