# CSV Statistical Processing System with DevOps CI

## 📌 Project Overview

This project is an automated CSV processing system that performs statistical analysis on datasets using Python. It integrates DevOps practices such as Continuous Integration (CI), automated testing, and version control.

The system reads CSV files from the `input` folder, processes them using statistical functions, and generates output files automatically in the `output` folder.

---

## ⚙️ Features

* Automatic detection of CSV files
* Statistical computations:

  * Mean
  * Median
  * Standard Deviation
  * Statistical Summary
  * Correlation Analysis
* Automated testing using PyTest
* Continuous Integration using GitHub Actions
* Organized project structure for scalability

---

## 🛠️ Tools and Technologies

* **Python 3** – Main programming language
* **Pandas** – Data processing and CSV handling
* **NumPy** – Numerical computations
* **PyTest** – Automated testing framework
* **Git & GitHub** – Version control
* **GitHub Actions** – CI pipeline automation

---

## 📂 Project Structure

```
project/
│
├── input/                     # Contains input CSV files
├── output/                    # Stores generated output files
├── processors/                # Statistical processing functions
│   ├── calculate_column_mean.py
│   ├── calculate_column_median.py
│   ├── calculate_column_std_dev.py
│   ├── generate_statistical_summary.py
│   └── correlation_analysis.py
│
├── tests/                     # PyTest test files
│   ├── test_mean.py
│   ├── test_median.py
│   ├── test_std_dev.py
│   ├── test_summary.py
│   └── test_correlation.py
│
├── main.py                   # Main automation script
├── requirements.txt          # Dependencies
├── pytest.ini                # PyTest configuration
└── .github/workflows/ci.yml  # CI pipeline configuration
```

---

## ▶️ How to Run the Project

### 1. Clone the Repository

```
git clone https://github.com/moonlighttttluna/csv-statistical-devops.git
cd csv-statistical-devops
```

---

### 2. Create Virtual Environment

```
python -m venv venv
venv\Scripts\activate
```

---

### 3. Install Dependencies

```
pip install -r requirements.txt
```

---

### 4. Add CSV File

Place your CSV file inside the `input` folder.

Example:

```
input/grades.csv
```

---

### 5. Run the Program

```
python main.py
```

Output will be generated in the `output` folder.

---

### 6. Run Tests

```
pytest -v
```

Expected output:

```
5 passed
```

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
  df.select_dtypes(include='number')
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
