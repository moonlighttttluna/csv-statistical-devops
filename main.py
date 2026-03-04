```python
import os

from processors.calculate_column_mean import calculate_column_mean
from processors.calculate_column_median import calculate_column_median
from processors.calculate_column_std_dev import calculate_column_std_dev
from processors.generate_statistical_summary import generate_statistical_summary
from processors.correlation_analysis import correlation_analysis

INPUT_FOLDER = "input"
OUTPUT_FOLDER = "output"

# Create output folder if it does not exist
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# Check if input folder exists
if not os.path.exists(INPUT_FOLDER):
    print("Input folder not found.")
    exit()

# Process CSV files
for file in os.listdir(INPUT_FOLDER):
    if file.endswith(".csv"):
        file_path = os.path.join(INPUT_FOLDER, file)

        print(f"Processing {file}...")

        mean = calculate_column_mean(file_path)
        median = calculate_column_median(file_path)
        std_dev = calculate_column_std_dev(file_path)
        summary = generate_statistical_summary(file_path)
        correlation = correlation_analysis(file_path)

        mean.to_csv(f"{OUTPUT_FOLDER}/mean_{file}")
        median.to_csv(f"{OUTPUT_FOLDER}/median_{file}")
        std_dev.to_csv(f"{OUTPUT_FOLDER}/std_{file}")
        summary.to_csv(f"{OUTPUT_FOLDER}/summary_{file}")
        correlation.to_csv(f"{OUTPUT_FOLDER}/correlation_{file}")

        print(f"{file} processed successfully.")

print("All CSV files processed.")
```
