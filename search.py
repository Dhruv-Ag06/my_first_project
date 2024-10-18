import streamlit as st
import recipes
st.set_page_config(page_icon="🔍",initial_sidebar_state="collapsed")

#for NER replace recipe generator 2 with recipe generator
#main function of search page
def search(ingredients):
    matching_recipes=recipes.recipe_generator_2(ingredients)
    if not matching_recipes:
        st.header("Sorry,no recipes found with the given ingredients!")
        return
    columns=st.columns(3,vertical_alignment="top")
    for i,recipe in enumerate(matching_recipes):
        # with st.container():
        with columns[i%3]:
            ingredient_list=""
            for item in matching_recipes[recipe]["Ingredients"]:
                ingredient_list+=item+","
            st.markdown("""
    <style>
    .truncate {
        display: -webkit-box;
        -webkit-line-clamp: 1;
        -webkit-box-orient: vertical;  
        overflow: hidden;
        text-overflow: ellipsis;
    }
    </style>
    """, unsafe_allow_html=True)
            st.markdown("""
        <style>
        .truncate-subheader h3 {
            display: -webkit-box;
            -webkit-line-clamp: 1;
            -webkit-box-orient: vertical;  
            overflow: hidden;
            text-overflow: ellipsis;
            line-height:2em;
            max-height:2em;
        }
        </style>
        """, unsafe_allow_html=True)
            st.markdown(f'<div class="truncate-subheader"><h3>{matching_recipes[recipe]["Title"]}</h3></div>',unsafe_allow_html=True) 
            st.markdown(f'<div class="truncate">{ingredient_list}</div>', unsafe_allow_html=True)
            st.image("C:\\Users\Dhruv\\recipes_generator\\Food Images\\"+matching_recipes[recipe]["Image_Name"]+".jpg")
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
            if st.button("See this",key=str(i)+matching_recipes[recipe]["Title"],use_container_width=True):
                st.session_state["current_recipe"]=recipe
                st.switch_page("pages/recipe_show.py")
            st.markdown("---")

if st.session_state["ingredients"]:
    search(st.session_state["ingredients"])
