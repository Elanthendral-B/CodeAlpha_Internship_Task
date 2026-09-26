# CodeAlpha Data Analysis 

A comprehensive collection of Python scripts for data analysis, visualization, sentiment analysis, and web scraping. This project demonstrates practical applications of data science techniques on real-world datasets.

---

## 📋 Project Overview

This repository contains four interconnected tasks that showcase end-to-end data analysis workflows:

1. **Exploratory Data Analysis (EDA)** - Understanding dataset structure and patterns
2. **Data Visualization** - Creating insightful charts and graphs
3. **Sentiment Analysis** - Analyzing product descriptions using NLP
4. **Web Scraping** - Extracting data from websites

---

## 📁 Project Structure

```
.
├── data_visualization.py      # Sales trends and product analysis charts
├── eda_analysis.py            # Dataset exploration and cleaning
├── sentiment_analysis.py      # NLP-based sentiment classification
├── web_scraping.py            # Web scraping with BeautifulSoup
├── dataset/
│   └── online_retail.csv      # Main retail dataset
├── cleaned_online_retail.csv  # Pre-processed data
├── output/                    # Generated visualizations
└── README.md                  # This file
```

---

## 🚀 Quick Start

### Prerequisites

Make sure you have Python 3.7+ installed. Install required packages:

```bash
pip install pandas matplotlib seaborn requests beautifulsoup4 vaderSentiment
```

### Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/data-analysis-project.git
cd data-analysis-project
```

2. Create a virtual environment (optional but recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

---

## 📊 Scripts Overview

### 1. **eda_analysis.py** - Exploratory Data Analysis

Performs initial data exploration and cleaning on the online retail dataset.

**What it does:**
- Loads the online retail CSV dataset
- Displays dataset information (rows, columns, data types)
- Identifies and handles missing values
- Removes duplicate entries
- Filters invalid data (negative quantities/prices)
- Generates summary statistics
- Analyzes top-selling products
- Calculates country-wise sales

**How to run:**
```bash
python eda_analysis.py
```

**Expected Output:**
- Dataset shape and info
- Missing values report
- Sales statistics (mean, median, std dev, etc.)
- Top 10 best-selling products
- Top 10 countries by revenue
- Monthly sales breakdown

---

### 2. **data_visualization.py** - Data Visualization

Creates professional visualizations from cleaned retail data.

**What it does:**
- Loads and cleans the dataset
- Generates **Monthly Sales Trend** line chart
- Creates **Top 10 Best-Selling Products** bar chart
- Plots **Top 10 Countries by Sales** visualization
- Saves all charts as PNG files

**How to run:**
```bash
python data_visualization.py
```

**Output files:**
- `output/monthly_sales_trend.png`
- `output/top_10_products.png`


---

### 3. **sentiment_analysis.py** - Sentiment Analysis

Analyzes sentiment in product descriptions using VADER sentiment analysis.

**What it does:**
- Loads cleaned retail dataset
- Applies VADER sentiment analyzer to product descriptions
- Classifies sentiments as: Positive, Neutral, or Negative
- Calculates sentiment scores (-1 to +1)
- Generates visualizations:
  - Bar chart: Sentiment distribution
  - Pie chart: Sentiment percentages
  - Histogram: Sentiment score distribution
- Saves results to CSV

**How to run:**
```bash
python sentiment_analysis.py
```

**Output files:**
- `sentiment_analysis_results.csv` - Dataset with sentiment labels
- `sentiment_distribution.png` - Bar chart
- `sentiment_percentage.png` - Pie chart
- `sentiment_score_distribution.png` - Histogram

---

### 4. **web_scraping.py** - Web Scraping

Scrapes book data from an online bookstore using web scraping techniques.

**What it does:**
- Connects to books.toscrape.com
- Extracts book information:
  - Title
  - Price
  - Availability status
- Stores data in a pandas DataFrame
- Exports data to CSV

**How to run:**
```bash
python web_scraping.py
```

**Output:**
- `books_data.csv` - Scraped book data with 3 columns

---

## 📦 Dependencies

| Package | Purpose |
|---------|---------|
| `pandas`         | Data manipulation and analysis |
| `matplotlib`     | Plotting and visualization |
| `seaborn`        | Statistical data visualization |
| `requests`       | HTTP requests for web scraping |
| `beautifulsoup4` | HTML/XML parsing |
| `vaderSentiment` | Sentiment analysis |

---

---

## 📈 Workflow & Data Flow

```
Raw Dataset (online_retail.csv)
      ↓
[web_scraping.py] → books_data.csv
      ↓
[eda_analysis.py] → Cleaned Data & Statistics
      ↓
[data_visualization.py] → Charts & Graphs (output/)
      ↓
[sentiment_analysis.py] → Sentiment Scores & Visualizations
```

---

## 💡 Key Features

✅ **Comprehensive EDA** - Full data exploration workflow
✅ **Professional Visualizations** - Publication-ready charts
✅ **NLP Integration** - Sentiment analysis using VADER
✅ **Web Scraping** - Ethical data collection techniques
✅ **Data Cleaning** - Robust handling of missing/invalid data
✅ **CSV Export** - Easy data sharing and further analysis
✅ **Clear Documentation** - Well-commented code

---




**Last Updated:** September 2026
**Status:** Complete ✅
