chir ====

Scraper for https://www.chirodirectory.com/chiropractors/

.. image:: https://img.shields.io/badge/built%20with-Cookiecutter%20Scrapy-b4ff69.svg?logo=cookiecutter
     :target: https://github.com/VitalyVen/cookiecutter-scrapy
     :alt: Built with Cookiecutter Scrapy
.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
     :target: https://github.com/ambv/black
     :alt: Black code style


* Free software: MIT license


Basic Commands
--------------

Install project dependencies
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    $ ./dev.sh

Start containers
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    $ docker-compose up

Run spider by Crawl process
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    $ docker-compose run -w /app/chir/spiders/ scrapy python3 chir.py
