import streamlit as st

def find_largest(num1, num2, num3):
    """
    This function finds the largest of three numbers.
    """
    largest = max(num1, num2, num3)
    return largest

st.title("Find the Largest Number")

# Input fields for the three numbers with default values set to 0
num1 = st.number_input("Enter the first number:", key="num1", min_value=-9999999999999, max_value=9999999999999, value=0)
num2 = st.number_input("Enter the second number:", key="num2", min_value=-9999999999999, max_value=9999999999999, value=0)
num3 = st.number_input("Enter the third number:", key="num3", min_value=-9999999999999, max_value=9999999999999, value=0)

# Clear input button
clear_button = st.button("Clear Inputs")

# Clear input fields on button click
if clear_button:
    num1 = ""
    num2 = ""
    num3 = ""
    st.experimental_rerun()

# Reset button
reset_button = st.button("Reset")

if reset_button:
    # Reset input fields to default values (0)
    num1 = 0
    num2 = 0
    num3 = 0
    st.experimental_rerun()

# Find the largest number
largest_number = find_largest(num1, num2, num3)

# Display the result
st.write("The largest number is:", largest_number)
