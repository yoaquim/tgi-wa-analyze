import streamlit as st
import altair as alt
import pandas as pd

with open("chat.txt", "r", encoding='utf-8') as in_file:
    lines = in_file.readlines()


def word_counter(word: str):
    d = 0
    for line in lines:
        if word.lower() in line.lower():
            d += 1
    return d


terms = ['tu mai', 'bicho', 'sylvia', 'maritza', 'cabron']
counts = [word_counter(term.lower()) for term in terms if True]

source = pd.DataFrame({
    'Count': counts,
    'Term': terms
})

bar_chart = alt.Chart(source).mark_bar().encode(
    y='Count',
    x='Term:O',
    # y='Price ($):Q',
    # x='Month:O',
)

st.title("")
st.markdown(
    """
    # 🕹️ The Gaming Initiative 🕹️
    ### What'sApp Data
    """
)
st.altair_chart(bar_chart, use_container_width=True)
