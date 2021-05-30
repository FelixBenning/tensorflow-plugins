from tensorflow.keras.optimizers import *
_GLOBALS_CACHE = list(globals().keys())
_ALL_CACHE = (g for g in _GLOBALS_CACHE if not g[0]=='_')

from itertools import chain
import importlib.metadata
import tensorflow as tf
from typing import Generator, Tuple

_PLUGINS = {
    plugin.attr : plugin.module for plugin in
    importlib.metadata.entry_points().get("tensorflow.optimizers", [])
}

__all__ = list(set(chain(_ALL_CACHE, _PLUGINS.keys())))

def __getattr__(name: str) -> Optimizer:
    return getattr(
        importlib.import_module(_PLUGINS[name]), 
        name
    )

def __dir__() -> list[str]:
    return list(set(chain(_GLOBALS_CACHE, __all__)))

def all_optimizers() -> Generator[Tuple[str, Optimizer], None, None]:
    return ((name, __getattr__(name)) for name in _PLUGINS.keys())

if __name__ == "__main__":
    opts = all_optimizers()
    pass
