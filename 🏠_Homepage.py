import streamlit as st


st.set_page_config(
        page_title="Summer of Science",
        page_icon="☀️")

st.title('Summer of Science: EXPTECH')
st.header('Toolboxes')
st.page_link('pages/1_🎨_Colour_Converter.py', icon='🎨')
st.page_link('pages/2_🌡️_Black_Body.py', icon='🌡️')
st.page_link('pages/3_👨🏻‍🔬_Einstein_Coefficients.py', icon='👨🏻‍🔬')
st.page_link('pages/4_🔫_Practicum.py', icon='🔫')