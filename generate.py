import os
import json
from jinja2 import Environment, FileSystemLoader, select_autoescape

# Root directory
root = os.path.dirname(os.path.abspath(__file__)) 

# templates directory
template_dir = os.path.join(root, 'templates')

# create jinja environment
env = Environment(
    loader = FileSystemLoader(template_dir),
    autoescape = select_autoescape()
)

# get the layout.html template
template = env.get_template('layout.html')


# get json data
with open('data.json', 'r') as data_file:
    data = json.loads(data_file.read())

# Output layout
filename = os.path.join(root, 'result', 'output_layout.html')

# write the output to output_layout.html file
with open(filename, "w") as file:
    file.write(
        template.render(**data)
    )
