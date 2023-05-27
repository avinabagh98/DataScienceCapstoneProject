import streamlit as st
import pickle

with open("stylesheet.css") as source_des:
    st.markdown(f"<style>{source_des.read()}</style>", unsafe_allow_html = True)


st.title(':red[Car Value Calculator]')


bodyCol1, bodyCol2 = st.columns(2)

with bodyCol1:
    st.markdown("<h2 style= font-weight:100 >Get the best value for your car with this AI powered tool</h2>", unsafe_allow_html=True)
    # st.subheader('with this :red[AI Powered tool]')

with bodyCol2:
    with st.form("predictionForm", clear_on_submit=True):
        car = st.text_input("Enter the name of car")
        brandName = car.split(" ")[0].title()
        modelName = " ".join(car.split(" ")[1:3]).title()
        
        Years = ["Choose year",2020, 2019, 2018, 2017, 2016, 2015, 2014, 2013, 2012, 2011, 2010,
            2009, 2008, 2007, 2006, 2005, 2004, 2003, 2002, 2001, 2000, 1999,
            1998, 1997, 1996, 1995, 1992]
        year = st.selectbox("Enter the year of purchase", Years, index=0)

        kms = st.number_input("Enter the number of kms driven", max_value=172500)
        fuel = st.selectbox("Enter the type of fuel", ["Choose type", "Petrol","LPG", "Electric", "Diesel", "CNG"])
        seller = st.selectbox("Enter the type of seller", ["Dealer", "Individual", "Trustmark Dealer"])
        transmission = st.selectbox("Enter the transmission type of the car", ["Manual", "Automatic"])
        owner = st.selectbox("Enter the type of owner", ["First Owner", "Second Owner", "other"])
        
        state = st.form_submit_button("Predict")

test = [[brandName, modelName, year, kms, fuel, seller, transmission, owner]]

bestModel = pickle.load(open('pipe.pkl', 'rb'))
prediction = bestModel.predict(test)

if state:
    with bodyCol1:
        st.write("The estimated value for your vehicle is:")
        st.write(prediction[0])
