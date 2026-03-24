import os
import pandas as pd
from processors.calculate_column_mean import calculate_column_mean
from processors.calculate_column_median import calculate_column_median
from processors.calculate_column_std_dev import calculate_column_std_dev
from processors.generate_statistical_summary import generate_statistical_summary
from processors.correlation_analysis import correlation_analysis

INPUT_FOLDER = "input"
OUTPUT_FOLDER = "output"

# Create output folder if it does not exist
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# Loop through all CSV files in input folder
for file in os.listdir(INPUT_FOLDER):
    if file.endswith(".csv"):
        file_path = os.path.join(INPUT_FOLDER, file)

        # Read CSV into DataFrame
        df = pd.read_csv(file_path)

        # Pass DataFrame to processor functions
        mean = calculate_column_mean(df)
        median = calculate_column_median(df)
        std_dev = calculate_column_std_dev(df)
        summary = generate_statistical_summary(df)
        correlation = correlation_analysis(df)

        # Save results to output folder
        mean.to_csv(os.path.join(OUTPUT_FOLDER, f"mean_{file}"), index=False)
        median.to_csv(os.path.join(OUTPUT_FOLDER, f"median_{file}"), index=False)
        std_dev.to_csv(os.path.join(OUTPUT_FOLDER, f"std_{file}"), index=False)
        summary.to_csv(os.path.join(OUTPUT_FOLDER, f"summary_{file}"), index=False)
        correlation.to_csv(os.path.join(OUTPUT_FOLDER, f"correlation_{file}"), index=False)

print("CSV files processed successfully.")
