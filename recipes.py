import pandas as pd

# Load the datasets
 
df = pd.read_csv("RecipeNLG_dataset.csv", nrows=35000)
df2=pd.read_csv("Food Ingredients and Recipe Dataset with Image Name Mapping.csv")

# Drop the first column and set 'title' as the index
df = df.iloc[:,1:]
df2 = df2.iloc[:,1:]

# Convert the dataframe to a list of dictionaries
df = df.to_dict(orient="records")
df2=df2.to_dict(orient="records")

# Initialize an empty list to store recipes
list_of_recipes = {}

# Process each recipe in the dataframes
suggestions=set()
for recipe in df:
    recipe["ingredients"] = set(eval(recipe["ingredients"]))
    if len(recipe["ingredients"])>20:
        continue
    recipe["NER"] = set(eval(recipe["NER"].lower()))
    for ingredient in recipe["NER"]:
        suggestions.add(ingredient)
    list_of_recipes[recipe["title"]]=recipe

def recipe_generator(user_input):
    # Convert user input to a set of ingredients
    user_input = set(user_input)
    
    # Initialize an empty list to store matching recipes
    matching_recipes = {}

    # Find recipes that match the user input
    for k in list_of_recipes:
        if user_input.issubset(list_of_recipes[k]["NER"]):
            matching_recipes[k]=list_of_recipes[k]

    # Sort the matching recipes by the number of named entities (NER)
    matching_recipes = dict(sorted(matching_recipes.items(), key=lambda x: len(x[1]["NER"])))
    
    # Return the titles of the matching recipes
    return matching_recipes


list_of_recipes_2={}
for recipe in df2: 
    recipe["Ingredients"] = eval(recipe["Ingredients"].lower())
    if len(recipe["Ingredients"])>=20 or len(recipe["Ingredients"])<=1 or recipe["Image_Name"]=="#NAME?":
        continue
    list_of_recipes_2[recipe["Title"]]=recipe


def recipe_generator_2(user_input):
    user_input=user_input.lower().split(",")
    matching_recipes = {}
    for k in list_of_recipes_2:
        if all(any(str1 in str2 for str2 in list_of_recipes_2[k]["Ingredients"]) for str1 in user_input):
            matching_recipes[k]=list_of_recipes_2[k]
    matching_recipes = dict(sorted(matching_recipes.items(), key=lambda x: len(x[1]["Ingredients"])))
    return matching_recipes

