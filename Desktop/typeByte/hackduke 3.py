import pandas as pd
# Load the CSV file into a DataFrame
tsv_file_path = "HACKDUKE Article List - Sheet1 (1).tsv"  
df = pd.read_csv(tsv_file_path, sep="\t")


# Define Lexile score ranges for easy, medium, and hard
lexile_ranges = {
    "Easy": (1, 33),
    "Medium": (34, 64),
    "Hard": (65, 100)
}

# Take user input for Lexile score
lexile_score = int(input("Enter your Lexile score (1-100): "))

# Determine the category based on Lexile score
category = None

if lexile_score in range(1,33):
    category = "Easy"
elif lexile_score in range(34,64):
    category = "Medium"
else:
    category = "Hard"

if category:
    # Check if the selected category column exists in the DataFrame
    if category not in df.columns:
        print(f"Error: The '{category}' column does not exist in the CSV file.")
    else:
        # Filter articles based on the selected category
        filtered_articles = df[df[df.columns[1]].notna()]  # Assuming 'df.columns[1]' is the column containing article names

        if not filtered_articles.empty:
            # Display articles in the chosen category
            print(f"Articles in the '{category.capitalize()}' category:")
            print(df)
            for index, row in filtered_articles.iterrows():
                print(f"{row[df.columns[0]]}")
                if(category == "Easy"):
                    print(f"{row[df.columns[1]]}")
                if (category == "Medium"):
                    print(f"{row[df.columns[2]]}")
                if (category == "Hard"):
                    print(f"{row[df.columns[3]]}")
                
        else:
            print(f"No articles found in the '{category.capitalize()}' category.")
else:
    print("Invalid Lexile score. Please enter a score between 1 and 100.")





