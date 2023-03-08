# LISTADO DE COMANDOS PARA MICROTIK 
   ![Badge en Desarollo](https://img.shields.io/badge/STATUS-EN%20DESAROLLO-green)
   ![Badge](https://img.shields.io/pypi/status/aiogram.svg?style=flat-square)
## Este manual introduce los comandos que son usados para realizar la siguientes funciones:

**Comandos Básicos (Disponibles desde directorio raíz)**:
 - `/?`: Visualización de ayuda (comandos disponibles desde la interfaz de MikroTik).
 - `file print`: Muestra archivos almacenados en el router.
 - `interface print`: Muestra datos de las interfaces disponibles (Incluye -> NAME, TYPE, ACTUAL-MTU, L2MTU , MAX-L2MTU, MAC-ADDRESS).
 - `ip address print`: Visualizar dirección IP, red e interfaz.
 - `interface bridge print`: Despliega datos de interface bridge.
 - `user print`: Muestra lista de usuarios, grupos y direcciones (Incluyendo LAST-LOGGED-IN).
 - `log print`: Imprime lista de logs del MT.
 - `tool profile`: Muestra el uso de CPU de los procesos en ejecución
 - `certificate print`: Permite visualizar datos del certificado (Name, fingerprint, etc).
 - `snmp print`: Despliega informacion sobre SNMP.
 - 
ip address: muestra y configura las direcciones IP en las interfaces de red.
ping: prueba la conectividad con una dirección IP.
traceroute: muestra la ruta tomada por los paquetes a una dirección IP.
route: muestra y configura las tablas de enrutamiento.
firewall: muestra y configura las reglas de firewall.
dhcp server: configura el servidor DHCP.
user: muestra y configura los usuarios y grupos de usuarios.
system: muestra y configura la configuración del sistema.
wireless: configura las interfaces inalámbricas y las redes inalámbricas.

**Comandos Avanzados (Disponibles desde /interface)**:
 - `/?`: Visualización de ayuda (comandos disponibles desde /interface).
 - `print`: Imprime resumen de interfaz.
 - `ethernet print`: Imprime datos de interfaces ethernet.
 - `monitor-traffic`: Monitorea tráfico de la interfaz requerida.
 - `detect-internet print`: Muestra lista de interfaces de internet, LAN y WAN.


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




    - 🇺🇿 `@aiogram_uz <https://t.me/aiogram_uz>`_
- 🇺🇿 `@aiogram_uz <https://t.me/aiogram_uz>`_
    
.. warning::

    - 🇺🇿 `@aiogram_uz <https://t.me/aiogram_uz>`_
    - 🇺🇿 `@aiogram_uz <https://t.me/aiogram_uz>`_
    - 🇺🇿 `@aiogram_uz <https://t.me/aiogram_uz>`_
    
    - 🇺🇿 `@aiogram_uz <https://t.me/aiogram_uz>`_
    
    
- 🇺🇿 `@aiogram_uz <https://t.me/aiogram_uz>`_
- 🇺🇿 `@aiogram_uz <https://t.me/aiogram_uz>`_
.. |beta badge| image:: https://img.shields.io/badge/-beta-orange
  :alt: Beta badge
