import pandas as pd
import streamlit as st
import urllib.request

# Define the file paths
# csv_url = 'https://github.com/fahmisajid/UserInput/blob/main/User_input.csv'
csv_file_path = 'User_input.csv'

# Download the CSV file from GitHub
# urllib.request.urlretrieve(csv_url, csv_file_path)

# Read the CSV file into a DataFrame
df = pd.read_csv("User_input.csv")

# Get user input
sentence = st.text_input('Masukkan Kalimat:') 

# Create a dictionary with the user input
user_input = {'Questions': sentence, 'Answers': 'idk', 'Response_Type': 'bot'}

# Create a DataFrame from the user input dictionary
df_input = pd.DataFrame(user_input, index=[0])

# Concatenate the original DataFrame with the new input DataFrame
df_merge = pd.concat([df, df_input], ignore_index=True)

# Display the updated DataFrame in the Streamlit app
st.write(df)

# Write the updated DataFrame back to the CSV file
df_merge.to_csv(csv_file_path, index=False)
