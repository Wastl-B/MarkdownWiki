"""
config file for MarkdownWiki
"""
import os


BASE_DIR = os.path.abspath(os.path.dirname(__file__))

SECRET_KEY = os.environ.get('SECRET_KEY') or '5227990dfcd6936148c061083398a3ffb813ba65'

MARKDOWN_WIKI_FILE_EXTENSION = '.md'
MARKDOWN_WIKI_ROOT = os.path.join(BASE_DIR, 'markdowns')
MARKDOWN_WIKI_RENDER_EXTENSIONS = ['codehilite', 'fenced_code', 'headerid']
MARKDOWN_WIKI_RENDER_CODE_STYLE = 'monokai'
MARKDOWN_WIKI_EXCLUDED_FOLDERS = ['includes/', 'excludes/']
MARKDOWN_WIKI_EXTRAPAGES_FOLDER = ['pages/']
MARKDOWN_WIKI_CONTENTMENU_ALPHABETIC = False
MARKDOWN_WIKI_CONTENTMENU_ALTORDER = 'order'
MARKDOWN_WIKI_EXTRTAMENU_ALPHABETIC = True
MARKDOWN_WIKI_EXTRTAMENU_ALTORDER = 'order'
MARKDOWN_WIKI_SEARCH_EXCLUDE_STRING = '#_*'
MARKDOWN_WIKI_BRAND = 'MarkdownWiki'
MARKDOWN_WIKI_TITLE = 'Example Documentation'
MARKDOWN_WIKI_EXTERNAL_LINK = 'https://github.com/lymbycfyk/MarkdownWiki'
MARKDOWN_WIKI_TEMPLATE = 'ChocolateForrest'
