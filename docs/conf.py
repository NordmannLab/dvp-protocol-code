"""Sphinx configuration for the dvp-protocol-code documentation."""

# -- Project information -----------------------------------------------------

project = "dvp-protocol-code"
author = "Mann Labs"
copyright = "2025, Mann Labs"

# -- General configuration ---------------------------------------------------

extensions = [
    "myst_nb",  # MyST Markdown + Jupyter notebook support
    "sphinx_copybutton",
    "sphinx_design",
]

# MyST Markdown is the only authoring format; notebooks are rendered via myst-nb.
source_suffix = {
    ".md": "myst-nb",
    ".ipynb": "myst-nb",
}

master_doc = "index"

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store", "**.ipynb_checkpoints"]

# -- MyST / notebook execution -----------------------------------------------

# Notebooks depend on large data and GPU-heavy libraries, so they are embedded
# with their stored outputs rather than re-executed at build time.
nb_execution_mode = "off"

myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "dollarmath",
    "fieldlist",
    "linkify",
    "substitution",
    "tasklist",
]

myst_heading_anchors = 3

# -- Options for HTML output -------------------------------------------------

html_theme = "shibuya"

html_title = "dvp-protocol-code"

html_theme_options = {
    "github_url": "https://github.com/MannLabs/dvp-protocol-code",
    "nav_links": [
        {"title": "Tutorials", "url": "tutorials/index"},
    ],
}

html_static_path = ["_static"]
