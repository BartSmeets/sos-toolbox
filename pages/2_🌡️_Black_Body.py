import streamlit as st
import numpy as np

st.set_page_config(
        page_title="Summer of Science",
        page_icon="☀️")

# Constants
h = 4.135667696e-15     # Planck's constant (eV/Hz)
c = 2.99792458e17       # Speed of Light (nm/s)
k = 8.617343e-5    # Boltzmann Constant (eV/K)
converter = lambda x: h*c/x
Si_bandgap = 1.14   # eV

# Initialise session state
if 'bd-wavelength' not in st.session_state:
    st.session_state['bd-wavelength']  = converter(Si_bandgap)
if 'bd-energy' not in st.session_state:
    st.session_state['db-energy'] = Si_bandgap
if 'bd-T' not in st.session_state:
    st.session_state['bd-T'] = 300

# Define callbacks
def callback1():
    wavelength = st.session_state['bd-wavelength']
    st.session_state['bd-energy'] = converter(wavelength)
def callback2():
    energy = st.session_state['bd-energy']
    st.session_state['bd-wavelength'] = converter(energy)

st.title('Black Body Radiation')

# Dashboard
st.title('Colour Converter')
col1, col2 = st.columns(2)
with col1:
    with st.container(height=350):
        st.header('Input')
        st.number_input('Wavelength (nm)', min_value=10, max_value=10000, key='bd-wavelength', on_change=callback1)
        st.number_input('Energy (eV)', min_value=converter(10000), max_value=converter(10), key='bd-energy', on_change=callback2)
        st.number_input('Temperature (K)', min_value=4, key='bd-T')



