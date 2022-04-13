import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib as mpl
import streamlit as st

st.write("""
# My first app
# Hello *world!*
# """)
num = 0

if st.button('Click this'):
    num += 1
    st.write(num)

path1 = '/Users/claywrentz/Desktop/ML-Fontenot/MLProject2/Dataset1/train.xlsx' 
flight1 = pd.read_excel(path1)

st.line_chart(data=flight1['Price'], width=0, height=0, use_container_width=True)
