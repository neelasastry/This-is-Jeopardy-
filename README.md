# Jeopardy! Data Manipulation Challenge

A data science project exploring a comprehensive history of questions and answers from the game show *Jeopardy!*. This project focuses on text processing, custom filtering engines, and data type coercion using Python and Pandas.

## Key Features & Achievements
* **Data Cleansing:** Used string stripping techniques to permanently eliminate leading whitespaces from messy column names.
* **Monetary Data Coercion:** Stripped formatting symbols (`$` and `,`) from data rows and utilized `pd.to_numeric()` with error coercion to safely transform raw strings into mathematical floats without crashing on 'No Value' Final Jeopardy entries.
* **Robust Text Filtering:** Engineered a case-insensitive multi-word search function leveraging lambda expressions and the strict `all()` iterator engine to identify clean target overlaps.
* **Statistical Insights:** Investigated data connectivity via cross-tabulation (`pd.crosstab`) to establish structural relationships between game rounds and specific clue categories.
