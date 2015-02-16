"""
Configuration file required for all new Toyz
"""
from __future__ import division,print_function
import os

root = os.path.abspath(os.path.join(os.path.dirname(__file__),os.pardir))

# All toyz are required to have lists containing static paths and template paths
static_paths = [os.path.join(root, 'static')]
template_paths = [os.path.join(root, 'templates')]

workspace_tiles = {
    'template_tile': {
        'name': 'Template Tile', # Name of the tile to show up in the workspace tiles list
        'namespace': 'Toyz.Template', # Namespace of the template (to check for dependencies)
        'url': 'toyz/static/toyz_template/template.js' # Javascript file to load
    }
}