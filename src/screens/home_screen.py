
import streamlit as st
from src.components.header import header_home
from src.ui.base_layout import style_base_layout, style_background_home
from src.components.footer import footer_home

def home_screen():    

    header_home()
    style_background_home()
    style_base_layout()

    col1, col2 = st.columns(2)
    with col1:
            st.header("I'm Student")
            st.image("C:/Users/User/Desktop/snapclass/src/screens/student.jpeg",width=120)
            if st.button('student portal',type='primary',icon=':material/arrow_upward:', icon_position='right'):
               st.session_state['login_type']='student'
               st.rerun
   
    with col2:
        st.header("I'm Teacher")
        st.image("C:/Users/User/Desktop/snapclass/src/screens/teacher.jpeg",width=120)
        if st.button('teacher portal', type='primary',icon=':material/arrow_upward:',icon_position='right'):
             st.session_state['login_type']='teacher'
             st.rerun

    footer_home()         