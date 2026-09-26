# CodeAlpha - Exploratory Data Analysis

## Internship Task 2

This project performs Exploratory Data Analysis (EDA) on an Online Retail dataset.

## Objectives

- Understand the structure of the dataset
- Identify missing values
- Detect duplicate records
- Clean the dataset
- Analyze sales statistics
- Find the top-selling products
- Analyze country-wise sales
- Analyze monthly sales trends

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn

## Dataset

Online Retail Sales Dataset.

## Key Analysis

### Data Cleaning
- Removed duplicate records
- Handled missing product descriptions
- Converted invoice dates into datetime format
- Removed invalid quantity values
- Removed invalid unit prices

### Sales Analysis
The project calculates total sales using:

`TotalSales = Quantity × UnitPrice`

### Key Findings

- Total cleaned records: 524,878
- Total revenue: 10,642,110.80
- Top-selling product by quantity: PAPER CRAFT, LITTLE BIRDIE
- Highest-sales country: United Kingdom
- Highest-sales month: November 2011

## Project Structure

CodeAlpha_EDA/
│
├── dataset/
│   └── online_retail.csv
│
├── eda_analysis.py
│
└── README.md

## How to Run

1. Install Python.
2. Install required libraries:

```bash
pip install pandas numpy matplotlib seaborn