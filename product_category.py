import streamlit as st
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns

def product_category():
    st.write("---")
    st.header("Diwali Sales Analysis")
    st.subheader("Product_Category")
    
    # Load the dataset
    df = pd.read_csv('Diwali Sales Data.csv', encoding= 'unicode_escape')

    st.code("""sns.set(rc={'figure.figsize':(20,5)})
    ax = sns.countplot(data = df, x = 'Product_Category')
    for bars in ax.containers:
        ax.bar_label(bars)
    st.pyplot(plt)""")
    # Plot the count of each product category
    sns.set(rc={'figure.figsize':(20,5)})
    ax = sns.countplot(data = df, x = 'Product_Category')
    for bars in ax.containers:
        ax.bar_label(bars)
    st.pyplot(plt)
    
    st.write("---")
    
    # Group by product category and sum the amount
    sales_state = df.groupby(['Product_Category'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)
    st.code(""" sns.set(rc={'figure.figsize':(20,5)})
    sns.barplot(data = sales_state, x = 'Product_Category', y = 'Amount')
    st.pyplot(plt)""")
    # Plot the sales amount by product category
    sns.set(rc={'figure.figsize':(20,5)})
    sns.barplot(data = sales_state, x = 'Product_Category', y = 'Amount')
    st.pyplot(plt)
    
    # Display the grouped data in a dataframe
    st.dataframe(sales_state)
    
    # Conclusion
    highest_sales_category = sales_state.iloc[0]['Product_Category']
    highest_sales_amount = sales_state.iloc[0]['Amount']
    st.write(f"The product category with the highest sales during Diwali is **{highest_sales_category}** with a total sales amount of **₹{highest_sales_amount}**.")

product_category()
