import pandas as pd
import streamlit as st

st.title('Hello World')
if 'count' not in st.session_state:
	st.session_state.count = 0

def increment_counter(increment_value=0):
	st.session_state.count += increment_value

def decrement_counter(decrement_value=0):
	st.session_state.count -= decrement_value

st.button('click me', on_click=increment_counter, kwargs=dict(increment_value=1))
st.button('dont click me', on_click=decrement_counter, kwargs=dict(decrement_value=1))

st.write(st.session_state.count)
