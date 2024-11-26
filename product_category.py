def product_category():
    import streamlit as st
    import numpy as np 
    import pandas as pd 
    import matplotlib.pyplot as plt 
    import seaborn as sns
    st.write("---")
    st.header("Product_Category")
    st.code("df = pd.read_csv('Diwali Sales Data.csv', encoding= 'unicode_escape')")
    df = pd.read_csv('Diwali Sales Data.csv', encoding= 'unicode_escape')
    st.code("""sns.set(rc={'figure.figsize':(20,5)})
ax = sns.countplot(data = df, x = 'Product_Category')

for bars in ax.containers:
    ax.bar_label(bars)""")
    sns.set(rc={'figure.figsize':(20,5)})
    ax = sns.countplot(data = df, x = 'Product_Category')

    for bars in ax.containers:
        ax.bar_label(bars)
    st.pyplot(plt)

    st.write("---")

    st.code("""sales_state = df.groupby(['Product_Category'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)

sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data = sales_state, x = 'Product_Category',y= 'Amount')""")


    sales_state = df.groupby(['Product_Category'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)

    sns.set(rc={'figure.figsize':(20,5)})
    sns.barplot(data = sales_state, x = 'Product_Category',y= 'Amount')

    st.pyplot(plt)
