import streamlit as st

st.title("Hello Streamlit 👋")
st.write("This is my first Streamlit app!")
st.markdown("# this is title")
st.markdown("## this is title")
st.markdown("### this is title")
st.success("this is success")
st.warning("this is success")
st.error("this is error")
st.info("this is info")
is_checked = st.checkbox("I agree")

if is_checked:
    st.write("user Agreed")
else:
    st.write("disagreed ???")

gender = st.radio("Select gender", {"m", "f", "other"})
st.write(f"user selected {gender}")
st.selectbox("select", {"a", "b", "c", "d", "e"})
ms = st.multiselect("select", {"a", "b", "c", "d", "e"})
st.write(f"user selected {ms}")


def predicthai():
    st.write("returned from predict")


btn = st.button("Predict")

if btn:
    predicthai()

st.text_input("enter name", placeholder="dfas")
st.number_input("enter name", min_value=0, max_value=10)
st.text_area("enter name", placeholder="dfas")
number = st.slider("Pick a number", 1, 100, 60)
st.write("You picked:", number)

from PIL import ptl

