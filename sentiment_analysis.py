# ============================================================
# CODEALPHA - TASK 4
# SENTIMENT ANALYSIS
# ============================================================

import pandas as pd
import re
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


# ============================================================
# 1. LOAD CLEANED DATASET
# ============================================================

df = pd.read_csv("cleaned_online_retail.csv")

print("Cleaned dataset loaded successfully!")
print("Dataset shape:", df.shape)


# ============================================================
# 2. INITIALIZE SENTIMENT ANALYZER
# ============================================================

analyzer = SentimentIntensityAnalyzer()


# ============================================================
# 3. SENTIMENT ANALYSIS FUNCTION
# ============================================================

def get_sentiment(text):

    score = analyzer.polarity_scores(str(text))

    compound = score["compound"]

    if compound >= 0.05:
        return "Positive"

    elif compound <= -0.05:
        return "Negative"

    else:
        return "Neutral"


# ============================================================
# 4. APPLY SENTIMENT ANALYSIS
# ============================================================

print("\nAnalyzing sentiment...")

df["Sentiment"] = df["Clean_Description"].apply(get_sentiment)


# ============================================================
# 5. CALCULATE SENTIMENT SCORE
# ============================================================

df["Sentiment_Score"] = df["Clean_Description"].apply(
    lambda text: analyzer.polarity_scores(str(text))["compound"]
)


# ============================================================
# 6. DISPLAY RESULTS
# ============================================================

print("\nSentiment Analysis Results:")
print(df[[
    "Description",
    "Sentiment",
    "Sentiment_Score"
]].head(20))


# ============================================================
# 7. SENTIMENT COUNT
# ============================================================

print("\nSentiment Distribution:")
print(df["Sentiment"].value_counts())


# ============================================================
# 8. SENTIMENT PERCENTAGE
# ============================================================

sentiment_percentage = (
    df["Sentiment"]
    .value_counts(normalize=True)
    .mul(100)
    .round(2)
)

print("\nSentiment Percentage:")
print(sentiment_percentage)


# ============================================================
# 9. SAVE FINAL DATASET
# ============================================================

df.to_csv("sentiment_analysis_results.csv", index=False)

print("\nSentiment analysis completed successfully!")

print("Results saved as:")
print("sentiment_analysis_results.csv")
# ============================================================
# 10. DATA VISUALIZATION
# ============================================================

import matplotlib.pyplot as plt
import seaborn as sns


# ============================================================
# BAR CHART - SENTIMENT DISTRIBUTION
# ============================================================

sentiment_counts = df["Sentiment"].value_counts()

plt.figure(figsize=(8, 5))

sns.barplot(
    x=sentiment_counts.index,
    y=sentiment_counts.values
)

plt.title("Sentiment Distribution")
plt.xlabel("Sentiment")
plt.ylabel("Number of Products")

plt.tight_layout()
plt.savefig("sentiment_distribution.png", dpi=300)

plt.show()


# ============================================================
# PIE CHART - SENTIMENT PERCENTAGE
# ============================================================

plt.figure(figsize=(7, 7))

plt.pie(
    sentiment_counts.values,
    labels=sentiment_counts.index,
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Sentiment Percentage Distribution")

plt.tight_layout()
plt.savefig("sentiment_percentage.png", dpi=300)

plt.show()


# ============================================================
# HISTOGRAM - SENTIMENT SCORE
# ============================================================

plt.figure(figsize=(8, 5))

plt.hist(
    df["Sentiment_Score"],
    bins=30
)

plt.title("Distribution of Sentiment Scores")
plt.xlabel("Sentiment Score")
plt.ylabel("Frequency")

plt.tight_layout()
plt.savefig("sentiment_score_distribution.png", dpi=300)

plt.show()


print("\nAll visualizations created successfully!")
