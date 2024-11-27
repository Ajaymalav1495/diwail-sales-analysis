import streamlit as st
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns

def Gender():
    st.write("---")
    st.header("Diwali Sales Analysis")
    st.subheader("Gender")
    df = pd.read_csv('Diwali Sales Data.csv', encoding='unicode_escape')
    
    st.code("""sns.set(rc={'figure.figsize':(20,5)})
ax = sns.countplot(x = 'Gender', data = df)
for bars in ax.containers:
    ax.bar_label(bars)
st.pyplot(plt)""")
    
    sns.set(rc={'figure.figsize':(20,5)})
    ax = sns.countplot(x = 'Gender', data = df)
    for bars in ax.containers:
        ax.bar_label(bars)
    st.pyplot(plt)
    
    st.write("---")
    
    st.code("""sales_gen = df.groupby(['Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)
plt.figure(figsize=(10, 7))
plt.pie(sales_gen['Amount'], labels=sales_gen['Gender'], autopct='%1.1f%%')
plt.title('Gender vs Total Amount')
st.pyplot(plt)""")
    
    sales_gen = df.groupby(['Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

    plt.figure(figsize=(10, 7))
    plt.pie(sales_gen['Amount'], labels=sales_gen['Gender'], autopct='%1.1f%%')
    plt.title('Gender vs Total Amount')
    st.pyplot(plt)

Gender()
