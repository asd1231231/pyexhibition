# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     __main__
   Description :
   date：          6/29/18
-------------------------------------------------
   Change Activity:
                   6/29/18:
-------------------------------------------------
"""
# Python standard library module
from aiohttp import web


def init_app():
    """
    init_app
    :return: app_instance
    """
    app = web.Application()
    return app


async def run():
    """
    run_app_instance
    :return: None
    """
    app = init_app()
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, '0.0.0.0', 8080)
    await site.start()