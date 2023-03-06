# Unofficial Docker image of Telegram Bot API

.. danger::
    This version is still in development!

.. image:: https://img.shields.io/pypi/l/aiogram.svg?style=flat-square
    :target: https://opensource.org/licenses/MIT
    :alt: MIT License

.. image:: https://img.shields.io/pypi/status/aiogram.svg?style=flat-square
    :target: https://pypi.python.org/pypi/aiogram
    :alt: PyPi status

.. image:: https://img.shields.io/pypi/v/aiogram.svg?style=flat-square
    :target: https://pypi.python.org/pypi/aiogram
    :alt: PyPi Package Version

.. image:: https://img.shields.io/pypi/dm/aiogram.svg?style=flat-square
    :target: https://pypi.python.org/pypi/aiogram
    :alt: Downloads

.. image:: https://img.shields.io/pypi/pyversions/aiogram.svg?style=flat-square
    :target: https://pypi.python.org/pypi/aiogram
    :alt: Supported python versions

.. image:: https://img.shields.io/badge/dynamic/json?color=blue&logo=telegram&label=Telegram%20Bot%20API&query=%24.api.version&url=https%3A%2F%2Fraw.githubusercontent.com%2Faiogram%2Faiogram%2Fdev-3.x%2F.butcher%2Fschema%2Fschema.json&style=flat-square
    :target: https://core.telegram.org/bots/api
    :alt: Telegram Bot API

.. image:: https://img.shields.io/github/actions/workflow/status/aiogram/aiogram/tests.yml?branch=dev-3.x&style=flat-square
    :target: https://github.com/aiogram/aiogram/actions
    :alt: Tests

.. image:: https://img.shields.io/codecov/c/github/aiogram/aiogram?style=flat-square
    :target: https://app.codecov.io/gh/aiogram/aiogram
    :alt: Codecov

**aiogram** is a modern and fully asynchronous framework for
`Telegram Bot API <https://core.telegram.org/bots/api>`_ written in Python 3.8 using
`asyncio <https://docs.python.org/3/library/asyncio.html>`_ and
`aiohttp <https://github.com/aio-libs/aiohttp>`_.

Make your bots faster and more powerful!

Documentation:
 - 🇺🇸 `English <https://docs.aiogram.dev/en/dev-3.x/>`_
 - 🇺🇦 `Ukrainian <https://docs.aiogram.dev/uk_UA/dev-3.x/>`_


.. danger::

    **Breaking News:**

    *aiogram* 3.0 has breaking changes.

    It breaks backward compatibility by introducing new breaking changes!

Features
========

- Asynchronous (`asyncio docs <https://docs.python.org/3/library/asyncio.html>`_, :pep:`492`)
- Has type hints (:pep:`484`) and can be used with `mypy <http://mypy-lang.org/>`_
- Supports `PyPy <https://www.pypy.org/>`_
- Supports `Telegram Bot API 6.5 <https://core.telegram.org/bots/api>`_ and gets fast updates to the latest versions of the Bot API
- Telegram Bot API integration code was `autogenerated <https://github.com/aiogram/tg-codegen>`_ and can be easily re-generated when API gets updated
- Updates router (Blueprints)
- Has Finite State Machine
- Uses powerful `magic filters <https://docs.aiogram.dev/en/dev-3.x/dispatcher/filters/magic_filters.html#magic-filters>`
- Middlewares (incoming updates and API calls)
- Provides `Replies into Webhook <https://core.telegram.org/bots/faq#how-can-i-make-requests-in-response-to-updates>`_
- Integrated I18n/L10n support with GNU Gettext (or Fluent)


.. warning::

    It is strongly advised that you have prior experience working
    with `asyncio <https://docs.python.org/3/library/asyncio.html>`_
    before beginning to use **aiogram**.

    If you have any questions, you can visit our community chats on Telegram:

    - 🇺🇸 `@aiogram <https://t.me/aiogram>`_
    - 🇺🇦 `@aiogramua <https://t.me/aiogramua>`_
    - 🇺🇿 `@aiogram_uz <https://t.me/aiogram_uz>`_
    - 🇰🇿 `@aiogram_kz <https://t.me/aiogram_kz>`_
    - 🇷🇺 `@aiogram_ru <https://t.me/aiogram_ru>`_
    - 🇮🇷 `@aiogram_fa <https://t.me/aiogram_fa>`_
    - 🇮🇹 `@aiogram_it <https://t.me/aiogram_it>`_
    - 🇧🇷 `@aiogram_br <https://t.me/aiogram_br>`_


.. warning::
- 🇺🇿 `@aiogram_uz <https://t.me/aiogram_uz>`_
- 🇺🇿 `@aiogram_uz <https://t.me/aiogram_uz>`_
.. |beta badge| image:: https://img.shields.io/badge/-beta-orange
  :alt: Beta badge
