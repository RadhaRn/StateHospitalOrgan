
import pandas as pd
import streamlit as st


def process():
    # randomizing icon & setting up logo
    st.set_page_config(page_title='State-Hospital finder', page_icon='random', initial_sidebar_state='auto')

    # hide hamburger menu and footer
    hide_st_style = """
                    <style>
                    #MainMenu {visibility: hidden;}
                    footer {visibility: hidden;}
                    </style>
                    """
    st.markdown(hide_st_style, unsafe_allow_html=True)

    data_df = (pd.read_excel('./StateHospitalSpclty.xlsx', engine='openpyxl')).sort_values(['State', 'Organ'])

    state = st.sidebar.selectbox(label='Choose state', options=data_df['State'].unique().tolist())

    if state:
        organ = ''
        sel_state_df = data_df.loc[(data_df['State'] == state)]
        organ = st.sidebar.selectbox(label='Choose organ disease', options=sel_state_df['Organ'].unique().tolist())
        hosp_list = (sel_state_df.loc[(sel_state_df['Organ'] == organ)])['Hospital'].tolist()

        st.write(f'Your options for {state} are as follows:')
        for hospName in enumerate(hosp_list):
            st.write(hospName[1])


if __name__ == '__main__':
    process()

