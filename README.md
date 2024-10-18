INTRODUCTION:
my_first_project is a project which gives the user with the recipes that they can make with the ingredients they have.
In order to complete this task we have a dataset of all the recipes in a csv file which we process through pandas and convert it to a format where we can use it to match with the ingredients entered by the user
The processing of the csv file into suitable datatype and matching the ingredients of it is done in the recipes.py file.It is to be noted that a recipe cant be made with all the ingredients the user has entered so we return the recipes in an order such that the recipe which requires least number of extra ingredients is shown first and also it is made sure that all  the ingredients entered by the user are used in the returned recipe
After the program to match the recipes is created ,we create a home page in our app .Here we take the ingredients from the user and redirect them to the search page.
Now,on the search page we import the logic to match the user ingredients and our dataset and after matching them we return the user with names and ingredients of all the recipes which can be made with the given ingredients
Also, we provide a button with each returned recipe to see the instructions to how to make a recipe.This button redirects the user to the recipe_show page when we list out the process of making it.
All the pages of our app are created using "streamlit" library
