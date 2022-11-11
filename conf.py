# Configuration file for the Sphinx documentation builder.
#
# Full list of options can be found in the Sphinx documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys
from typing import Any, Dict

# add the demo python code to the path, so that it can be used to demonstrate
# source links
sys.path.append(os.path.abspath("./kitchen-sink/demo_py"))

# -- Project information -----------------------------------------------------
#

project = "CV"
#copyright = "2020, Pradyun Gedam"
author = "Ruslan Kid"

# -- General configuration ---------------------------------------------------
#

extensions = [
    # Sphinx's own extensions
    "sphinx.ext.autodoc",
    "sphinx.ext.extlinks",
    "sphinx.ext.intersphinx",
    "sphinx.ext.mathjax",
    "sphinx.ext.todo",
    "sphinx.ext.viewcode",
    # Our custom extension, only meant for Furo's own documentation.
    #"furo.sphinxext",
    # External stuff
    #"sphinx_design",
    #"sphinx_inline_tabs",
]
templates_path = ["_templates"]


html_theme = "furo"
html_title = "CV"
html_logo = "logo.png"
language = "ru"

