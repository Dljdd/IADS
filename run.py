import streamlit as st
import numpy as np 
import pandas as pd
from PIL import Image

st.set_page_config(page_title="Integrated Ag Decision App", layout="wide")

page = st.sidebar.selectbox("Select page", 
                            ("Introduction","Crop Recommendation", 
                             "Disease Detection","Profitability Analysis"))

if page == "Introduction":

    st.header("Integrated Agriculture Decision Assistant")
    st.header("⭐️ Overview")
    st.write("""
            Our goal is to empower small farm holders with 
            data-driven intelligence for enhanced productivity, 
            profitability and sustainable cultivation through 
            precision agriculture.
        """)
    st.image("agriculture.jpg", width=700)

    left_column, right_column = st.columns([1,2])
    
    with left_column:
        st.header("Offerings")
        crop_rec = st.button("**Crop Recommender**")
        disease_det = st.button("**Disease Detector**")
        profit_anal = st.button("**Profit Analyzer**")

    with right_column:
        if crop_rec:
            st.header("Crop Recommender")
            st.write("""Suggests suitable crops to cultivate based 
                   on predictive modeling considering geographic variability  
                   in soil, climate and other parameters.""")
                   
        if disease_det:
            st.header("Disease Detector")
            st.write("""Employes image classification and computer vision  
                   techniques to detect onset of crop diseases through  
                   photographs of leaves for prompt intervention.""")
            
        if profit_anal:
            st.header("Profitability Analysis ")
            st.write("""Provides cultivation costs, expected yields and 
                  profitability forecasts across different crops tailored to the 
                individual farm size, soil quality and other parameters.""")

elif page == "Crop Recommendation":
    st.header("Crop Recommendation")
    
    # Inputs 
    
    n = st.number_input("Enter the Nitrogen Content") 
    p = st.number_input("Enter the Phosphorous Content") 
    k = st.number_input("Enter the Potassium Content") 

    temperature = st.slider("Select Average Temperature",0.0,40.0,(10.0,30.0),0.5)  
    humidity = st.slider("Select Humidity %",0,100, (50,80),10)
    rain = st.number_input("Please enter the amount of rainfall") 

    
    # Dummy prediction 
    crops = ["Rice","Wheat","Maize","Sugarcane"]
    pred_crop = np.random.choice(crops)
    
    # Output
    st.subheader("Recommended crops:")
    st.write(pred_crop)
    
elif page == "Disease Detection":

    st.header("Disease Detection") 
    
    image = st.file_uploader("Upload Image",type=["jpeg","jpg","png"])
    if image is not None:
        st.image(image,width=300)    
        
    # Dummy prediction         
    classes = ["Healthy","Blight","Rust","Scab","Mildew","Mosaic"]
    pred_class = np.random.choice(classes)
    
    # Output  
    st.subheader("Predicted Disease:")
    st.write(pred_class)
    
elif page == "Profitability Analysis":
   
    st.header("Profitability Analysis")  
    
    # Inputs
    area = st.number_input("Enter farm area (in hectares)",0.0,20.0,1.0) 
    crop = st.selectbox("Select target crop",["Rice","Wheat","Sugarcane"])
    market_rate = st.number_input("Enter expected market rate per kg",0.0,100.0,10.0)
    
    # Dummy prediction  
    profit = area * market_rate * np.random.randint(1000,5000)
    
    # Output
    st.subheader("Predicted Profit:")
    st.write("Rs.",int(profit))