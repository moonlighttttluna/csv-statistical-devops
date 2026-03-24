import os
import pandas as pd

from processors.calculate_column_mean import calculate_column_mean
from processors.calculate_column_median import calculate_column_median
from processors.calculate_column_std_dev import calculate_column_std_dev
from processors.generate_statistical_summary import generate_statistical_summary
from processors.correlation_analysis import correlation_analysis

INPUT_FOLDER = "input"
OUTPUT_FOLDER = "output"


def process_csv(file_path):
    df = pd.read_csv(csv_file)
    name, _ = os.path.splitext(filename)

    df = pd.read_csv(file_path)

    # Apply functions
    mean = calculate_column_mean(df)
    median = calculate_column_median(df)
    std_dev = calculate_column_std_dev(df)
    summary = generate_statistical_summary(df)
    correlation = correlation_analysis(df)

    # Save output
    output_file = os.path.join(OUTPUT_FOLDER, f"{name}_results.txt")

    with open(output_file, "w") as f:
        f.write("=== MEAN ===\n")
        f.write(str(mean) + "\n\n")

        f.write("=== MEDIAN ===\n")
        f.write(str(median) + "\n\n")

        f.write("=== STD DEV ===\n")
        f.write(str(std_dev) + "\n\n")

        f.write("=== SUMMARY ===\n")
        f.write(str(summary) + "\n\n")

        f.write("=== CORRELATION ===\n")
        f.write(str(correlation) + "\n\n")

    print(f"Processed: {filename}")


def main():
    if not os.path.exists(OUTPUT_FOLDER):
        os.makedirs(OUTPUT_FOLDER)

    for file in os.listdir(INPUT_FOLDER):
        if file.endswith(".csv"):
            process_csv(os.path.join(INPUT_FOLDER, file))


if __name__ == "__main__":
    main()
