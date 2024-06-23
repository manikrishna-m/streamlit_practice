import streamlit as st
import time

choice = st.sidebar.radio(label="Choose the option", options=("audio", "video"))

if choice == "audio":
    st.write("This is audio")
elif choice == "video":
    st.write("This is video")


col1, col2 = st.columns(2, gap="small")
col1.write("This is audio")
col2.write("This is video")

tab1, tab2 = st.tabs(["audio", "video"])
tab1.write("This is audio")
tab2.write("This is video")

exp = st.expander("See pic")
exp.write("This is image")
exp.write("This is video")

col1, col2 = st.columns([1, 2], gap="small")
col1.write("This is audio")
col2.write("This is video")


st.write("One")
st.write("Two")
st.write("Three")

cont = st.container()

cont.write("One")
st.write("Two")
cont.write("Three")

txt = "% completed"

my_bar = st.progress(0, text=txt)

for pr in range(100):
    time.sleep(0.1)
    my_bar.progress(pr + 1, text=txt)

with st.spinner("Wait for it.."):
    time.sleep(0.1)

st.write("Wait Over")

st.balloons()

st.snow()

st.error("This is an error message")

st.warning("This is an warning message")

st.info("This is an information message")

st.success("This is a success message")

e = RuntimeError("Exp")
st.exception(e)
