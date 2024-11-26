def States():
    import streamlit as st
    import numpy as np 
    import pandas as pd 
    import matplotlib.pyplot as plt 
    import seaborn as sns
    st.write("---")
    st.header("Diwali Sales Analysis")
    st.subheader("State")
    st.code("df = pd.read_csv('Diwali Sales Data.csv', encoding= 'unicode_escape')")
    df = pd.read_csv('Diwali Sales Data.csv', encoding= 'unicode_escape')
    st.code("""# total number of orders from top 10 states

sales_state = df.groupby(['State'], as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(10)

sns.set(rc={'figure.figsize':(15,5)})
sns.barplot(data = sales_state, x = 'State',y= 'Orders')""")
    # total number of orders from top 10 states

    sales_state = df.groupby(['State'], as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(10)

    sns.set(rc={'figure.figsize':(15,5)})
    sns.barplot(data = sales_state, x = 'State',y= 'Orders')
    st.pyplot(plt)

    st.write("---")

    st.code("""sales_state = df.groupby(['State'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)

sns.set(rc={'figure.figsize':(15,5)})
sns.barplot(data = sales_state, x = 'State',y= 'Amount')""")


    sales_state = df.groupby(['State'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)

    sns.set(rc={'figure.figsize':(15,5)})
    sns.barplot(data = sales_state, x = 'State',y= 'Amount')

    st.pyplot(plt)
