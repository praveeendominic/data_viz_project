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
    with anim:
        anim.title('Animation & ml')
        index_htmpage('animation.html', width=1100, height=1000)  #
    with reg:
        anim.title('Regression')
        index_htmpage('regression.html', width=1100, height=1000)  #
    with clust:
        clust.title('Clustering & Forescasting')
        index_htmpage('clustering_forecasting.html', width=1100, height=1000)  #
