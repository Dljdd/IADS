import streamlit as st
import numpy as np 
import pandas as pd
from PIL import Image
import requests
from part1.imagemodel import imageModel
import cv2
import random

uploaded_image = None
crops = ['Wheat', 'Rice', 'Maize', 'Sugarcane', 'Cotton', 'Mothbeans', 'Tomato']

st.set_page_config(page_title="Integrated Ag Decision App", layout="wide")

page = st.sidebar.selectbox("Select page", 
                            ("Introduction","Vision", "Crop Recommendation", 
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
elif page == "Vision":
    st.header("Our Vision")
    st.image("landing-iot-devices.jpeg", width=800)
    st.header("Use of IoT Devices")
    st.write("""
     The IoT devices that the system will leverage include:

Soil sensors - Measure moisture, temperature and pH levels in real-time across the field. These metrics indicate the health and nutrition levels of the soil. Soil that is too dry or too wet, too cold or too hot, or with a poor pH balance negatively impacts crops. Integrating these insights allows for corrective recommendations to farmers on irrigation, fertilizers etc.\n
Weather stations - Provide hyperlocal weather data including temperature, rainfall and humidity levels. This will be fed into forecasting models to accurately predict yield outcomes, disease risks, and other crop patterns for an area. Continuous updates to weather trends also enable dynamic recommendations to farmers.\n
Leaf sensors - Can detect the early onset of diseases, pest attacks or nutritional deficiencies in plants by measuring chlorophyll content, water levels and changes to cellular structure in real time. The key benefit is that plant infections can be detected before physical symptoms appear, allowing the system to recommend preventative treatment.\n
By assimilating data from multiple sensor types to create a digital profile of the farm, the system can run analytics to derive preventative and prescriptive actions - thereby driving more informed decision making. Sensor integration is crucial to achieving precision, efficiency and profitability in agriculture.""")

elif page == "Crop Recommendation":
    st.header("Crop Recommendation")
    
    # Inputs 
    
    n = st.number_input("Enter the Nitrogen Content") 
    p = st.number_input("Enter the Phosphorous Content") 
    k = st.number_input("Enter the Potassium Content") 
    ph = st.number_input("Enter the pH Level of the soil") 
    temperature = st.number_input("Enter the Average Temperature")  
    humidity = st.number_input("Enter the Humidity %")
    rain = st.number_input("Please enter the amount of rainfall") 

    pred_crop = ""
    
    if st.button("Predict Crop"):
        url = "https://pred-test.onrender.com/predict"
        payload = {
            "n": n,
            "p": p, 
            "k": k,
            "temp": temperature,
            "humidity": humidity, 
            "ph": ph, 
            "rainfall": rain
        }
        response = requests.post(url, json=payload).json()
        pred_crop = response["predicted_crop"]

    # Output prediction
    
    # Output
    reco = random.choice(crops) 

     # Display the recommendation
    st.subheader("Recommended crops:")
    # st.write(f'Recommended crop: {reco}')
    st.write(pred_crop)
    
elif page == "Disease Detection":

    st.header("Disease Detection") 
    
    image = st.file_uploader("Upload Image",type=["jpeg","jpg","png"])
    
    if st.button("Identify Disease") and image is not None:
        st.image(image, width=300)
        image_content = image.read()

        img_array = np.asarray(bytearray(image_content), dtype=np.uint8)
        img = cv2.imdecode(img_array, 1) 

        imgModel = imageModel()
        pred_crop =  imgModel.predict_on_image(img)
        
        st.subheader("Predicted Disease:")
        st.write(pred_crop)
    
elif page == "Profitability Analysis":

    st.header("Profitability Analysis")  

    # Inputs
    area = st.number_input("Enter farm area (in hectares)",0.0,20.0,1.0)
    crop = st.selectbox("Select target crop",["Rice","Wheat","Sugarcane"])
    market_rate = st.number_input("Enter expected market rate per kg",0.0,100.0,10.0)

    # Crop yield estimates (kg/hectare)
    if crop == "Rice":
        yield_estimate = 50000 
    elif crop == "Wheat":
        yield_estimate = 30000
    else:
        yield_estimate = 70000

    # Calculate total yield
    total_yield = area * yield_estimate

    # Production costs
    costs = area * 25000 # Rs 25,000 per hectare

    # Calculate profit
    profit = total_yield * market_rate - costs

    if st.button("Estimate Profit"):
        st.subheader("Estimated Profit:")
        st.write("Rs.", int(profit))