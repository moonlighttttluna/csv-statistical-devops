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
```
Bash
export PYTHONPATH=$PYTHONPATH:$(pwd)
pytest -v
```


---

## 🔄 DevOps Workflow (CI/CD)

1. Local Dev: Write code or add data locally.
2. Push: Commit changes to GitHub.
3. CI Trigger: GitHub Actions starts an Ubuntu runner.
4. Test Phase: Pytest validates that the math logic (Mean, Median, etc.) is still 100% accurate.
5. Process Phase: main.py runs, generating the stats and charts.
6. Deploy: The GitHub Action Bot automatically commits the new output/ files back to your repository.

---

## 🧪 Testing Strategy

We utilize a Modular Testing Strategy. Each statistical function is isolated and tested against "Known Good" data. If a function is modified and the math becomes incorrect, the CI Pipeline will fail (❌) and block the update to the output folder, protecting the integrity of your data.


---

## 📈 Example Visualization

The system automatically identifies the best "Label" column (like Name or ID) and creates charts for all numeric columns:

---

## 🎯 DevOps Concepts Applied

* Continuous Integration (CI): Automated testing on every push.
* Infrastructure as Code (IaC): Using YAML to define the build environment.
* Automated Visualization: Removing the manual step of creating reports.



---

## ✅Developed by the CSV Statistical DevOps Team

---
