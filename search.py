import streamlit as st
import recipes
st.set_page_config(page_icon="🔍",initial_sidebar_state="collapsed")
hide_streamlit_style = """
    <style>
    [data-testid="stSidebarCollapsedControl"]  {
        display: none;
    }
    </style>
    """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
#for NER replace recipe generator 2 with recipe generator
#main function of search page
def search(ingredients):
    matching_recipes=recipes.recipe_generator_2(ingredients)
    if not matching_recipes:
        st.header("Sorry,no recipes found with the given ingredients!")
        return
    columns=st.columns(3,vertical_alignment="top")
    for i,recipe in enumerate(matching_recipes.values()):
        # with st.container():
        with columns[i%3]:
            ingredient_list=""
            for item in recipe["Ingredients"]:
                ingredient_list+=item+","
            ingredient_list=ingredient_list[:-1]
            st.markdown("""
    <style>
    .truncate {
        display: -webkit-box;
        -webkit-line-clamp: 1;
        -webkit-box-orient: vertical;  
        overflow: hidden;
        text-overflow: ellipsis;
    }
    .truncate:hover::after {
        content: attr(title);
        position: absolute;
        background: #fff;
        border: 1px solid #ccc;
        padding: 10px;
        width: max-content;
        max-width: 400px;
        white-space: pre-wrap; 
        z-index: 1000;
    }
    </style>
    """, unsafe_allow_html=True)
            st.markdown("""
        <style>
        .truncate-subheader h5 {
            display: -webkit-box;
            -webkit-line-clamp: 1;
            -webkit-box-orient: vertical;  
            overflow: hidden;
            text-overflow: ellipsis;
            line-height:2em;
            max-height:2em;
        }
        .truncate-subheader:hover::after {
        content: attr(title);
        position: absolute;
        background: #fff;
        border: 1px solid #ccc;
        padding: 10px;
        width: max-content;
        max-width: 400px;
        white-space: pre-wrap; 
        z-index: 1000;
    }
        </style>
        """, unsafe_allow_html=True)
            st.markdown(f'<div class="truncate-subheader" title="{recipe["Title"]}"><h5>{recipe["Title"]}</h5></div>',unsafe_allow_html=True) 
            st.markdown(f'<div class="truncate" >{ingredient_list}</div>', unsafe_allow_html=True)
            st.image("C:\\Users\Dhruv\\recipes_generator\\Food Images\\"+recipe["Image_Name"]+".jpg",use_column_width="always")
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
            if st.button("See this",key=str(i)+recipe["Title"],use_container_width=True):
                st.session_state["current_recipe"]=recipe
                st.switch_page("pages/recipe_show.py")
            st.markdown("---")


if "ingredients" in st.session_state:
    search(st.session_state["ingredients"])
