from bs4 import BeautifulSoup
import requests
import pandas as pd


url = "https://www.worldometers.info/world-population/population-by-country/"
page = requests.get(url)

soup = BeautifulSoup(page.text,"html")

# Getting the 'Table' id from the website:
table = soup.find("table","table table-striped table-bordered")

# Searching for our th tags and putting them into a list:
world_columns = table.find_all("th")
world_columns_titles = [columns.text for columns in world_columns]


# Placing into a dataframe, with Pandas
df = pd.DataFrame(columns = world_columns_titles)
table.find_all("tr")

world_rows = table.find_all("tr") # <-- row data

for row in world_rows[1:]:
    row_data = row.find_all("td")
    individual_row_data = [data.text for data in row_data]
    
    length = len(df)
    df.loc[length] = individual_row_data
    


# Exporting our file to a CSV:
df.to_csv("/Users/chris/Desktop/Projects/project3/Csv/World_population_Scrapped.csv", index = False)








