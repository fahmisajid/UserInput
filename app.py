import pandas as pd
import streamlit as st

import pickle 

# Clone the GitHub repository
repo_url = 'https://github.com/fahmisajid/UserInput.git'
local_path = 'UserInput'
Repo.clone_from(repo_url, local_path)

# Specify the CSV file path
csv_file_path = '/path/to/local/repository/UserInput.csv'

df = pd.read_csv(path)

sentence = st.text_input('Masukkan Kalimat:') 

user_input = {'Questions':sentence, 'Answers': 'idk', 'Response_Type':'bot'}
df_input = pd.DataFrame(user_input, index=[0])

df_merge = pd.concat([df, df_input], ignore_index=True)

st.write(df)

# Write the updated DataFrame back to the CSV file
df_merge.to_csv(csv_file_path, index=False)

# Commit and push the changes back to the GitHub repository
repo = Repo(local_path)
repo.git.add(csv_file_path)
repo.index.commit('Added user input to UserInput.csv')
origin = repo.remote('origin')
origin.push()
