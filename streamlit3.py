import streamlit as st
import datetime

st.set_page_config(page_title="New App", layout="wide")
st.write("hi")

email = st.text_input("Enter mail")
if not email:
    st.warning("Please enter your email address")
    st.stop()
st.success("Go Ahead")


form = st.form("Basic Form")

name = form.text_input("Name")
age = form.slider("Age", min_value=18, max_value=100, step=1)
date = form.date_input("Date", value=datetime.date(2023, 4, 13))
submitted = form.form_submit_button("Submit")

if submitted:
    st.write(name, age, date)


def summ(a, b):
    return a + b


with st.echo():

    def mult(a, b):
        return a * b

    a = 10
    b = 20
    su = summ(a, b)
    mu = mult(a, b)
    st.write(su, mu)

st.write("This is outside")

st.help(datetime)
