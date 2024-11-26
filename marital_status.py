def marital_status():
    import streamlit as st
    import numpy as np 
    import pandas as pd 
    import matplotlib.pyplot as plt 
    import seaborn as sns
    st.write("---")
    st.header("Diwali Sales Analysis")
    st.subheader("Marital_Statuse")
    st.code("df = pd.read_csv('Diwali Sales Data.csv', encoding= 'unicode_escape')")
    df = pd.read_csv('Diwali Sales Data.csv', encoding= 'unicode_escape')
    st.code("""ax = sns.countplot(data = df, x = 'Marital_Status')

sns.set(rc={'figure.figsize':(7,5)})
for bars in ax.containers:
    ax.bar_label(bars)""")
    ax = sns.countplot(data = df, x = 'Marital_Status')

    sns.set(rc={'figure.figsize':(7,5)})
    for bars in ax.containers:
        ax.bar_label(bars)
    st.pyplot(plt)

    st.write("---")

    st.code("""sales_state = df.groupby(['Marital_Status', 'Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.set(rc={'figure.figsize':(6,5)})
sns.barplot(data = sales_state, x = 'Marital_Status',y= 'Amount', hue='Gender')""")


    sales_state = df.groupby(['Marital_Status', 'Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

    sns.set(rc={'figure.figsize':(6,5)})
    sns.barplot(data = sales_state, x = 'Marital_Status',y= 'Amount', hue='Gender')

    st.pyplot(plt)
