import streamlit
import pandas as pd
import snowflake.connector
import requests
from urllib.error import URLError

streamlit.title("My parents New healthy diner")
streamlit.header("Breakfast Menu")
streamlit.text("Eggs")
streamlit.text("Idli")
streamlit.text("Dosa")
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')


# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page.
streamlit.dataframe(fruits_to_show)

#api header
streamlit.header("Fruityvice Fruit Advice!")
def get_fruityvice_data():
  streamlit.write('The user entered ', fruit_choice)
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+ fruit_choice)
    fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
    return streamlit.dataframe(fruityvice_normalized)

try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
    streamlit.error('Please select a fruit to get information')
  else:
    get_fruityvice_data(fruit_choice)
except URLError as e:
  streamlit.error()

streamlit.stop()
# write your own comment - what does this do?

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select * from pc_rivery_db.public.fruit_load_list")
my_data_row = my_cur.fetchall()
streamlit.header("The fruit list contains:")
streamlit.dataframe(my_data_row)

fruit_add = streamlit.text_input('What fruit would you like to add?','Jackfruit')
streamlit.write('The user entered ', fruit_add)

