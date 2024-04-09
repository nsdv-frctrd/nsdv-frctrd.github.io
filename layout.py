from jinja2 import Template
import json

# Load the HTML template
with open('template2.html') as file:
    template_content = file.read()

# Load the finance news from the JSON file
with open('data.json') as file:
    state_news = json.load(file)

# Create a Jinja2 template object
template = Template(template_content)

# Render the template with finance_news data
rendered_html = template.render(articles=state_news)

# Save the rendered HTML to a file
with open('right2.html', 'w') as file:
    file.write(rendered_html)

print("HTML file generated: right2.html")





with open('template3.html') as file:
    template_content = file.read()

# Load the finance news from the JSON file
with open('data.json') as file:
    state_news = json.load(file)

# Create a Jinja2 template object
template = Template(template_content)

# Render the template with finance_news data
rendered_html = template.render(articles=state_news)

# Save the rendered HTML to a file
with open('right3.html', 'w') as file:
    file.write(rendered_html)

print("HTML file generated: right3.html")
