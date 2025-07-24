# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = u'Docs'
copyright = u'2025, J-Sai'
author = u'J-Sai'

version = u'0.1'

release = u'0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.todo', 'sphinx.ext.imgmath']

templates_path = [u'_templates']

source_suffix = '.rst'

source_encoding = u'utf-8-sig'

master_doc = u'index'

copyright = u'1994-%Y, Jin Sai'

exclude_patterns = []

language = u'zh_CN'

pygments_style = 'sphinx'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = u'sphinx_rtd_theme'

html_favicon = "images/favicon.ico"

html_use_index = True

htmlhelp_basename = 'Docs'

latex_paper_size = u'a4'

latex_font_size = u'10pt'

latex_documents = []

latex_use_parts = False