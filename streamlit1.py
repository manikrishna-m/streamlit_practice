import streamlit as st
import datetime
from PIL import Image
import numpy as np
from io import StringIO

txt = st.text_area(
    label="Write Something", height=200, max_chars=100, placeholder="Please write here"
)


dat = st.date_input("Enter your birth date", value=datetime.date(2023, 4, 11))

tim = st.time_input("Enter your meal time", value=datetime.time(14, 00))

fl = st.file_uploader(
    label="Please Upload here",
)

if fl:
    st.write(fl.type)
    if "image" in fl.type:
        img = Image.open(fl)
        st.write(np.array(img).shape)
    elif "text" in fl.type:
        stringio = StringIO(fl.getvalue().decode("utf-8"))
        st.write(stringio.read())

picture = st.camera_input("Take a picture")
if picture:
    img = Image.open(picture)
    st.write(np.array(img).shape)


color = st.color_picker("Pick a color")
if color:
    st.write("You Selected", color)
