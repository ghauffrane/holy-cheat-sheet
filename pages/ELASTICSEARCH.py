import streamlit as st
import yaml

# Function to load YAML content from file
def load_yaml(file_path):
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)

def filter_by_category(data, category):
    return data['categories'].get(category, [])

def make_page():
    col1, col2, col3 = st.columns(3)
    yaml_file = 'CHEATS/data.yaml'
    yaml_content = load_yaml(yaml_file)

    # Filter code snippets by category or title
    aws_snippets = filter_by_category(yaml_content, 'elasticsearch')
    
    for index, snippet in enumerate(aws_snippets):
        if index % 3 == 0:
            container = col1
        elif index % 3 == 1:
            container = col2
        else:
            container = col3

        container.subheader(snippet['title'])
        container.code(snippet['code'])

make_page()
        