import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def States():
    st.write("---")
    st.header("Diwali Sales Analysis")
    st.subheader("State")
    
    # Load data
    df = pd.read_csv('Diwali Sales Data.csv', encoding='unicode_escape')
    
    # Display code for loading data
    st.code("df = pd.read_csv('Diwali Sales Data.csv', encoding= 'unicode_escape')")
    
    # Total number of orders from top 10 states
    sales_state = df.groupby(['State'], as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(10)
    
    # Display code for the bar chart
    st.code("""
    # Total number of orders from top 10 states
    sales_state = df.groupby(['State'], as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(10)
    sns.set(rc={'figure.figsize':(15,5)})
    sns.barplot(data=sales_state, x='State', y='Orders')
    """)
    
    sns.set(rc={'figure.figsize':(15,5)})
    sns.barplot(data=sales_state, x='State', y='Orders')
    
    # Display first plot
    st.pyplot(plt)
    st.write("---")
    
    # Total sales amount from top 10 states
    sales_state = df.groupby(['State'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)
    
    # Display code for the bar chart
    st.code("""
    
    sns.set(rc={'figure.figsize':(15,5)})
    sns.barplot(data=sales_state, x='State', y='Amount')
    """)
    
    sns.set(rc={'figure.figsize':(15,5)})
    sns.barplot(data=sales_state, x='State', y='Amount')
    
    # Display second plot
    st.pyplot(plt)
    st.dataframe(sales_state)
    
    # Conclusion based on the analysis
    st.write("### Conclusion")
    st.write("""
    The analysis of the Diwali sales data by state highlights the top 10 states with the highest number of orders and total sales amounts.
    These insights can help identify key markets and focus efforts on regions with high sales performance, which can be valuable for optimizing sales strategies 
    and allocating resources efficiently.
    """)
