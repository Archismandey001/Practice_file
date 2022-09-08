import streamlit as st
import plotly.express as px
import pandas as pd
import seaborn as sns
import datetime
import numpy as np

st.header("Hi, this is streamlit")

st.write(10)

st.markdown('Hi, there')

st.subheader("The next thing will litt you up")

st.text('life is like ML')

df = sns.load_dataset('tips')
st.dataframe(df)
st.table(df)

st.bar_chart(data=df,x='sex',y='total_bill')

st.button('my_first_button ')

if st.dataframe(df):
    st.table(df)

else :
    arr = np.random.normal(1,1, size = 100)
    fig, ax = plt.subplot()
    ax.hist(arr, bins = 20)

    st.pyplot(fig)
@st.cache
def convert_df(df):
    return df.to_csv().encode('utf-8')
v=convert_df(df)

st.download_button(label='download_button', data = v, file_name = 'tips_dat')

#radio button
genre = st.radio(
     "What's your favorite car",
     ('sedan', 'suv', 'hatchback'))

if genre == 'sedan':
     st.write('You selected sedan.')
elif genre == 'suv':
    st.write('You selected suv.')
elif  genre == 'hatchback':
    st.write('You selected hatchback.')
else:
     st.write("You didn't select anything.")

#checkbox
agree = st.checkbox('I agree')

if agree:
     st.write('Its Great that you have agreed, congratulations!')


Title = st.text_input('Movie title', 'Life of Brian')
st.write('The current movie title is', Title)
st.title(Title)

birth_day = st.date_input(
     "When's your birthday",
     datetime.date(2019, 7, 6))
st.write('Your birthday is:', birth_day)

t = st.time_input('Set an alarm for', datetime.time(8, 45))
st.write('Alarm is set for', t)








