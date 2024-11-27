import streamlit as st
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns

def Age():
    st.write("---")
    st.header("Diwali Sales Analysis")
    st.subheader("Age")

    # Load the dataset
    df = pd.read_csv('Diwali Sales Data.csv', encoding= 'unicode_escape')

    st.code("""sns.set(rc={'figure.figsize':(20,5)})
ax = sns.countplot(data = df, y = 'Age Group', hue = 'Gender')
for bars in ax.containers:
    ax.bar_label(bars)
st.pyplot(plt)""")
    
    # Plot the count of each age group by gender
    sns.set(rc={'figure.figsize':(20,5)})
    ax = sns.countplot(data = df, y = 'Age Group', hue = 'Gender')
    for bars in ax.containers:
        ax.bar_label(bars)
    st.pyplot(plt)
    
    st.write("---")
    
    # Group by age group and sum the amount
    st.code("""sales_age = df.groupby(['Age Group'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)
sns.barplot(data = sales_age, y = 'Age Group', x = 'Amount')
st.pyplot(plt)""")
    
    sales_age = df.groupby(['Age Group'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

    # Plot the sales amount by age group
    sns.set(rc={'figure.figsize':(20,5)})
    sns.barplot(data = sales_age, y = 'Age Group', x = 'Amount')
    st.pyplot(plt)
    
    # Display the grouped data in a dataframe
    st.dataframe(sales_age)
    
    # Conclusion
    highest_sales_age_group = sales_age.iloc[0]['Age Group']
    highest_sales_amount = sales_age.iloc[0]['Amount']
    st.write(f"The age group with the highest sales during Diwali is **{highest_sales_age_group}** with a total sales amount of **₹{highest_sales_amount}**.")

Age()
