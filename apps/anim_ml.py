import streamlit as st
import streamlit.components.v1 as stc
import codecs

def index_htmpage(index_htm, width,height):
    f=codecs.open(index_htm,'r')
    page=f.read()
    stc.html(page, width=width,height=height, scrolling=False)

def app():
    anim = st.container()  # 800*700
    reg=st.container()
    clust=st.container()
    story = st.container()
    with anim:
        anim.title('DIAGNOSTIC ANALYTICS')
        index_htmpage('animation.html', width=1100, height=1000)  #
    with reg:
        anim.title('PREDICTIVE ANALYTICS')
        anim.title('Regression')
        index_htmpage('regression.html', width=1100, height=900)  #
    with clust:
        clust.title('Clustering & Forecasting')
        index_htmpage('clustering_forecasting.html', width=1100, height=1000)  #

    with story:
        story.title('Summary Inference')
        index_htmpage('pred_story.html', width=1100, height=1400)
