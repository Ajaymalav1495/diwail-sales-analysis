def Gender():
    import streamlit as st
    import numpy as np 
    import pandas as pd 
    import matplotlib.pyplot as plt 
    import seaborn as sns
    st.write("---")
    st.header("Diwali Sales Analysis")
    st.sub_header("Gender")
    st.code("df = pd.read_csv('Diwali Sales Data.csv', encoding= 'unicode_escape')")
    df = pd.read_csv('Diwali Sales Data.csv', encoding= 'unicode_escape')
    st.code("""ax = sns.countplot(x = 'Gender',data = df)

for bars in ax.containers:
    ax.bar_label(bars)""")
    ax = sns.countplot(x = 'Gender',data = df)

    for bars in ax.containers:
        ax.bar_label(bars)
    st.pyplot(plt)

    st.write("---")

    st.code("""# plotting a bar chart for gender vs total amount

sales_gen = df.groupby(['Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.barplot(x = 'Gender',y= 'Amount' ,data = sales_gen)""")

    # plotting a bar chart for gender vs total amount

    sales_gen = df.groupby(['Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

    sns.barplot(x = 'Gender',y= 'Amount' ,data = sales_gen)

    st.pyplot(plt)
