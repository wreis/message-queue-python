# -*- coding: utf-8 -*-
import sys
import os

sys.path.insert(0, os.path.abspath('../../'))

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
    'sphinx.ext.coverage',
]

templates_path = ['_templates']
source_suffix = '.rst'
source_encoding = 'utf-8-sig'
master_doc = 'index'

project = u'message-queue'
copyright = u'2016, Ingresse'
author = u'Ingresse'

version = u'0.1.0'
release = u'0.1.0'
language = None

exclude_patterns = []
pygments_style = 'sphinx'
todo_include_todos = False


# -- Options for HTML output ----------------------------------------------
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
htmlhelp_basename = 'message-queuedoc'

# -- Options for LaTeX output ---------------------------------------------
latex_elements = {}

latex_documents = [
    (master_doc, 'message-queue.tex', u'message-queue Documentation',
     u'Ingresse', 'manual'),
]

# -- Options for manual page output ---------------------------------------
man_pages = [
    (master_doc, 'message-queue', u'message-queue Documentation',
     [author], 1)
]

# -- Options for Texinfo output -------------------------------------------
texinfo_documents = [
    (master_doc, 'message-queue', u'message-queue Documentation',
     author, 'message-queue', 'Message Queue',
     'Miscellaneous'),
]

intersphinx_mapping = {'https://docs.python.org/': None}

