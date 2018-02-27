"""
here is space for some little helpers like the search function and the menu generators
"""
from markdown_wiki.config import MARKDOWN_WIKI_EXCLUDED_FOLDERS
from markdown_wiki.config import MARKDOWN_WIKI_EXTRAPAGES_FOLDER
from markdown_wiki.config import MARKDOWN_WIKI_SEARCH_EXCLUDE_STRING
from markdown_wiki.config import MARKDOWN_WIKI_CONTENTMENU_ALPHABETIC
from markdown_wiki.config import MARKDOWN_WIKI_EXTRTAMENU_ALPHABETIC
from markdown_wiki.config import MARKDOWN_WIKI_CONTENTMENU_ALTORDER
from markdown_wiki.config import MARKDOWN_WIKI_EXTRTAMENU_ALTORDER
from markdown_wiki.config import MARKDOWN_WIKI_BRAND
from markdown_wiki.config import MARKDOWN_WIKI_TITLE
from markdown_wiki.config import MARKDOWN_WIKI_EXTERNAL_LINK

from markdown_wiki import PAGES


MARKDOWN_WIKI_CONTEXT = {
    'BRAND': MARKDOWN_WIKI_BRAND, 
    'TITLE': MARKDOWN_WIKI_TITLE,
    'EXT_LINK': MARKDOWN_WIKI_EXTERNAL_LINK
    }


def get_menu(*arg):
    """
    gathers all markdown files, which are not in 'FLATPAGES_EXCLUDE_FOLDERS' and 'MARKDOWN_WIKI_EXTRAPAGES_FOLDER' 
    for the main content menu generation, orderd based on 'MARKDOWN_WIKI_CONTENTMENU_ALPHABETIC'
    :return: pages for the menu
    """
    menu_entries = [p for p in PAGES if not any(exclude in p.path for exclude in MARKDOWN_WIKI_EXCLUDED_FOLDERS + MARKDOWN_WIKI_EXTRAPAGES_FOLDER)]
    if MARKDOWN_WIKI_CONTENTMENU_ALPHABETIC:
        return sorted(menu_entries, key=lambda p: p.path)
    else:
        return sorted(menu_entries, key=lambda p: p[MARKDOWN_WIKI_CONTENTMENU_ALTORDER])

def get_extra_pages():
    """
    gathers all markdown files, which are not in 'FLATPAGES_EXCLUDE_FOLDERS' 
    for the extra pages menu generation, orderd based on 'MARKDOWN_WIKI_EXTRTAMENU_ALPHABETIC'
    :return: pages for the menu
    """
    pages = [p for p in PAGES if any(exclude in p.path for exclude in MARKDOWN_WIKI_EXTRAPAGES_FOLDER)]
    
    if MARKDOWN_WIKI_EXTRTAMENU_ALPHABETIC:
        return sorted(pages, key=lambda p: p.path)
    else:
        return sorted(pages, key=lambda p: p[MARKDOWN_WIKI_EXTRTAMENU_ALTORDER])


def search_files(query):
    """
    search function to search in ALL pages in FLATPAGES_ROOT
    returns a dictionary with the title from metadata and the line where it was found
    :param query: query to search for
    :return: results as dictionary
    """
    results = list()
    for p in PAGES:
        for line in p.body.splitlines():
            if query.lower() in line.lower() and '```' not in line:
                for char in MARKDOWN_WIKI_SEARCH_EXCLUDE_STRING:
                    line = line.replace(char, '')
                result = {'TITLE': p['title'], 'LINE': line, 'PATH': p.path}
                results.append(result) 
    return results
