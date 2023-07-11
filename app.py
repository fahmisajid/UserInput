import pandas as pd
import streamlit as st

df = pd.read_csv('User_input.csv')

sentence = st.text_input('Masukkan Kalimat:')

user_input = {'Questions': sentence, 'Answers': 'idk', 'Response_Type': 'bot'}
df_input = pd.DataFrame(user_input, index=[0])

df_merge = pd.concat([df, df_input], ignore_index=True)

st.write(df)

df_merge.to_csv('User_input.csv', index=False)
