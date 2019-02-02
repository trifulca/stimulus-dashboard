import os
from jinja2 import Environment, FileSystemLoader
from sanic.response import html

TEMPLATES_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "templates")

def render(template, **kw):
    j2_env = Environment(loader=FileSystemLoader(TEMPLATES_DIR), trim_blocks=True)
    data = j2_env.get_template(template).render(**kw)
    return html(data)
