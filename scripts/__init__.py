# -*- coding: utf-8 -*-
import pkgutil
from .base import Base
import inspect


# load classes subclass of BaseCrawler
classes = []
for loader, name, is_pkg in pkgutil.walk_packages(__path__):
    module = loader.find_module(name).load_module(name)
    for name, value in inspect.getmembers(module):
        globals()[name] = value
        if inspect.isclass(value) and issubclass(value, Base) and value is not Base \
                and not getattr(value, 'ignore', False):
            classes.append(value)
__all__ = __ALL__ = classes