import streamlit as st
import pandas as pd
import base64

st.title("Excel/CSV File Joiner")

st.header("Upload Excel/CSV Files")

uploaded_file1 = st.file_uploader(
    "Upload the first Excel/CSV file", type=["xls", "xlsx", "csv"]
)
uploaded_file2 = st.file_uploader(
    "Upload the second Excel/CSV file", type=["xls", "xlsx", "csv"]
)

if uploaded_file1 and uploaded_file2:
    st.header("Preview of Uploaded Files")

    file_extension = uploaded_file1.name.split(".")[-1]

    if file_extension in ["xls", "xlsx"]:
        df1 = pd.read_excel(uploaded_file1, engine="openpyxl")
        df2 = pd.read_excel(uploaded_file2, engine="openpyxl")
    elif file_extension == "csv":
        df1 = pd.read_csv(uploaded_file1)
        df2 = pd.read_csv(uploaded_file2)
    else:
        st.error(
            "Unsupported file format. Please upload an Excel (xls, xlsx) or CSV file."
        )
        st.stop()

    st.subheader("Data from File 1")
    st.write(df1)

    st.subheader("Data from File 2")
    st.write(df2)

    st.header("Join the Dataframes")

    join_type = st.selectbox(
        "Select join type:", ["Inner Join", "Left Join", "Right Join", "Outer Join"]
    )

    common_column = st.text_input("Enter the common column name for the join:")

    if st.button("Join Dataframes"):
        if join_type == "Inner Join":
            result_df = pd.merge(df1, df2, on=common_column, how="inner")
        elif join_type == "Left Join":
            result_df = pd.merge(df1, df2, on=common_column, how="left")
        elif join_type == "Right Join":
            result_df = pd.merge(df1, df2, on=common_column, how="right")
        elif join_type == "Outer Join":
            result_df = pd.merge(df1, df2, on=common_column, how="outer")

        st.subheader("Resulting Dataframe")
        st.write(result_df)

        st.header("Download Result as File")

        if file_extension in ["xls", "xlsx"]:
            result_file = result_df.to_excel(index=False, engine="openpyxl")
            file_extension = "xlsx"
        elif file_extension == "csv":
            result_file = result_df.to_csv(index=False)
            file_extension = "csv"

        b64 = base64.b64encode(result_file.encode()).decode()
        href = f'<a href="data:application/octet-stream;base64,{b64}" download="result.{file_extension}">Download Result</a>'
        st.markdown(href, unsafe_allow_html=True)
