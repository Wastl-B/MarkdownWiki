"""
Flask routes
"""
import markdown

from flask import render_template, render_template_string, redirect, url_for, g

from flask_flatpages import pygments_style_defs

from markdown_wiki import MarkdownWiki, PAGES, forms

from markdown_wiki.config import MARKDOWN_WIKI_RENDER_EXTENSIONS
from markdown_wiki.utils import search_files, get_menu, get_extra_pages, MARKDOWN_WIKI_CONTEXT
from markdown_wiki.config import MARKDOWN_WIKI_RENDER_CODE_STYLE


@MarkdownWiki.route('/')
def index():
    """
    basic index route
    :return: redirect to page route for index/home file
    """
    return page('excludes/home')


@MarkdownWiki.route('/<path:path>/')
def page(path):
    """
    route for markdown 'Pages'
    :param path: path to file, relative from FLATPAGES_ROOT
    :return: rendered template
    """
    menu_entries = get_menu()
    extra_pages = get_extra_pages()
    _page = PAGES.get_or_404(path)
    return render_template('index.html', 
                            page=_page, 
                            menu_entries=menu_entries,
                            extra_pages=extra_pages, 
                            context=MARKDOWN_WIKI_CONTEXT)


def custom_md_renderer(text):
    """
    custom markdown render function to add some nice extensions for code blocks
    :param text: markdown string
    :return: rendered markdown
    """
    rendered_body = render_template_string(text)
    pygmented_body = markdown.markdown(rendered_body, extensions=MARKDOWN_WIKI_RENDER_EXTENSIONS)
    return pygmented_body


MarkdownWiki.config.update({'FLATPAGES_HTML_RENDERER': custom_md_renderer})


@MarkdownWiki.route('/search', methods=['POST'])
def search():
    """
    search route with form validation
    :return: redirect to searchresults with query
    """
    if not g.search_form.validate_on_submit():
        return redirect(url_for('index'))
    return redirect(url_for('search_results', query=g.search_form.search.data))


@MarkdownWiki.route('/search_results/<query>')
def search_results(query):
    """
    route for search results where the search happens
    :param query: query to search for
    :return: rendered template with results
    """
    results = search_files(query)
    menu_entries = get_menu()
    extra_pages = get_extra_pages()
    return render_template('search_results.html',
                           query=query,
                           results=results,
                           menu_entries=menu_entries,
                           extra_pages=extra_pages,
                           context=MARKDOWN_WIKI_CONTEXT,
                           title='Searchresults')


@MarkdownWiki.before_request
def before_request():
    """
    instantiates a search form in Flask's g(lobal)
    """
    g.search_form = forms.SearchForm()


@MarkdownWiki.route('/pygments.css')
def pygments_css():
    """
    route for pygments stylesheet
    :return: pygments.css
    """
    return pygments_style_defs(MARKDOWN_WIKI_RENDER_CODE_STYLE), 200, {'Content-Type': 'text/css'}


@MarkdownWiki.errorhandler(404)
def not_found_error(error):
    """
    404 error route
    :param error: error description
    :return: redirect to page route for 404
    """
    return page('excludes/404'), 404


@MarkdownWiki.errorhandler(500)
def unexpected_error(error):
    """
    500 error route
    :param error: error description
    :return: redirect to page route for 500
    """
    return page('excludes/404'), 500
