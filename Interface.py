import streamlit as st
from PIL import Image
import pandas as pd 
import requests 
import plotly.express as px

img = Image.open("./dashboard.jpg")
st.image(img, width=4000)

st.set_page_config(page_title="Fake Store Insights", page_icon="🏤",layout="wide")
st.title("🏤 Fake Store API - Interactive DASHBOARD") 


Api = "https://fakestoreapi.com/products"

@st.cache_data 
def load_data():
    response = requests.get(Api)
    data = response.json()
    df = pd.DataFrame(data) 
    return df 

df = load_data() 

st.subheader(" 🏗️ Dataset Overview")
st.dataframe(df,use_container_width=True)


# Basic Cleaning 
df['price'] = df['price'].astype(float) 
df['category'] = df["category"].astype(str) 


# slider 
st.sidebar.header("🚥 Filters") 
categories = st.sidebar.multiselect(
    "Select Category",
    df["category"].unique(),default=df["category"].unique()
)

filtered_df = df[df['category'].isin(categories)]



#  KPI 

st.header(" 🏗️ Key Insights ")

col1,col2,col3 = st.columns(3) 

col1.metric("Total Product ",len(filtered_df))
col2.metric("Average Price ",f"${filtered_df['price'].mean():.2f}")
col3.metric("Hieghest Price ",f"${filtered_df['price'].mean():.2f}")


# Visuals 

st.header(" 🚃 Key Insights ")
# barchart :- categories count 
cate_count = filtered_df["category"].value_counts().reset_index()
fig_bar = px.bar(cate_count, x="category",y="count",title="Products Count by Category")
st.plotly_chart(fig_bar,use_container_width =True)


# Price distribution 
fig_hist = px.histogram(filtered_df,x='price',nbins=20,title="Price Distribution ")
st.plotly_chart(fig_hist,use_container_width=True) 


# Sactter PRICE VS ID 
fig_scatter = px.scatter(
    filtered_df,
    x="id",
    y="price",
    color="category",
    title="Price by product ID"
)
st.plotly_chart(fig_scatter,use_container_width=True) 


# Table View 
st.header("Filtered Product ")
st.dataframe(filtered_df,use_container_width=True) 


# Download Button 
csv = filtered_df.to_csv(index=False).encode("utf-8")
st.download_button("Download Filtered Data (csv)",csv,
                   "filtered_data.csv",
                   "text/csv"
)

