Static Django website blueprint
===

A stripped-down blueprint Django project to serving static templates directly.
It is intented as a basis for the Ubuntu design team's informational sites.

Much of Django's dynamic functionality (e.g. sessions, any database interation)
has been removed. URLs map directly to template locations, so creating a new
web page is as simple as creating a new template file.

While this project is public, you won't be able to use it out of the box unless
you have access to the private `django-fenchurch` plugin - which is currently
only accessible by members of Canonical. We have plans to change this soon.

Basic usage
---

Just clone the project and run the server:

``` bash
git clone https://github.com/ubuntudesign/static-django-blueprint.git
static-django-blueprint
make run     # Download containers and run the dev server
```

Now visit <http://0.0.0.0:8099>.

You can run the server on a custom port by specifying the `PORT` environment variable:

``` bash
PORT=8054 make run
```

Customisation
---

This project is intended to be forked and turned into a new project as follows:

### Customise Makefile

You should change the defaults in the [Makefile](Makefile) for the project name and the default port:

``` bash
# Makefile

ifeq ($(PORT),)
    PORT=8765  # Set a new default port
endif

PROJECT_NAME=my-new-project  # Set a new project name
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
vim template/index.html     # Edit the homepage
vim template/about.html     # Create a new page
vim static/css/global.scss  # Edit the styles
```

Your changes should show immediately. E.g. the above `about.html` page should be
immediately available at <http://0.0.0.0:8099/about>.

### Error pages

You will probably want to make your error pages look prettier:

``` bash
vim templates/error/404.html  # Customise the 404 page
vim templates/error/500.html  # Customise the 500 page
```

### Secret key

The app comes with the SECRET_KEY setting set to
"SECRET_KEY_INSECURE_PLACEHOLDER".

It doesn't matter that this is insecure initially, as none of the functionality
of the basic project uses the SECRET_KEY. However, you should change it when
you get the chance in case someone adds functionality that uses it in the
future.

Visit the
[secret key generator](http://www.miniwebtool.com/django-secret-key-generator/)
to generate a new key, and then set it in `webapp/settings.py` as follows:

``` python.py
# webapp/settings.py

SECRET_KEY = '!!!YOUR_NEW_SECRET_KEY_HERE!!!'
```

Dependencies
---

Among the dependencies of this project are several modules which we,
the Ubuntu design team, have written ourselves:

- django-fenchurch (private - soon to be open-sourced)
- [django-versioned-static-url](https://github.com/ubuntudesign/django-versioned-static-url)
- [django-static-root-finder](https://github.com/ubuntudesign/django-static-root-finder)
- [django-asset-server-url](https://github.com/ubuntudesign/django-asset-server-url)
