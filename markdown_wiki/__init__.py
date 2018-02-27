"""
Flask app initialization and configuration
"""
import os

from flask import Flask
from flask_flatpages import FlatPages, pygments_style_defs

from markdown_wiki.config import BASE_DIR, MARKDOWN_WIKI_TEMPLATE
from markdown_wiki.config import MARKDOWN_WIKI_RENDER_CODE_STYLE


pygments_style_defs(style=MARKDOWN_WIKI_RENDER_CODE_STYLE)

MarkdownWiki = Flask(__name__, template_folder=os.path.join('templates', MARKDOWN_WIKI_TEMPLATE))
MarkdownWiki.config.from_object('markdown_wiki.extend.Config')

PAGES = FlatPages(MarkdownWiki)

from markdown_wiki import routes, config
