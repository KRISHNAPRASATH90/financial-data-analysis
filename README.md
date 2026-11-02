# Automated Financial Data Analysis and Reporting System

## Project Overview

Developed an automated financial data analysis and reporting system using Python and MySQL. The system extracts financial transaction data from five relational database tables, performs data cleaning and integration, analyses spending patterns, and generates visual reports automatically.

## Technologies Used

- Python
- MySQL
- Pandas
- Matplotlib
- Schedule
- mysql-connector-python

## Key Features

- Extracts data from five MySQL relational tables.
- Performs data cleaning and preprocessing using Pandas.
- Handles missing values and duplicate records.
- Performs data validation and data integration.
- Analyses monthly expenses and category-wise spending.
- Identifies the top 10 merchants based on spending.
- Compares budget allocation with actual expenditure.
- Generates four visual reports using Matplotlib.
- Saves generated charts as PNG files.
- Automates scheduled report generation using Python Schedule.

## Analysis Performed

1. Monthly Expense Analysis
2. Category-wise Spending Analysis
3. Top 10 Merchants Analysis
4. Budget vs Actual Expenditure Analysis

## Project Structure

```text
financial-data-analysis/
│
├── src/
│   └── finance_data.py
│
├── sql/
│   └── finance_dashboard_raw_data.sql
│
├── reports/
│
├── README.md
├── requirements.txt
└── .gitignore
```

## Installation and Execution

### 1. Clone the Repository

```bash
git clone https://github.com/KRISHNAPRASATH90/financial-data-analysis.git
cd financial-data-analysis
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure MySQL

- Install and start MySQL.
- Create the required database.
- Execute the SQL script.
- Configure database connection details in the Python application.

### 4. Run the Application

```bash
python src/finance_data.py
```

## Output

The system generates four Matplotlib visual reports and saves them as PNG files in the reports directory.

## Learning Outcomes

- Python-based data analysis
- SQL database connectivity
- Data cleaning and preprocessing
- Financial data analysis
- Data visualization
- Automated reporting

## Author

Krishna Prasath DS