# Task 2: Data Cleaning and Exploratory Data Analysis (EDA) on Titanic Dataset

## Objective:
This task involves performing data cleaning and exploratory data analysis (EDA) on the Titanic dataset to explore relationships between variables and identify patterns and trends in the data.

## Data Cleaning Steps:
1. **Age**: Missing values in the 'Age' column were filled with the median.
2. **Cabin**: The 'Cabin' column was dropped due to excessive missing values.
3. **Duplicates**: Duplicate entries were removed to ensure data quality.

## Exploratory Data Analysis (EDA):
### 1. Survival Count:
A bar chart displaying the count of survivors versus non-survivors.

### 2. Age Distribution:
A histogram showing the distribution of passenger ages with a KDE line for smoother visualization.

### 3. Survival Count by Gender:
A count plot illustrating survival distribution based on gender.

### 4. Survival Rate by Class:
A bar plot highlighting the survival rate across different passenger classes (1st, 2nd, and 3rd class).

### 5. Age vs. Fare with Survival Status:
A scatter plot displaying the relationship between age and fare, with survival status as a hue to identify trends.

## How to Run:
1. Download the Titanic dataset from Kaggle or use the provided CSV file.
2. Ensure all required libraries (`pandas`, `matplotlib`, `seaborn`) are installed.
3. Run the script `task2_EDA_Titanic.py` to generate visualizations.

## Insights:
- There are more non-survivors than survivors.
- Age distribution is mostly centered between 20-40 years.
- Females had a higher survival rate than males.
- Higher class passengers had better survival chances.
- Fare and Age don't seem to have a strong correlation with survival, but higher fares were associated with higher class passengers.
