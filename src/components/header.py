
import streamlit as st
import base64


def header_home():

    # Read image
    with open("src/components/logo.jpeg", "rb") as f:
        image = base64.b64encode(f.read()).decode()

    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:

        st.markdown(
            f"""
            <div class="logo-container">
                <img src="data:image/jpeg;base64,{image}" class="logo">
            </div>

            <h1 class="title">
                SNAP<br>CLASS
            </h1>

            <style>
                .logo-container {{
                    text-align: center;
                    margin-bottom: 15px;
                    margin-top: 30px;
                }}

                .logo {{
                    width: 100px;
                    height: 100px;
                    object-fit: contain;

                    border-radius: 20px;

                    border: 3px solid #E03FFF;

                    box-shadow: 0px 5px 15px rgba(0,0,0,0.3);
                }}

                .title {{
                    text-align: center;
                    color: #30EFF;
                    font-size: 28px;
                    line-height: 1;
                    margin-top: 10px;
                }}
            </style>
            """,
            unsafe_allow_html=True
        )