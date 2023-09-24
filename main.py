# INF601 - Advanced Programming in Python
# Clayton Allen
# Mini Project 2


# This project makes use of PANDAS data frames to show total death counts for Kansans from Janurary 2015 to March 2023. The data is represented in tabular data pulled from a spreadsheet which is then transformed to graphs that are saved to a folder called 'charts'. Charts is created relative to where the script was run from if it doesn't exist.

# Grading criteria copied from blackboard. 


'''
    (5/5 points) Initial comments with your name, class and project at the top of your .py file.

    (5/5 points) Proper import of packages used.
    
    (20/20 points) Using a data source of your choice, such as data from data.gov or using the Faker package, generate or retrieve some data for creating basic statistics on. This will generally come in as json data, etc.
        Think of some question you would like to solve such as:
        "How many homes in the US have access to 100Mbps Internet or more?"
        "How many movies that Ridley Scott directed is on Netflix?" - https://www.kaggle.com/datasets/shivamb/netflix-shows
        Here are some other great datasets: https://www.kaggle.com/datasets
    (10/10 points) Store this information in Pandas dataframe. These should be 2D data as a dataframe, meaning the data is labeled tabular data.
    (10/10 points) Using matplotlib, graph this data in a way that will visually represent the data. Really try to build some fancy charts here as it will greatly help you in future homework assignments and in the final project.
    (10/10 points) Save these graphs in a folder called charts as PNG files. Do not upload these to your project folder, the project should save these when it executes. You may want to add this folder to your .gitignore file.
    (10/10 points) There should be a minimum of 5 commits on your project, be sure to commit often!
    (10/10 points) I will be checking out the master branch of your project. Please be sure to include a requirements.txt file which contains all the packages that need installed. You can create this fille with the output of pip freeze at the terminal prompt.
    (20/20 points) There should be a README.md file in your project that explains what your project is, how to install the pip requirements, and how to execute the program. Please use the GitHub flavor of Markdown. Be thorough on the explanations.
'''

# INF601 - Advanced Programming in Python
# Clayton Allen
# Mini Project 2

import pandas as pd
import matplotlib.pyplot as plt
import os

# Check if the "charts" directory exists. If not, create it.
output_directory = 'charts'
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Function to import your chosen dataset into a Pandas DataFrame
def import_data(csv_file):
    data = pd.read_csv(csv_file)
    return data

# Load your dataset
csv_file = 'VSRR_Provisional_Drug_Overdose_Death_Counts.csv'
data = import_data(csv_file)

# Filter data for Kansas and select relevant columns
kansas_data_new = data[(data['State'] == 'KS') & (data['Indicator'].str.startswith('Number of Drug Overdose Deaths'))].copy()

# Remove commas from the 'Data Value' column and convert to integers
kansas_data_new['Data Value'] = kansas_data_new['Data Value'].str.replace(',', '').astype(int)

# Group the data by year and sum the death counts
yearly_totals = kansas_data_new.groupby('Year')['Data Value'].sum().reset_index()

# Plotting the data
plt.figure(figsize=(10, 10))
plt.scatter(yearly_totals['Year'], yearly_totals['Data Value'], label='Kansan Overdose Deaths')
for i, row in yearly_totals.iterrows():
    plt.annotate(str(int(row['Data Value'])), (row['Year'], row['Data Value']), textcoords="offset points", xytext=(0,10), ha='center')
plt.xlabel('Year')
plt.ylabel('Total Deaths')
plt.title('Total Overdose Deaths for Kansans (Jan 2015 - Mar 2023)')
plt.legend(['Kansan Overdose Deaths'], loc='upper left', bbox_to_anchor=(1, 1))

# Save the plot as a PNG file
output_filename = os.path.join(output_directory, 'kansas_overdose_death_counts.png')
plt.savefig(output_filename, bbox_inches='tight')  # Use bbox_inches='tight' to ensure the legend is not cut off

# Show the plot (optional)
plt.show()