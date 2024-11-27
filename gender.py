import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def Gender():
    st.write("---")
    st.header("Diwali Sales Analysis")
    st.subheader("Gender")
    
    # Load data
    df = pd.read_csv('Diwali Sales Data.csv', encoding='unicode_escape')
    
    # Display code for loading data
    st.code("df = pd.read_csv('Diwali Sales Data.csv', encoding= 'unicode_escape')")
    
    # Count plot of Gender
    ax = sns.countplot(x='Gender', data=df)
    for bars in ax.containers:
        ax.bar_label(bars)
    
    # Display first plot
    st.pyplot(plt)
    st.write("---")
    
    # Bar chart for Gender vs Total Amount
    sales_gen = df.groupby(['Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)
    
    # Display code for the bar chart
    st.code("""
    # Plotting a bar chart for Gender vs Total Amount
    sales_gen = df.groupby(['Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)
    sns.barplot(x='Gender', y='Amount', data=sales_gen)
    """)
    
    sns.barplot(x='Gender', y='Amount', data=sales_gen)
    
    # Display second plot
    st.pyplot(plt)
    
    # Conclusion based on the analysis
    st.write("### Conclusion")
    st.write("""
    The analysis of the Diwali sales data by gender reveals that there are differences in the total sales amounts between genders. 
    By visualizing the number of transactions and the total amount of sales by gender, it is evident that one gender may have higher engagement 
    or spending power in the context of Diwali sales. Such insights can be valuable for targeted marketing strategies and understanding customer behavior.
    """)
