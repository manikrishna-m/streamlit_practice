import streamlit as st
import pandas as pd


# Function to read the file based on its extension
def read_file(file):
    if file.name.endswith(".csv"):
        return pd.read_csv(file)
    elif file.name.endswith(".xlsx"):
        return pd.read_excel(file)
    else:
        st.error("Unsupported file type")
        return None


# Title of the app
st.title("Car Number Feature Adder")

# File uploader for two files
uploaded_files = st.file_uploader(
    "Upload two CSV or Excel files", type=["csv", "xlsx"], accept_multiple_files=True
)

if uploaded_files and len(uploaded_files) == 2:
    # Initialize a dictionary to store car numbers for each file
    car_numbers = {}

    # Display file paths and ask for car number for each file
    for uploaded_file in uploaded_files:
        st.write(f"File: {uploaded_file.name}")
        car_number = st.text_input(f"Enter the car number for {uploaded_file.name}")
        if car_number:
            car_numbers[uploaded_file.name] = car_number

    # Process the files once all car numbers have been entered
    if len(car_numbers) == 2:
        # Read and process each file
        dataframes = []
        for uploaded_file in uploaded_files:
            df = read_file(uploaded_file)
            if df is not None:
                df["car_number"] = car_numbers[uploaded_file.name]
                dataframes.append(df)

        # Display dataframes with new feature
        for idx, df in enumerate(dataframes):
            st.write(
                f"Data from file {uploaded_files[idx].name} with new feature 'car_number':"
            )
            st.dataframe(df)
    else:
        st.info("Please enter car numbers for all uploaded files.")
else:
    st.info("Please upload exactly two files.")
