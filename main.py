import pandas as pd  # pandas
import numpy as np  # numpy
import seaborn as sns  # seaborn
import matplotlib.pyplot as plt  # plotting
import streamlit as st
from streamlit_option_menu import option_menu

from data1 import data
from gender import Gender
from state import States  
from occupation import occupation
from age import Age
from marital_status import marital_status
from product_category import  product_category

# Sidebar menu
with st.sidebar:
    selected = option_menu(
        menu_title="Main Menu",  # Required
        options=[
            "Home","Gender","occupation","marital_status","product_category","States","Age"

        ],  # Required
        menu_icon="cast",  # Optional
        default_index=0,  # Optional
    )


if selected == "Home":
    data()
elif selected == "Gender":
    Gender()
elif selected == "occupation":
    occupation()
elif selected == "marital_status":
    marital_status()
elif selected == "product_category":
    product_category()
elif selected == "States":
    States()
elif selected == "Age":
    Age()
st.header("Diwali Sales Analysis")
