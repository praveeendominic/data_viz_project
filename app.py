import streamlit as st
from multiapp import MultiApp
from apps import home, anim_ml, main
#from apps import main

app = MultiApp()

st.markdown("""
# Impact of the Covid-19 pandemic on America’s airline industry since the onset of the pandemic
## Data Visualization - Final Project
### Group 11
### Praveen  Dominic Dharmalinga Pandian (0691527) & Niranjan Purushothaman (0704586)
#### Dr. Fadi Alzhouri 

""")

#st.write('In this app, we will be building a series of visualizations that show how bad USA was impacted during the onset of Covid-19 in 2020. Also, we have used some ml algorithms like regression, clustering and forecasting to predict the near future recovery status of the airline industry.')

# Add all your application here
app.add_app("Home", home.app)
app.add_app("Descriptive Analytics", main.app)
app.add_app("Diagnostic & Predictive Analytics", anim_ml.app)
# The main app
app.run()

