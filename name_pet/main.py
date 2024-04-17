import langchain_helper2 as lch
import streamlit as st



st.title("Pets name generator")

animal_type = st.sidebar.selectbox("What is your pet?", ("Cat", "Dog", "Cow", "Hamster", "Giraffe"))



pet_color = st.sidebar.text_area(
    f"What color is your {animal_type}?", max_chars=15
)

response = lch.generate_pet_name(animal_type, pet_color)

st.text(response["pet_name"])

