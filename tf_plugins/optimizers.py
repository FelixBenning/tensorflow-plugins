_BUILTINS_CACHE = list(globals().keys())

# import existing optimizer namespace
from tensorflow.keras.optimizers import Optimizer, serialize, deserialize, get, schedules

# avoid polluting the globals namespace with helpers (see __all__ definition)
from tf_plugins.helper import LazyClassMapping as _LazyClassMapping
from importlib.metadata import entry_points as _entry_points
from itertools import chain as _chain

all_optimizers = _LazyClassMapping[Optimizer](
    _entry_points().get("tensorflow.optimizers", [])
)

def __getattr__(name: str) -> Optimizer:
    try:
        return all_optimizers[name]
    except KeyError as e:
        raise AttributeError(str(e)) from None

def __dir__() -> list[str]:
    return list(set(_chain(_BUILTINS_CACHE, __all__)))

__all__ = list(set(_chain(
    (g for g in globals().keys() if not g[0]=='_'), # default
    all_optimizers.keys() # additional
)))
