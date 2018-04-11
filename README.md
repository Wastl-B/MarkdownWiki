## _This page, as well as the project, are in development..._

**MarkdownWiki** aims to be a quick and easy solution if you need to host some information like a documentation or a small wiki
and want to maintain the content as markdown files. The Website will be generated, based on your Markdown files and subfolders.

**MarkdownWiki** is build with [Flask](http://flask.pocoo.org/), [Flask-FlatPages](http://flask-flatpages.readthedocs.io/en/latest/)
& [Bootstrap 4](http://getbootstrap.com/docs/).

I have also prepared this repo including some placeholder Markdowns as [Demo](https://markdownwiki.lymbycfyk.de).

# Table of content

* [Requirements](#requirements)
* [Installation](#installation)
* [Configuration](#configuration)
  * [MarkdownWiki config](#markdownwiki-config)
  * [Logos](#logos)
* [Markdowns](#markdowns)
  * [Folder structure](#folder-structure)
  * [File layout](#file-layout)
  * [Links](#links)
* [Starting the development server](#starting-the-development-server)
* [Style cutomization](#style-cutomization)
* [Custom templates](#custom-templates)
  * [Menus](#menus)
  * [Search](#search)
  * [Tips](#tips)

# Requirements

* Python3
* pip
* virtualenv
* nodejs and yarn (or npm) for style development

# Installation

```Bash
git clone git@github.com:lymbycfyk/MarkdownWiki.git
cd MarkdownWiki
virtualenv .venv
.venv/bin/pip install -r requirements.txt
```

# Configuration

## MarkdownWiki _config_

> `markdown_wiki/config.py`

|                                       |                                                                                                                                                      |
| ------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| `SECRET_KEY`                          | to generate secrets like tokens to allow communication between homepage and user (Search). Change here or in production set as environment variable. |
| `MARKDOWN_WIKI_ROOT`                  | the root markdown directory. You can keep them in the app folder, or anywhere else, just edit to your needs.                                         |
| `MARKDOWN_WIKI_FILE_EXTENSION`        | file extension. Change it, only if you use another extension that `*.md`.                                                                            |
| `MARKDOWN_WIKI_EXCLUDED_FOLDERS`      | subfolders of `MARKDOWN_WIKI_ROOT`, which should be excluded in the main (content) menu.                                                             |
| `MARKDOWN_WIKI_EXTRAPAGES_FOLDER`     | subfolder of `MARKDOWN_WIKI_ROOT`, where you can place extra pages like impressum etc.                                                               |
| `MARKDOWN_WIKI_CONTENTMENU_ORDER`     | string, key from _metadata_ for the menu order                                                                                                       |
| `MARKDOWN_WIKI_EXTRTAMENU_ORDER`      | string, key from _metadata_ for the menu order                                                                                                       |
| `MARKDOWN_WIKI_SEARCH_EXCLUDE_STRING` | chars, which should be excluded in search, due to text search. Read [Markdown File layout](#file-layout) for more information                        |
| `MARKDOWN_WIKI_BRAND`                 | string for navbar title nexto the logo.                                                                                                              |
| `MARKDOWN_WIKI_TITLE`                 | string for an alternative title, will be shown on large screens as top menu entry for 'home', on smaller screens in navbar as alternative title.     |
| `MARKDOWN_WIKI_EXTERNAL_LINK`         | Link for the navbar brand.                                                                                                                           |
| `MARKDOWN_WIKI_TEMPLATE`              | template to use (as subfolder in `templates/`).                                                                                                      |
| `MARKDOWN_WIKI_RENDER_EXTENSIONS`     | default values are for nice code blocks, and headerids.                                                                                              |
| `MARKDOWN_WIKI_RENDER_CODE_STYLE`     | style for code blocks, based an well known [themes](https://help.farbox.com/pygments.html)                                                           |

## Logos

In `markdown_wiki/static/img/` are two placeholder by [Octicons](https://octicons.github.com/). You can simply replace them but
should rename them to the default names or change the filenames in the the template files `base.html` and `includes/topbar.html`.

# Markdowns

## Folder structure

Default:

* the main content belongs in `MARKDOWN_WIKI_ROOT`.
* `excludes/` holds the "Home"-page and the error pages.
* `includes/` is for examle a possibility to link to a page, which wont be shown in any menu. Rename it if you like, because the `URL` will be based on the foldername.
* `pages/` is the space for pages for the extra menu (seperated menu in smaller views). Keep the `URL` in mind
* If you rename the folders oder add some more, add them to your `config.py`

## File layout

At the top of each file, we can add some **metadata** in yaml format and keep on free line to your markdown.
The `title` provides the page title, menue entry and heading in the template, `edited` generates
a _datetime_ object, so the syntax is very important, so it can be treated as a typical Python _datetime_
object in templates like `{{ page.edited.strftime('%b %d %Y') }}`, which will result in `Feb 20 2018` .
The author or editor is of course the `by`. The `order` is a numerical value for a custom menu order.
You can add any meta value you like and call it in a template or order them by it.

```yaml
title: Home
edited: 2018-02-20
by: John Doe
order: 100

# Welcome to this Wiki
...
```

For a safe search functionality, you should use the asterisks instead of underscores, to be able to exclude one character in the search

## Links

To link to another page you can use Markdown regular syntax

```Markdown
[Networking](/networking)
```

to excluded files

```Markdown
[__SOLUTION__](/includes/solution)
```

or to a heading on the same page:

```Markdown
[Starting the development server](#starting-the-development-server)
```

But if you want to link to a file from the `static` folder,
like a picture for example, we mix both Markdown and Jinja

```Markdown
![picture]({{ url_for('static', filename='img/picture.png') }})
```

# Starting the development server

```Bash
./run_dev.py
# or
./run_dev.py -h  # for additional options
```

# Style cutomization

I chose bootstrap for the interface, but with some customized bootstrap variables and
compiled with my additional rules with gulp-sass. To do it also this way, you need nodejs and npm installed to run
the installation script:

```Bash
./install.py
# or if you use npm instead of yarn
./install.py --npm
```

In `markdown_wiki/static/src/scss` are the _\_variables.scss_ from **Bootstrap**'s sourcefiles and the _\_custom.scss_ with
our own rules. The _bootstrap-custom.scss_ contains only some imports and will be compiled to our customized bootstrap stylesheet:

```SCSS
@import '../node_modules/bootstrap/scss/_functions';    //< for some  nice function like lighten(), darken()
@import '_variables';                                   //< our customized variables
@import '../node_modules/bootstrap/scss/bootstrap';     //< boostrap from source
@import '_custom';                                      //< and at least, our own set of rules
```

to compile your changes, simply run the build script I made:

```Bash
./build.py # --npm if you use npm
# or to start the wathed mode
./build.py --watch
# or to minifiy the compiled css
./build.py --minify
```

# Custom templates

You need at least two template files. One main template for all the markdown pages and one for the search results.
Usually, each of these templates will be extenden by a third one, the **base** template.

Let's start with the base. It should hold the main design of the page, at least the `<html>...</html>`, `<head>...</head>` and `<body>...</body>` tag.
You should define the navigation the as well, because this template will extend all other templates and we mostly render **markdown**. The part where the requested
part should be renderd, becomes this `{% block content %}{% endblock %}` Jinja2-tag and every template that will be extended by this base will be build inside a Jinja-block

```Jinja
{% extends "base.html" %}
{% block content %}
    ... HTML here ...
{% endblock %}
```

and in our case the HTML, is in the `page` object, so we only have to add `{{ page.html|safe }}`.

To seperate a single component in your HTML code, you can create a new `html` file inside `templates/includes/`, to include it in any other template file. To do this, wrap the code in the new `html` file inside Jinja blocks:

```Jinja
{% block content %}
 ... HTML here ...
{% endblock %}
```

... and include it in the other file:

```Jinja
{% include 'includes/new_file.html %}
```

### Menus

To generate the main content menu, Jinja recieves a list called `menu_entries` which contains all objects that are intended to be an entry.
This means, we can iterate trough this list in a template like this:

```Jinja
{% for menu in menu_entries %}
    <li class="nav-item">
        <a class="nav-link" href="/{{ menu.path }}">
            {{ menu.title }}
        </a>
    </li>
{% endfor %}
```

for further pages, Jinja also recieves a list called `extra_pages` for additional pages and their menu entries, because the entries above will collapse to a dropdown on small devices. So iteate through that list, where ever you like, but better check if it exists:

```Jinja
{% if extra_pages %}
    {% for extra_page in extra_pages %}
        <a class="nav-link" href="{{ extra_page.path }}">
            {{ extra_page.title }}
        </a>
    {% endfor %}
{% endif %}
```

### Search

To include the searchbar:

```Jinja
<form>
    {{ g.search_form.hidden_tag() }}  {# hidden csrf token #}
    {{ g.search_form.search(class_="AnyClass", id="AnyID", placeholder="Search for ...", size=20) }}
    {{ g.search_form.submit(class_="AnyClass", id="AnyID", value="Search") }}
</form>
```

Last but not least, the search results template. You get a list with the results, where every result is represented as a dictionary.
So just iterate through the list like here:

```Jinja
{% for result in results %}
      <p>
        {{ result.LINE }}
      </p>
      <strong>gefunden in <a href="/{{ result.PATH }}">"{{ result.TITLE }}"</a></strong>
      <hr>
{% endfor %}
```

### Tips

as you can see, Jinja also allows conditional statements:

```Jinja
{% if page %}
    {{ page.title }}
{% elif title %}
    {{ title }}
{% else %}
    ...I have no title...
{% endif %}
```

The difference between `page.title` and `title` here is, that mostly the title of that page object is used, but
the search results aren't a rendered markdown, so the search route passes a `title`, which can be used for further _not_-md pages.
