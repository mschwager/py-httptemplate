#!/usr/bin/env python3

import unittest

from aiohttp import test_utils

from uitemplate import application


class TestApplication(test_utils.AioHTTPTestCase):

    async def get_application(self):
        return application.get_application()

    @test_utils.unittest_run_loop
    async def test_index_ok(self):
        response = await self.client.request('GET', '/')

        assert response.status == 200

    @test_utils.unittest_run_loop
    async def test_about_ok(self):
        response = await self.client.request('GET', '/about')

        assert response.status == 200


if __name__ == "__main__":
    unittest.main()
