# pyOstrom

<!-- [![PyPI version](https://badge.fury.io/py/pyOstrom.svg)](https://badge.fury.io/py/pyOstrom)  -->
<a href="https://github.com/ambv/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
<a href="https://github.com/ambv/black/blob/master/LICENSE"><img alt="License: MIT" src="https://black.readthedocs.io/en/stable/_static/license.svg"></a>

Python3 library for [Ostrom](https://www.ostrom.de/).

Get electricity price and consumption.

If you have a Smart meter you can see your consumption in real time.

Go to [developer.ostrom-api.io](https://developer.ostrom-api.io/) to get your API token.

## Disclaimer

This library is not affiliated with Ostrom. It is an unofficial library.
The source code is currently in a beta state and is not recommended for production use.

This library is based on the work of [pyTibber](https://github.com/Danielhiversen/pyTibber/tree/master/tibber)

## Install

```bash
pip3 install pyOstrom
```

## Example

```python
import ostrom.const
import ostrom
import asyncio


async def start():
  ostrom_connection = ostrom.Ostrom(ostrom.const.DEMO_TOKEN, user_agent="change_this")
  await ostrom_connection.update_info()
  print(ostrom_connection.name)

  home = ostrom_connection.get_homes()[0]
  await home.fetch_consumption_data()
  await home.update_info()
  print(home.address1)

  await home.update_price_info()
  print(home.current_price_info)

  # await ostrom_connection.close_connection()

loop = asyncio.run(start())
```

## Example realtime data

An example of how to subscribe to realtime data (Pulse/Watty):

```python
import asyncio
import aiohttp
import ostrom
import ostrom.const

def _callback(pkg):
    print(pkg)
    data = pkg.get("data")
    if data is None:
        return
    print(data.get("liveMeasurement"))


async def run():
    async with aiohttp.ClientSession() as session:
        ostrom_connection = ostrom.Ostrom(ostrom.const.DEMO_TOKEN, websession=session, user_agent="change_this")
        await ostrom_connection.update_info()
    home = ostrom_connection.get_homes()[0]
    await home.rt_subscribe(_callback)

    while True:
      await asyncio.sleep(10)

loop = asyncio.run(run())
```

The library is used as part of Home Assistant.
