import yaml
from jinja2 import Environment, BaseLoader
from flask import Flask
from werkzeug.serving import run_simple

app = Flask(__name__)

def load_config(path):
    with open(path) as f:
        return yaml.safe_load(f)

def render_template(template_str, context):
    env = Environment(loader=BaseLoader(), autoescape=True)
    template = env.from_string(template_str)
    return template.render(context)

@app.route("/")
def index():
    return "Hello World"

if __name__ == "__main__":
    config = load_config("config.yaml")
    app.run(host="127.0.0.1", port=5000)
