def Age():
    import streamlit as st
    import numpy as np 
    import pandas as pd 
    import matplotlib.pyplot as plt 
    import seaborn as sns
    st.write("---")
    st.header("Age")
    st.code("df = pd.read_csv('Diwali Sales Data.csv', encoding= 'unicode_escape')")
    df = pd.read_csv('Diwali Sales Data.csv', encoding= 'unicode_escape')
    st.code("""ax = sns.countplot(data = df, x = 'Age Group', hue = 'Gender')

for bars in ax.containers:
    ax.bar_label(bars)""")
    ax = sns.countplot(data = df, x = 'Age Group', hue = 'Gender')

    for bars in ax.containers:
        ax.bar_label(bars)
    st.pyplot(plt)

    st.write("---")

    st.code("""# Total Amount vs Age Group
sales_age = df.groupby(['Age Group'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.barplot(x = 'Age Group',y= 'Amount' ,data = sales_age)""")


    sales_age = df.groupby(['Age Group'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

    sns.barplot(x = 'Age Group',y= 'Amount' ,data = sales_age)

    st.pyplot(plt)
