import pandas as pd
import streamlit as st

@st.cache_data(ttl=600)
def load_data(sheets_url):
    csv_url = sheets_url.replace("/edit#gid=", "/export?format=csv&gid=")
    return pd.read_csv(csv_url)

df = load_data(st.secrets["public_gsheets_url"])

# df = pd.read_csv('User_input.csv')

sentence = st.text_input('Masukkan Kalimat:') 

user_input = {'Questions':sentence, 'Answers': 'idk', 'Response_Type':'bot'}
df_input = pd.DataFrame(user_input, index=[0])

df_merge = pd.concat([df, df_input], ignore_index=True)

st.write(df_merge)

# Save the merged DataFrame back to Excel
df_merge.to_csv('User_input.csv', index=False)
