
import pandas as pd
import streamlit as st
import openpyxl


def process():
    data_df = pd.read_excel('./StateHospitalSpclty.xlsx', engine='openpyxl')
    st.write(data_df)


if __name__ == '__main__':
    process()
