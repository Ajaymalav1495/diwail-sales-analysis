def Gender():
    import streamlit as st
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns

    st.write("---")
    st.header("Diwali Sales Analysis")
    st.subheader("Gender")

    df = pd.read_csv('Diwali Sales Data.csv', encoding='unicode_escape')

    # Gender Count Plot
    ax = sns.countplot(x='Gender', data=df)
    for bars in ax.containers:
        ax.bar_label(bars)
    st.pyplot(plt)

    st.write("---")

    # Gender vs Total Amount Pie Chart
    sales_gen = df.groupby(['Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)
    
    # Plotting Pie Chart
    fig, ax = plt.subplots()
    ax.pie(sales_gen['Amount'], labels=sales_gen['Gender'], autopct='%1.1f%%', startangle=90)
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    st.pyplot(fig)
