#!/usr/bin/env python3

import unittest

import aiohttp_jinja2
import bs4
import jinja2

from uitemplate import application


class TestViews(unittest.TestCase):

    def setUp(self):
        self.application = application.get_application()
        self.env = aiohttp_jinja2.get_env(self.application)

    def render_template(self, template, context):
        template = self.env.get_template(template)
        text = template.render(context)
        soup = bs4.BeautifulSoup(text, "html.parser")

        return soup

    def test_index(self):
        header = "header"
        context = {"content_header": header}

        soup = self.render_template("index.html", context)
        result = soup.find("h1").get_text()

        self.assertEquals(result, header)

    def test_missing_context(self):
        context = {}

        with self.assertRaises(jinja2.exceptions.UndefinedError):
            self.render_template("index.html", context)

    def test_autoescape(self):
        context = {"content_header": "<script>alert(1);</script>"}

        soup = self.render_template("index.html", context)
        result = soup.find("h1").prettify()
        expected = "&lt;script&gt;alert(1);&lt;/script&gt;"

        self.assertIn(expected, result)

    def test_about(self):
        context = {}

        soup = self.render_template("about.html", context)
        result = soup.find("h1").get_text()
        expected = "About"

        self.assertEquals(result, expected)


if __name__ == "__main__":
    unittest.main()
