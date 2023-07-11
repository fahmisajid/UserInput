import pandas as pd
import streamlit as st

@st.cache(allow_output_mutation=True)
def read_csv_file(file_path):
    return pd.read_csv(file_path)

@st.cache(allow_output_mutation=True)
def write_csv_file(df, file_path):
    df.to_csv(file_path, index=False)

file_path = 'User_input.csv'

df = read_csv_file(file_path)

sentence = st.text_input('Masukkan Kalimat:')

user_input = {'Questions': sentence, 'Answers': 'idk', 'Response_Type': 'bot'}
df_input = pd.DataFrame(user_input, index=[0])

df_merge = pd.concat([df, df_input], ignore_index=True)

st.write(df_merge)

write_csv_file(df_merge, file_path)
