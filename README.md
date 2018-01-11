# HTTP Server Template

[![Build Status](https://travis-ci.org/mschwager/py-httptemplate.svg?branch=master)](https://travis-ci.org/mschwager/py-httptemplate)
[![Coverage Status](https://coveralls.io/repos/github/mschwager/py-httptemplate/badge.svg?branch=master)](https://coveralls.io/github/mschwager/py-httptemplate?branch=master)

Something simple to base your next web server off of! This project makes heavy
use of [aiohttp](https://aiohttp.readthedocs.io/en/stable/), and Python 3's
`asyncio` functionality.

With this you can:

* Do asynchronous things, handle many connections, web scale!
* Build that blog you've been dreaming of... but with Python!
* Integrate with PostgreSQL via [aiopg](https://aiopg.readthedocs.io/en/stable/), or MySQL via [aiomysql](https://aiomysql.readthedocs.io/en/latest/). Do database-y things, maintain state!
* Avoid repetitive structuring of your CRUD apps. Base it off this template!
* Place it behind [nginx](https://www.nginx.com/). Load balance! Serve static content! Add HTTP headers! Use SSL/TLS!

# Installing

```
$ git clone https://github.com/mschwager/py-httptemplate.git
$ cd py-httptemplate
$ pipenv install
```

# Using

```
$ pipenv run python -m httptemplate --static
======== Running on http://127.0.0.1:8080 ========
(Press CTRL+C to quit)
...
```

# Development

You should install the development packages before starting development:

```
$ pipenv install --dev
```

## Testing

```
$ pipenv run nose2 --with-coverage
......
----------------------------------------------------------------------
Ran 6 tests in 0.086s

OK
```

## Linting

```
$ pipenv run flake8 src/httptemplate
```

## Debugging

You can run `pipenv shell` to spawn a shell within the virtualenv. Now you're
free to debug within the package's environment at you're leisure.
