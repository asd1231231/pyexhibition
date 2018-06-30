# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     main
   Description :
   date：          6/29/18
-------------------------------------------------
   Change Activity:
                   6/29/18:
-------------------------------------------------
"""
# Python standard library module
import asyncio
import sys
from pathlib import Path
# Python third party module
try:
    import uvloop
    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
except ImportError:
    pass
# Application custom module
sys.path.append(Path(__file__).absolute().parent.parent)
from app import run
_loop = asyncio.get_event_loop()
asyncio.ensure_future(run())
_loop.run_forever()
