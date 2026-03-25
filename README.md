# CSV Statistical Processing System with DevOps CI

## 📌 Project Overview

This project is an Automated Data Science Pipeline that performs complex statistical analysis and data visualization on CSV datasets. It is built as a DevOps Showcase, integrating Continuous Integration (CI) and automated quality gates to ensure data integrity.

The system monitors the input/ folder, detects new datasets, executes a suite of mathematical processors, and generates both tabular reports (CSV) and graphical insights (PNG) in the `output/` folder.

---

## ⚙️ Features

* Smart CSV Detection: Automatically processes any file in the input/ directory.
* Comment Handling: Built-in support for skipping metadata/header comments (e.g., # tags found in basic-data.csv).
* Statistical Suite:

  * Mean, Median, & Std Dev: Core central tendency and dispersion metrics.
  * Statistical Summary: Full descriptive statistics (count, min, max, percentiles).
  * Correlation Analysis: Matrix showing how variables relate to one another.
  * Statistical Summary
  * Correlation Analysis
  * Automated Visualization: Dynamically generates Bar Charts for every processed dataset, identifying numeric columns automatically.
  * DevOps Ready: Integrated GitHub Actions pipeline for automated testing and "Zero-Touch" updates.

---

## 🛠️ Tools and Technologies

* **Python 3.9+** – Core programming logic.
* **Pandas** – Data manipulation and robust CSV parsing.
* **Matplotlib** - Graphical engine for automated visualization.
* **PyTest** – Framework for automated unit testing.
* **Git & GitHub** – Version control
* **GitHub Actions** – CI/CD automation and bot-driven commits.

---

## 📂 Project Structure

```
csv-statistical-devops/
│
├── .github/workflows/
│   └── ci.yml                # GitHub Actions CI Configuration
├── input/                    # Raw Data (e.g., grade.csv, basic-data.csv)
├── output/                   # Auto-generated CSVs and PNG Charts
├── processors/               # Logic Modules
│   ├── _init_.py           # Package exports
│   ├── calculate_column_mean.py
│   ├── calculate_column_median.py
│   ├── calculate_column_std_dev.py
│   ├── generate_statistical_summary.py
│   ├── correlation_analysis.py
│   └── generate_visualizations.py  # Charting engine
│
├── tests/                    # Quality Assurance
│   └── test_processors.py    # Unit tests for all math functions
├── main.py                   # Main Automation Script
├── requirements.txt          # Project dependencies
└── README.md                 # Project Documentation
```

---

## ▶️ How to Run the Project

### 1. Clone & Setup

```
Bash
git clone https://github.com/moonlighttttluna/csv-statistical-devops.git
cd csv-statistical-devops
pip install -r requirements.txt

```

---

### 2. Add Your Data

```
Place any CSV file inside the input/ folder. The system is designed to handle different schemas (different column names) automatically using df.select_dtypes(include='number').
```

---

### 3. Execute Pipeline

```
Bash
python main.py
Look in the output/ folder for your new statistical CSVs and the .png visualization.
```

---

### 4. Run Tests

Bash
export PYTHONPATH=$PYTHONPATH:$(pwd)
pytest -v



---

## 🔄 DevOps Workflow

1. Write code and test locally
2. Commit changes using Git
3. Push to GitHub repository
4. GitHub Actions CI pipeline runs automatically
5. Tests are executed using PyTest
6. Build is marked as success (✔) or failure (❌)

---

## ⚙️ CI Pipeline (GitHub Actions)

The CI pipeline automatically performs:

* Setup Python environment
* Install dependencies
* Run PyTest
* Validate project functionality

A green check mark in GitHub Actions indicates a successful run.

---

## 🧪 Testing Strategy

* Each function has a dedicated test file
* Tests validate correctness of statistical outputs
* PyTest automatically executes all test cases
* Ensures reliability and error detection

---

## 📊 CSV Processing Techniques

* CSV files are read using Pandas
* Data is converted into DataFrames
* Numeric columns are automatically detected using:

  ```
  df.select_dtypes(include=['number'])
  ```
* Statistical computations are applied
* Results are exported as CSV files

---

## 👥 Group Roles

### Data Processing Lead

Designs and implements CSV processing algorithms.

### DevOps Engineer

Configures GitHub Actions CI pipeline and automation.

### Tester

Develops and validates PyTest test cases.

### Documenter / Presenter

Prepares README and presentation materials.

---

## 📈 Example Input

```
Name,Math,Science,English
Melvin,85,75,76
Maddie,90,85,80
Dani,70,88,95
Lisa,80,75,72
```

---

## 📁 Example Output Files

```
mean_grades.csv
median_grades.csv
std_grades.csv
summary_grades.csv
correlation_grades.csv
```

---

## 🎯 DevOps Concepts Applied

* Continuous Integration (CI)
* Automation
* Testing
* Version Control

---

## ✅ Conclusion

This project demonstrates how DevOps practices can be applied to automate data processing systems. By integrating Python, automated testing, and CI pipelines, the system ensures reliability, scalability, and efficiency.

---
