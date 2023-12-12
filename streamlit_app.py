import altair as alt
import numpy as np
import pandas as pd
import streamlit as st

"""
# Welcome to Streamlit!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:.
If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
"""



def find_largest(num1, num2, num3):
  """
  This function finds the largest of three numbers.
  """
  largest = max(num1, num2, num3)
  return largest

st.title("Find the Largest Number")

# Input fields for the three numbers
num1 = st.number_input("Enter the first number:", min_value=-9999999999999, max_value=9999999999999)
num2 = st.number_input("Enter the second number:", min_value=-9999999999999, max_value=9999999999999)
num3 = st.number_input("Enter the third number:", min_value=-9999999999999, max_value=9999999999999)

# Find the largest number
largest_number = find_largest(num1, num2, num3)

# Display the result
st.write("The largest number is:", largest_number)

