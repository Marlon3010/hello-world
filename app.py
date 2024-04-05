import pandas as pd
import scipy.stats
import streamlit as st
import time

# estas son variables de estado que se conservan cuando Streamlin vuelve a ejecutar este script
if 'experiment_no' not in st.session_state:
    st.session_state['experiment_no'] = 0

if 'df_experiment_results' not in st.session_state:
    st.session_state['df_experiment_results'] = pd.DataFrame(columns=['no', 'iteraciones', 'media'])

st.header('Lanzar una moneda')

chart = st.line_chart([0.5])
