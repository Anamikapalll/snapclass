
import streamlit as st

def style_background_home():
    st.markdown("""
        <style>

        .stApp {
        background: #5865f2 !important
        }
    </style>
    
    """
                , unsafe_allow_html = True
)


def style_background_dashboard():
    st.markdown("""
        <style>

        .stApp {
        background: #E0E3FF !important
        }
    </style>
    
    """
                , unsafe_allow_html = True
)

def style_base_layout():
    st.markdown("""
        <style>
        
        @import url('https://fonts.googleapis.com/css2?family=Climate+Crisis:YEAR@1979&display=swap');
        @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@100..900&display=swap');



        /*  Hide toolbar of streamlit  */
            #MainMenu, footer, header !important;{
                visibility: hidden !important;
            }
                .block-container {
                padding-top:3.5rem !important;
            }
            h1 {
                font-family:'Climate Crisis', sans-serif !important;
                font-size: 2rem, !important;
                line-height: 1.1 !important;
                margine-bottom: 0rem !important;
                color: #E03FF;
                }

            h2 {
                font-family:'Climate Crisis', sans-serif !important;
                font-size: 2rem, !important;
                line-height: 1.1 !important;
                margine-bottom: 0rem !important;
                color: #E03FF;
                }

            h3,h4,p{
                font-family: 'outfit', sans-serif;            
            } 
            button{
                border-radius:1.5rem !important;
                background: #5865F2 !important;
                color:white !important;
                padding:10px 20px!important;
                border:none !important;
                transition:transform0.25s ease-in-out !important;         
            }  

            button[kind="secondary"]{
                border-radius:1.5rem !important;
                background: #EB459E !important;
                color:white !important;
                padding:10px 20px!important;
                border:none !important;
                transition:transform 0.25s ease-in-out !important;
            }  

            button[kind="tertiar"]{
                border-radius:1.5rem !important;
                background: black !important;
                color:white !important;
                padding:10px 20px!important;
                border:none !important;
                transition:transform 0.25s ease-in-out !important;         
            }  
            button:hover{
                transform :scale(1.05)
            }
    </style>
    
    """
                , unsafe_allow_html = True
)


