import streamlit as st
from multiapp import MultiApp
from apps import home, anim_ml, main
#from apps import main

app = MultiApp()

st.markdown("""
# Data Viz final project_Group 11_Praveen & Niranjan
    
""")

st.write('In this app, we will be building a series of visualizations that show how bad USA was impacted during the onset of Covid-19 in 2020. Also, we have used some ml algorithms like regression, clustering and forecasting to predict the near future recovery status of the airline industry.')

# Add all your application here
app.add_app("Home", home.app)
app.add_app("The decline in US air travel", main.app)
app.add_app("Ml models", anim_ml.app)
# The main app
app.run()

