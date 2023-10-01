#!/usr/bin/env python3

"""
__init__.py: TODO: Headline...

TODO: Description...
"""

# Header.
__author__ = "Lennart Haack"
__email__ = "lennart-haack@mail.de"
__license__ = "GNU GPLv3"
__version__ = "0.0.2"
__build__ = "2023.2"
__date__ = "2023-09-28"
__status__ = "Prototype"

# Imports.
from .autostart import add_autostart  # noqa: F401
from .log import LogCount, add_handler, create_logger  # noqa: F401
