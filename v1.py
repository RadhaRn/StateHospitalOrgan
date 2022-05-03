import pandas as pd
import streamlit as st


def process():
    # randomizing icon & setting up logo
    st.set_page_config(page_title='State-Hospital finder', page_icon='random', initial_sidebar_state='auto')
    # st.sidebar.image('./images/logo-eee-XU-wobg.png', use_column_width=True)

    # hide hamburger menu and footer
    hide_st_style = """
                    <style>
                    #MainMenu {visibility: hidden;}
                    footer {visibility: hidden;}
                    </style>
                    """
    st.markdown(hide_st_style, unsafe_allow_html=True)

    data_df = (pd.read_excel('./StateHospitalSpclty.xlsx', engine='openpyxl')).sort_values(['State', 'Organ'])
    # data_df = data_df.sort_values(['State'])

    # temp_df = pd.DataFrame()
    # data_new = pd.concat([temp_df, data_df], ignore_index=False)
    # print(data_new.head())

    # st.write(data_df.head(10))
    # print(data_df.head())

    state = st.sidebar.selectbox(label='Choose state', options=data_df['State'].unique().tolist())
    # state = 'Delhi'
    # st.write(f'Selected state: {state}')
    if state:
        organ = ''
        sel_state_df = data_df.loc[(data_df['State'] == state)]
        organ = st.sidebar.selectbox(label='Choose organ disease', options=sel_state_df['Organ'].unique().tolist())
        # st.write(f'Selected organ: {organ}')
        # print(f'Selected organ: {organ}')
        hosp_list = (sel_state_df.loc[(sel_state_df['Organ'] == organ)])['Hospital'].tolist()
        # st.write(hosp_list.head())
        st.write(f'Your options for {state} are as follows:')
        for hospName in enumerate(hosp_list):
            st.write(hospName[1])


if __name__ == '__main__':
    process()
