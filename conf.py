# Configuration file for the Sphinx documentation builder.
#
# Full list of options can be found in the Sphinx documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys
from typing import Any, Dict


# -- Project information -----------------------------------------------------
#

project = "CV"
#copyright = "2020, Pradyun Gedam"
author = "Ruslan Kid"

# -- General configuration ---------------------------------------------------
#

extensions = []
templates_path = ["_templates"]

html_theme_path = ['cv_rtd/src/inspirid_sphinx_theme']
html_theme = "inspirid"
html_title = "CV"
html_logo = "logo.png"
language = "ru"

