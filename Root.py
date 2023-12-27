"""
Streamlit Cheat Sheet

App to summarise streamlit docs v1.25.0

There is also an accompanying png and pdf version

https://github.com/daniellewisDL/streamlit-cheat-sheet

v1.25.0
20 August 2023

Author:
    @daniellewisDL : https://github.com/daniellewisDL

Contributors:
    @arnaudmiribel : https://github.com/arnaudmiribel
    @akrolsmir : https://github.com/akrolsmir
    @nathancarter : https://github.com/nathancarter

"""

import streamlit as st
from pathlib import Path
import base64
import yaml, os
from streamlit_modal import Modal

# Initial page config

st.set_page_config(
     page_title='Holy Cheat Factory',
     layout="wide",
     initial_sidebar_state="expanded",
)

def main():
    welcome()
    add_code()

    return None

# Thanks to streamlitopedia for the following code snippet

def img_to_bytes(img_path):
    img_bytes = Path(img_path).read_bytes()
    encoded = base64.b64encode(img_bytes).decode()
    return encoded

# sidebar

def cs_sidebar():

    st.sidebar.markdown('''[<img src='data:image/png;base64,{}' class='img-fluid' width=32 height=32>](https://streamlit.io/)'''.format(img_to_bytes("logomark_website.png")), unsafe_allow_html=True)
    st.sidebar.header('Holy cheat sheet')
    st.sidebar.markdown('__Install and import__')

    # Examples
    st.sidebar.code('$ pip install streamlit')

    st.sidebar.code('''
# Import convention
>>> import streamlit as st
''')

    return None

##########################
# Add cheat sheet tip 
##########################

def welcome():
    st.header("Welcome 🚀  to Cheat Factory, Cheater .. 👽")
    st.subheader("Have you cheated today? 😈 ")
    

def add_code():
    if 'add' not in st.session_state:
        st.session_state.add = False
    if 'cheat' not in st.session_state:
        st.session_state.cheat = False
    add_cheat_container = st.container()
    col1, col2= add_cheat_container.columns([2,2])
    col1.markdown("##### Hide your cheat hacks for another day 🤭")
    add_btn = col2.button("Cheat 🤫", type="primary")
    if add_btn:
        st.session_state.add = True
    if st.session_state.add:
        cheat_page = col1.selectbox("Select cheat topic", options=[page.split(".")[0].lower() for page in os.listdir("./pages")])
        cheat_subheader = col1.text_input('Cheat title')
        cheat_code = col1.text_area('The Holy Cheat Code')
        cheat_submit = col1.button('Save cheat for another day', type="primary")
        if cheat_submit:
            st.session_state.cheat = True
        if st.session_state.cheat:
            if (cheat_subheader !="") and (cheat_code !=""):
                try:
                    save_cheat(cheat_page, cheat_subheader, cheat_code)
                    col1.success("Cheat saved")
                except Exception as e:
                    st.write(e)
                    col1.error("Cheat again?!")
            else:
                col1.error("Empty cheat! Cheat again?!")
            st.write("Cheat Page:", cheat_page)
            st.write("Cheat Subheader:", cheat_subheader)
            st.write("Cheat Code:", cheat_code)
                
# Function to load YAML content from file
def load_yaml(file_path):
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)

# Function to add a new code snippet to the YAML content
def add_snippet(data, category, title, code):
    if category in data['categories']:
        data['categories'][category].append({'title': title, 'code': code})
    else:
        data['categories'][category] = [{'title': title, 'code': code}]

    return data

def save_cheat(cheat_page, cheat_subheader, cheat_content):
    data = load_yaml("CHEATS/data.yaml")  
    updated_data = add_snippet(data, cheat_page, cheat_subheader, cheat_content)
    with open("CHEATS/data.yaml", 'w+') as file:
        yaml.dump(updated_data, file)

if __name__ == '__main__':
    main()
