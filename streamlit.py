import json
import time

import numpy as np
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
from datetime import time


st.text("This is the Test")

st.write("This is **just** a test **_Mani Krishna_**")

df = pd.read_csv(
    r"/Users/manikrishnamandepudi/Desktop/AmygdaProjects/experimentation/notebooks/develop/angeltrain_poc/class_156/mani/data/car_15647352.csv"
)

st.write(df.head())

dc = {"a": 10, "b": 20, "c": 30}
st.write(dc)

fig, ax = plt.subplots()
ax.scatter(np.arange(5), np.arange(5) ** 2)
st.write(fig)

st.write(st.error)

df
dc


code = """def  main():
print("Hello World!")"""

st.code(code, language="python")

df = pd.DataFrame(np.random.randn(50, 20), columns=["cols" + str(i) for i in range(20)])

st.write(df)

st.dataframe(df, width=200, height=900)
st.dataframe(np.random.randn(50, 20))

st.table(df)

st.metric("TCS stock", value="3220.70", delta="19.10", delta_color="inverse")

json

df = pd.DataFrame(np.random.randn(10, 2), columns=["prices", "diff"])

# Line Chart
st.line_chart(df, y=["prices"])

st.line_chart(df, y=["diff"])

st.area_chart(df)

st.bar_chart(df)


fig, ax = plt.subplots()
ax.scatter(np.arange(10), np.arange(10) ** 2)
st.pyplot(fig)

fig, ax = plt.subplots()
ax.hist(np.random.randn(100), bins=10)
st.pyplot(fig)

places = pd.DataFrame({"lat": [19.07, 28.64], "lon": [72.88, 77.21]})


st.map(places)
if st.button("Click me"):
    st.write(time.time())

st.title("This is the title function")
st.header("Header")
st.subheader("Subheader")
st.subheader("Subheader")


df = pd.DataFrame(np.random.randn(10, 2), columns=["col1", "col2"])

data = df.to_csv().encode("utf-8")

st.download_button(
    label="Download Data",
    data=data,
    file_name="data.csv",
    mime="text/csv",
)

text = "This is the title function"

st.download_button(label="Download Text", data=text)

if st.checkbox("I agree", value=True):
    st.write("Agreement Done")
else:
    st.write("Agreement is not done")

option = st.radio(
    label="Order your food",
    options={
        "Pizza",
        "Burger",
        "Chips",
    },
    index=2,
)

if option == "Pizza":
    st.write(option)
elif option == "Burger":
    st.write(option)
elif option == "Chips":
    st.write(option)

option = st.selectbox(
    label="Where do you live", options={"Moscow", "New York", "Istanbul"}
)

if option == "Istanbul":
    st.write("You live in Istanbul")
elif option == "New York":
    st.write("You live in New York")
elif option == "Moscow":
    st.write("You live in Moscow")

option = st.multiselect(
    label="Which places have you been?",
    options=("Sydney", "Tokyo", "New Delhi", "Paris", "Cape Town"),
    default=("Sydney", "Paris"),
)

st.write(option)

num = st.slider(label="Your Age", min_value=18, max_value=120, value=20, step=1)
st.write(num)

num = st.slider(label="Your age", min_value=18, max_value=120, value=(40, 60), step=1)

st.write(num)

visting_timing = st.slider(label="Your Appointmnet", value=(time(11, 30), time(12, 45)))
st.write(visting_timing)

option = st.select_slider(
    label="Select the Best Color",
    options=("Violet", "Indigo", "Blue", "Green", "Yellow", "Orange", "Red"),
)
st.write(option)


start_color, end_color = st.select_slider(
    label="Select the Best Color",
    options=("Violet", "Indigo", "Blue", "Green", "Yellow", "Orange", "Red"),
    value=("Blue", "Orange"),
)
st.write(start_color)

st.write(end_color)

txt = st.text_input(
    label="Please Enter your mail id",
    max_chars=20,
    placeholder="mandepudi.mk@gmail.com",
)

st.write(txt)

passw = st.text_input(
    label="Enter you password",
    max_chars=20,
    placeholder="password here",
    type="password",
)

num = st.number_input(
    label="Enter your Weights", min_value=40, max_value=120, value=65, step=1
)

st.write(num)
