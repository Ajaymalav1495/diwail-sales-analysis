import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def marital_status():
    st.write("---")
    st.header("Diwali Sales Analysis")
    st.subheader("Marital Status")
    
    # Load data
    df = pd.read_csv('Diwali Sales Data.csv', encoding='unicode_escape')
    
    # Display code for loading data
    st.code("df = pd.read_csv('Diwali Sales Data.csv', encoding= 'unicode_escape')")
    
    # Count plot of Marital Status
    sns.set(rc={'figure.figsize':(7,5)})
    ax = sns.countplot(data=df, x='Marital_Status')
    for bars in ax.containers:
        ax.bar_label(bars)
    
    # Display first plot
    st.pyplot(plt)
    st.write("---")
    
    # Bar chart for Marital Status vs Total Amount (segmented by Gender)
    sales_state = df.groupby(['Marital_Status', 'Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)
    
    # Display code for the bar chart
    st.code("""
    sales_state = df.groupby(['Marital_Status', 'Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)
    sns.set(rc={'figure.figsize':(6,5)})
    sns.barplot(data=sales_state, x='Marital_Status', y='Amount', hue='Gender')
    """)
    
    sns.set(rc={'figure.figsize':(6,5)})
    sns.barplot(data=sales_state, x='Marital_Status', y='Amount', hue='Gender')
    
    # Display second plot
    st.pyplot(plt)
    st.dataframe(sales_state)
    
    # Conclusion based on the analysis
    st.write("### Conclusion")
    st.write("""
    The analysis of the Diwali sales data by marital status reveals that there are differences in the total sales amounts between different marital statuses. 
    By visualizing the number of transactions and the total amount of sales by marital status and gender, it becomes evident which groups contribute more to sales. 
    These insights can help tailor marketing strategies and understand customer behavior better.
    """)
