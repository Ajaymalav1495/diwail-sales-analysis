def data():
    import streamlit as st
    import pandas as pd
    st.header("Diwali Sales Analysis")
    # Displaying the import code
    st.code("""# Import python libraries
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt  # visualizing data
%matplotlib inline
import seaborn as sns""")
    
    # Reading the CSV file
    st.code("df = pd.read_csv('Diwali Sales Data.csv', encoding='unicode_escape')")
    df = pd.read_csv('Diwali Sales Data.csv', encoding='unicode_escape')
    st.dataframe(df)
    
    # Displaying the shape of the DataFrame
    st.code("df.shape")
    st.write(df.shape)
    
    # Displaying the first few rows of the DataFrame
    st.code('df.head()')
    st.write(df.head())
    
    # Displaying DataFrame info
    st.code("df.info()")
    buffer = pd.io.formats.format.StringIO()
    df.info(buf=buffer)
    s = buffer.getvalue()
    st.text(s)

    # Dropping unrelated/blank columns
    st.code("# Drop unrelated/blank columns \n df.drop(['Status', 'Unnamed: 1'], axis=1, inplace=True)")
    #df.drop(['Status', 'Unnamed: 1'], axis=1, inplace=True)

    # Checking for null values
    st.code('# Check for null values \n pd.isnull(df).sum()')
    st.write(pd.isnull(df).sum())
    
    # Dropping null values
    st.code("# Drop null values \n df.dropna(inplace=True)")
    df.dropna(inplace=True)

    # Converting 'Amount' column to integer type
    st.code("df['Amount'] = df['Amount'].astype('int')")
    df['Amount'] = df['Amount'].astype('int')

    # Displaying the data types of columns
    st.code("df['Amount'].dtypes")
    st.write(df['Amount'].dtypes)
    
    # Displaying the columns of the DataFrame
    st.code("df.columns")
    st.write(df.columns)


    # Displaying the description of the DataFrame
    st.code("""# describe() method returns description of the data in the DataFrame (i.e. count, mean, std, etc)
df.describe()""")
    st.dataframe(df.describe())

    st.code("""# use describe() for specific columns
df[['Age', 'Orders', 'Amount']].describe()""")
