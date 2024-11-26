def occupation():
    import streamlit as st
    import numpy as np 
    import pandas as pd 
    import matplotlib.pyplot as plt 
    import seaborn as sns
    st.write("---")
    st.header("Occupation")
    st.code("df = pd.read_csv('Diwali Sales Data.csv', encoding= 'unicode_escape')")
    df = pd.read_csv('Diwali Sales Data.csv', encoding= 'unicode_escape')
    st.code("""sns.set(rc={'figure.figsize':(20,5)})
ax = sns.countplot(data = df, x = 'Occupation')

for bars in ax.containers:
    ax.bar_label(bars)""")
    sns.set(rc={'figure.figsize':(20,5)})
    ax = sns.countplot(data = df, x = 'Occupation')

    for bars in ax.containers:
        ax.bar_label(bars)
    st.pyplot(plt)

    st.write("---")

    st.code("""sales_state = df.groupby(['Occupation'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data = sales_state, x = 'Occupation',y= 'Amount')""")


    sales_state = df.groupby(['Occupation'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

    sns.set(rc={'figure.figsize':(20,5)})
    sns.barplot(data = sales_state, x = 'Occupation',y= 'Amount')

    st.pyplot(plt)

    