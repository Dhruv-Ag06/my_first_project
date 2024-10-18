
import streamlit as st
st.set_page_config(page_icon="🍽️",initial_sidebar_state="collapsed")
from recipes import suggestions,list_of_recipes




st.markdown(
    """
<style>
    [data-testid="collapsedControl"] {
        display: none
    }
</style>
""",
    unsafe_allow_html=True,
)
st.title("Welcome to Recipe Genie 🍽️")
st.subheader("Your Personal Assistant for Creative Cooking")
st.write("""
Feeling hungry and can't decide what to cook? Recipe Genie is here to spark some culinary inspiration! 
Just input the ingredients you have, and we'll suggest mouth-watering recipes you can whip up.
""")
#This is for NER
# ingredients=st.multiselect("Enter the ingredients ",options=suggestions)
ingredients=st.text_input("Enter the ingredients ")
# # Custom CSS for a colored button
st.markdown("""
    <style>
    div.stButton > button:first-child {
        background-color: #4CAF50; /* Green */
        color: white;
        padding: 15px 32px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        cursor: pointer;
        border-radius: 8px;
        border: none;
    }
    </style>
    """, unsafe_allow_html=True)



if st.button("submit"):
    st.session_state["ingredients"]=ingredients
    if ingredients:
        st.switch_page("pages/search.py")

    





