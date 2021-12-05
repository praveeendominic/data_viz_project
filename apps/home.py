import streamlit as st

def app():
    st.write('This is the `home page` of this app.')
    st.title('Project Objectives:')
    st.write(
    'It’s difficult to overstate just how much the COVID-19 pandemic has devastated airlines.'
    'Financial woes aside, the pandemic’s longer-term effects on aviation are emerging.'
    'Hence, we decided to work on a project that would quantify the impact the covid has created in the US air travel industry at various granular levels.'
    'The objective is to create a web application that emphasizes majorly on descriptive analytics and some part of diagnostic and predictive analytics in the '
        'context of US airline impact during the onset of covid-19 pandemic. Granularity studied includes the impact in the overall US, state-wise impact and then the '
        'impact in the top routes of the air travel. The afore-said granularities encompass the `descriptive analytics` part of the project. '
        'Also, we have developed one simple animation visualization to depict the the correlation between the sudden devline in the US air travel and the rise of the covid-19 pandemic. This constitutes the `diagnostic analytics` part of this project.'
        'Regarding the predictive analytics, we have tried to leverage the Machine learning capabilities of Tableau, by making use of the Regression, Clustering, and the forecasting analytical options available. '
        'The objective of the `predictive analytics` deployed in our context is to provide a fair idea about trends that prevail state-wise and for the overall US data. '
        'Also, forecasting the number of travellers in the near future also falls under the scope of this project objective.')
    #st.write('In this app, we will be building a series of visualizations that show how bad USA was impacted during the onset of Covid-19 in 2020. Also, we have used some ml algorithms like regression, clustering and forecasting to predict the near future recovery status of the airline industry.')

    from PIL import Image
    image=Image.open('home.jpg')
    st.image(image)