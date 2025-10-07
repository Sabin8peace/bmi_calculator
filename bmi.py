import streamlit as st

weight = st.text_input("enter weight", placeholder="WEIGHT")
height = st.text_input("enter height", placeholder="HEIGHT")


def bmi_category(bmi):
    match bmi:
        case _ if bmi < 18.5:
            return "Underweight"
        case _ if 18.5 <= bmi < 25:
            return "Normal weight"
        case _ if 25 <= bmi < 30:
            return "Overweight"
        case _ if bmi >= 30:
            return "Obesity"
        case _:
            return "Invalid value"


btn = st.button("Calc")

if btn:
    weight_val = float(weight)
    height_val = float(height)
    hm = height_val/100
    bmi = weight_val / (hm ** 2)
    category = bmi_category(bmi)
    st.success(f"Your BMI is: **{bmi:.2f}**")
    st.info(f"Category: **{category}**")
