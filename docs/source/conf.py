# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "summerschool-Jun2026-demo"
project_copyright = "2026, Su Sun, Richard H. West, Kyle Niemeyer, and Tyler Janoski"
author = "Su Sun, Richard H. West, Kyle Niemeyer, and Tyler Janoski"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",  # pull in docstrings
    "sphinx.ext.autosummary",  # summary tables
    "sphinx.ext.napoleon",  # understand NumPy / Google style docstrings
    "sphinx.ext.intersphinx",  # link to other projects' docs
    "sphinx.ext.mathjax",  # render LaTeX math
    "myst_nb",  # Markdown + Jupyter notebooks as pages
]

# Generate stub pages for entries listed in autosummary directives.
autosummary_generate = True

templates_path = ["_templates"]
exclude_patterns: list[str] = []

intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "numpy": ("https://numpy.org/doc/stable/", None),
    "pandas": ("https://pandas.pydata.org/pandas-docs/version/2.3", None),
}

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "alabaster"
html_static_path = ["_static"]
