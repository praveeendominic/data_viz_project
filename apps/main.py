# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import streamlit as st
import streamlit.components.v1 as stc
import codecs

def index_htmpage(index_htm, width,height):
    f=codecs.open(index_htm,'r')
    page=f.read()
    stc.html(page, width=width,height=height, scrolling=False)

def app():
    _2019 = st.container()  # 800*700
    routes = st.container()  # 800*1000
    states = st.container()
    story=st.container()
    anim = st.container()
    index = st.container()
    dash = st.container()
    # with dash:
    html_tmp = """
                            <div class='tableauPlaceholder' id='viz1636419054366' style='position: relative'><noscript><a href='#'><img alt='mom2021  ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Da&#47;DataViz_Project_AMOD5430H_Group11&#47;mom2021&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='path' value='views&#47;DataViz_Project_AMOD5430H_Group11&#47;mom2021?:language=en-US&amp;:embed=true&amp;:toolbar=yes&amp;:embed_code_version=3&amp;:loadOrderID=0&amp;publish=yes?:embed&amp;:display_count=yes' /> <param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Da&#47;DataViz_Project_AMOD5430H_Group11&#47;mom2021&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /><param name='filter' value='publish=yes' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1636419054366');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.width='1000px';vizElement.style.minHeight='627px';vizElement.style.maxHeight='727px';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='1000px';vizElement.style.minHeight='627px';vizElement.style.maxHeight='727px';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';} else { vizElement.style.width='1000px';vizElement.style.minHeight='627px';vizElement.style.maxHeight='727px';vizElement.style.height=(divElement.offsetWidth*1.77)+'px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>
                            """
    # stc.html(html_tmp)
    # index_htmpage('index.html')

    with _2019:
        _2019.title('2020 vs 2019')
        index_htmpage('2020vs2019.html', width=1000, height=800)  #width=1000, height=1100
        # _2019.text('dgkjdgndkjgnkdfjngkfdjngkdfjgnkfjdgnkdfjngdgnkdjfngkfdjngkdjngfdkj')

    # index_htmpage('routes.html')
    # index_htmpage('states.html')

    with routes:
        routes.title('Routes')
        index_htmpage('routes.html', width=1000, height=900)#height=1100

    with states:
        states.title('State viz analysis')
        index_htmpage('states.html', width=1000, height=800)

    with story:
        story.title('Summary Inference')
        index_htmpage('impact_story.html', width=1100, height=1400)

    #def main():


        # with index:
        # index_htmpage('index.html')

    #if __name__ == '__main__':
    #    main()






