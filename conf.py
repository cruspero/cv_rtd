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
html_static_path = ['_static', 'img']
html_js_files = [
    'https://cdn.jsdelivr.net/npm/chart.js'
]
extensions = []
templates_path = ["_templates"]
html_css_files = [
    'css/theme_overrides.css',
    'css/style.css',
    'css/animate.css',
    'https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css'
]
html_favicon = 'favico.png'
html_theme = "sphinx_rtd_theme"
html_theme_options = {
    'logo_only': True,
    'display_version': True,
    'prev_next_buttons_location': 'bottom',
    'style_external_links': True,
    'style_nav_header_background': '#343131',
    # Toc options
    'collapse_navigation': True,
    'sticky_navigation': True,
    'includehidden': True,
    'titles_only': False
}
html_title = "CV"
html_logo = "logo.png"
language = "ru"

