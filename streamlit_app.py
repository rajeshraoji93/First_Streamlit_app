import streamlit
import pandas as pd

streamlit.title("My parents New healthy diner")
streamlit.header("Breakfast Menu")
streamlit.text("Eggs")
streamlit.text("Idli")
streamlit.text("Dosa")
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')


# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page.
streamlit.dataframe(fruits_to_show)

#api header
streamlit.header("Fruityvice Fruit Advice!")
#api request response
import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/kiwi")
# write your own comment -what does the next line do? 
fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
streamlit.dataframe(fruityvice_normalized)

