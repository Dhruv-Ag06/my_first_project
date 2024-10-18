import streamlit as st
from recipes import list_of_recipes_2
st.set_page_config(page_icon="🥣",initial_sidebar_state="collapsed")

def show_recipe(recipe):
    """
    Searches for a recipe in the list of recipes.
    params: recipe["title"]
    """
    st.header(recipe)
    st.image("C:\\Users\Dhruv\\recipes_generator\\Food Images\\"+list_of_recipes_2[recipe]["Image_Name"]+".jpg",width=500)
    st.subheader("Ingredients:")
    st.write("All the ingredients required for making "+recipe+" are")
    for  i,ingredient in enumerate(eval(list_of_recipes_2[recipe]["Cleaned_Ingredients"])):
        st.write(str(i+1)+". "+ingredient)

    st.subheader("How to cook")
    st.write("To cook "+recipe+" follow these steps")
    instructions = list_of_recipes_2[recipe]["Instructions"]
    if isinstance(instructions, str):
        steps = instructions.split('. ')  # Assuming steps are separated by a period and a space
    else:
        steps = instructions  # Assuming it's already a list

    for j, step in enumerate(steps):
    # Process each step
        st.write(str(j+1)+"."+step)

    # st.write("For more details click the link below")
    # st.write(matching_recipes[recipe]["link"])

if "current_recipe" in st.session_state:
    show_recipe(st.session_state["current_recipe"])