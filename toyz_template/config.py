"""
Configuration file required for all new Toyz
"""
from __future__ import division,print_function
import os

##################
# Custom Methods #
##################

# Root directory of the config.py file
root = os.path.abspath(os.path.join(os.path.dirname(__file__)))

# Example function illustrating how to render tornado.RequestHandler templates with
# custom parameters
def gen_text(params):
    kwargs = {
        'mytext': "{0} requested '{1}'".format(params['handler'].get_user_id(), params['path'])
    }
    params['handler'].render(params['filename'], **kwargs)

####################
# Required methods #
####################

# List of static and template paths
static_paths = [os.path.join(root, 'static')]
template_paths = [os.path.join(root, 'templates')]

# Tiles added by your toy
workspace_tiles = {
    'template_tile': {
        'name': 'Template Tile', # Name of the tile to show up in the workspace tiles list
        'namespace': 'Toyz.Template', # Namespace of the template (to check for dependencies)
        'url': '/toyz/static/toyz_template/template.js' # Javascript file to load
    }
}

# Urls to add to the 'Toyz' tab on the home page. The keys are the text that will appear and the
# values are the urls
toyz_urls = {
    'Template': "/toyz/templates/toyz_template/template.html"
}

# If any tornado.RequestHandler templates have parameters, special functions to render
# the page must be defined here
render_functions = {
    "toyz_template/template.html": gen_text
}