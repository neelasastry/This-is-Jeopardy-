import pandas as pd
pd.set_option('display.max_colwidth', -1)
pd.set_option('display.max_colwidth', 10000)

#task 2
#Loading the CSV file and using .strip() to strip off additional white spaces from the columns.
jeopardy_data = pd.read_csv('jeopardy.csv')
jeopardy_data.columns = jeopardy_data.columns.str.strip()
print(jeopardy_data.columns)


# Task 3: Reusable function to filter Jeopardy questions.
# Task 4: Upgrading the function for real-world text variations using .lower()
def filter_data(words):
    return jeopardy_data[jeopardy_data["Question"].apply(lambda q: all([word.lower() in q.lower() for word in words]))]
filtered_df = filter_data(["King", "England"])   
print(filtered_df["Question"])

#task 5
#Convert value column to floats by taking off special characters
# Clean the strings
cleaned_value = jeopardy_data["Value"].str.replace("$", "").str.replace(",", "")

# Convert to float numbers safely
jeopardy_data["Float Value"] = pd.to_numeric(cleaned_value, errors='coerce')

# Print out the first few rows of your new column to check your handiwork!
print(jeopardy_data["Float Value"].head())

#task 6
#a function that returns the count of the unique answers to all of the questions in a dataset.
def unique_answers(data):
    return data["Answer"].value_counts()
print(unique_answers(filtered_df))
# Step 1: Filter the dataset for rows containing the word "King"
king_df = filter_data(["King"])

# Step 2: Grab the "Float Value" column from those rows and find the average
average_king_value = king_df["Float Value"].mean()

# Step 3: Print it out to see the result!
print(f"The average king value is {average_king_value}")

#task 7 - A
# Create a dataset of just 90s questions
data_90s = jeopardy_data[jeopardy_data["Air Date"].str.contains("199")]

# Create a dataset of just 2000s questions
data_2000s = jeopardy_data[jeopardy_data["Air Date"].str.contains("200")]

# Count how many 90s questions contain "Computer"
computer_90s_count = data_90s["Question"].str.contains("Computer", case=False).sum()

# Count how many 2000s questions contain "Computer"
computer_2000s_count = data_2000s["Question"].str.contains("Computer", case=False).sum()

print(f"Computer questions in the 90s: {computer_90s_count}")
print(f"Computer questions in the 2000s:{computer_2000s_count}")

#task 7 - B
# 1. Filter the dataset for just Literature categories
# Create a full connectivity table between Round and Category
round_category_crosstab = pd.crosstab(jeopardy_data["Category"], jeopardy_data["Round"])

# Look at a few rows to see the connectivity
print(round_category_crosstab.head(10))
