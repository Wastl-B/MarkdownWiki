from flask_flatpages import pygments_style_defs

from markdown_wiki.config import *


class Config(object):
    """
    To configure the flask application and translate some values
    """
    BASE_DIR = BASE_DIR
    SECRET_KEY = SECRET_KEY
    FLATPAGES_EXTENSION = MARKDOWN_WIKI_FILE_EXTENSION
    FLATPAGES_ROOT = MARKDOWN_WIKI_ROOT
    FLATPAGES_MARKDOWN_EXTENSIONS = MARKDOWN_WIKI_RENDER_EXTENSIONS
    
