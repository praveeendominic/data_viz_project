import streamlit as st
import plotly.express as pl
import pandas as pd

cov_view=st.container()
pass_view=st.container()


def app():
    st.title('Home')
    with cov_view:
        covid = pd.read_csv(
            r'https://raw.githubusercontent.com/shinokada/covid-19-stats/master/data/daily-new-confirmed-cases-of-covid-19-tests-per-case.csv')
        covid.columns = ['Country', 'Code', 'Date', 'Confirmed', 'Days since confirmed']
        covid['Date'] = pd.to_datetime(covid['Date']).dt.strftime('%Y-%m-%d')

        country_options = list(covid['Country'].unique())
        date_options = list(covid['Date'].unique())

        st.header('Covid-19 data')
        st.write(covid.head(1000))

        covid_date = st.selectbox('Which date would you like to see', date_options, 100)
        covid_country = st.multiselect('Which country would you like to see?', country_options)

        covid = covid.loc[covid.Country.isin(covid_country), :]
        covid = covid.loc[covid.Date == covid_date]

        fig = pl.bar(covid, x='Country', y='Confirmed', color='Country', range_y=[0, 35000], animation_frame='Date',
                     animation_group='Country')

        # fig.layout.updatemenus[0].buttons[0].args[1]['frame']['duration']=30
        # fig.layout.updatemenus[0].buttons[0].args[1]['transition']['duration'] = 5

        fig.update_layout(width=800)
        st.write(fig)

    with pass_view:
        pass_tmp = pd.read_csv(
            r"C:\users\prave\OneDrive\Desktop\AMOD\2nd sem\Data Viz\Project\Fin US Monthly Air Passengers.csv")
        mask1 = pass_tmp.ORIGIN_COUNTRY == 'US'
        mask2 = pass_tmp.DEST_COUNTRY == 'US'
        mask3 = pass_tmp.YEAR.isin([2019, 2020])
        passengers = pass_tmp.loc[mask1 & mask2 & mask3, :]

        passengers['date'] = passengers.YEAR.astype(str) + '-' + passengers.MONTH.astype(str)
        passengers['date'] = pd.to_datetime(passengers.date).dt.strftime('%Y-%m')
        # st.title('EDA_Covid_ml')
        st.header('View US airline passenger data')
        st.write(passengers.head(1000).loc[passengers.AIRLINE_ID.isna() == False, :])

        # country_options = list(covid['Country'].unique())
        pass_date_options = list(passengers['date'].unique())
        # pass_date = st.selectbox('Which date would you like to see', pass_date_options)

        fig2 = pl.line(passengers, x='date', y='Sum_PASSENGERS')
        st.write(fig2)



