import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def occupation():
    st.write("---")
    st.header("Diwali Sales Analysis")
    st.subheader("Occupation")
    
    # Load data
    df = pd.read_csv('Diwali Sales Data.csv', encoding='unicode_escape')
    
    # Display code for loading data
    st.code("df = pd.read_csv('Diwali Sales Data.csv', encoding= 'unicode_escape')")
    
    # Count plot of Occupation
    sns.set(rc={'figure.figsize':(20,5)})
    ax = sns.countplot(data=df, x='Occupation')
    for bars in ax.containers:
        ax.bar_label(bars)
    
    # Display first plot
    st.pyplot(plt)
    st.write("---")
    
    # Bar chart for Occupation vs Total Amount
    sales_state = df.groupby(['Occupation'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)
    
    # Display code for the bar chart
    st.code("""
    sales_state = df.groupby(['Occupation'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)
    sns.set(rc={'figure.figsize':(20,5)})
    sns.barplot(data=sales_state, x='Occupation', y='Amount')
    """)
    
    sns.set(rc={'figure.figsize':(20,5)})
    sns.barplot(data=sales_state, x='Occupation', y='Amount')
    
    # Display second plot
    st.pyplot(plt)
    st.dataframe(sales_state)
    
    # Conclusion based on the analysis
    st.write("### Conclusion")
    st.write("""
    The analysis of the Diwali sales data by occupation reveals that different occupations have varying levels of engagement and spending power. 
    By visualizing the number of transactions and the total amount of sales by occupation, it is evident which occupations contribute more to sales. 
    These insights can help tailor marketing strategies and understand customer behavior better.
    """)
