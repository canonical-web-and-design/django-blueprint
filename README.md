Static Django website blueprint
===

A stripped-down blueprint Django project to serving static templates directly.
It is intented as a basis for the Ubuntu design team's informational sites.

Much of Django's dynamic functionality (e.g. sessions, any database interation)
has been removed. URLs map directly to template locations, so creating a new
web page is as simple as creating a new template file.

Basic usage
---

Just clone the project and run the server:

``` bash
git clone https://github.com/ubuntudesign/static-django-blueprint.git
static-django-blueprint
./run     # Download containers, run the dev server and watch for CSS changes
```

Now visit <http://0.0.0.0:8090>.

### Options

You can customise the way the server is run directly in a few ways:

``` bash
./run --port 8111          # Run on a custom port
./run --db                 # Run with a database attached
./run --db server --watch  # Run with a database attached, watching for CSS changes (same as above)
./run server               # Run the server without watching for CSS changes
```

Customising your project
---

This project is intended to be forked as the basis for a new project, which
can then be customised as follows:

### Devrun environment settings

You should change the defaults for how `./run` behaves
in the [.env](.env) file, e.g.:

``` bash
PORT=8111                 # Run the server on local port 8111
DJANGO_DEBUG=false        # Turn off Django's DEBUG mode
DEFAULT_COMMAND="server"  # Override default command (what happens on `./run`)
DB=true                   # Attach a database to the webapp
```

### Readme

You should probably customise the README for your new project:

``` bash
cp README.template.md README.md  # Overwrite this README with the template
vim README.md                    # Customise the README
```

### Templates and stylesheets

Edit template and stylesheets:

``` bash
vim template/index.html      # Edit the homepage
vim template/about.html      # Create a new page
vim static/sass/global.scss  # Edit the styles
```

Your changes should show immediately. E.g. the above `about.html` page should be
immediately available at <http://0.0.0.0:8090/about>.

### Error pages

You will probably want to make your error pages look prettier:

``` bash
vim templates/error/404.html  # Customise the 404 page
vim templates/error/500.html  # Customise the 500 page
```

### Production settings

The default provided `webapp/settings.py` is written to facilitate overriding
of the `DEBUG` and `SECRET_KEY` settings.

#### Debug

The `DEBUG` setting will default to `false` (ready for production) unless
it's overridden by the `DJANGO_DEBUG` environment variable (`./run` takes care
  of turning `DEBUG` on in development mode).

#### Secret key

The `SECRET_KEY` setting default to "no_secret" unless overridden with the
`SECRET_KEY` environment variable.

It doesn't matter that this is insecure initially, as none of the functionality
of the basic project uses the SECRET_KEY. However, you should change it when
you get the chance in case someone adds functionality that uses it in the
future.

Visit the
[secret key generator](http://www.miniwebtool.com/django-secret-key-generator/)
to generate a new key, and then use that secret key in production by setting
the `SECRET_KEY` environment variable.

Dependencies
---

Among the dependencies of this project are several modules which we,
the Ubuntu design team, have written ourselves:

- [django-template-finder-view](https://github.com/ubuntudesign/django-template-finder-view)
- [django-versioned-static-url](https://github.com/ubuntudesign/django-versioned-static-url)
- [django-static-root-finder](https://github.com/ubuntudesign/django-static-root-finder)
- [django-asset-server-url](https://github.com/ubuntudesign/django-asset-server-url)

License
---

The content of this project is licensed under the [Creative Commons Attribution-ShareAlike 4.0 International license](https://creativecommons.org/licenses/by-sa/4.0/), and the underlying code used to format and display that content is licensed under the [LGPLv3](http://opensource.org/licenses/lgpl-3.0.html) by [Canonical Ltd](http://www.canonical.com/).

---

With ♥ from [Canonical]((http://www.canonical.com/)).
