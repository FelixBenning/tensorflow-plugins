import importlib
from importlib.metadata import EntryPoint
from tensorflow.keras.optimizers import Optimizer

from collections.abc import Mapping, Sequence, Iterator


class LazyClassMapping(Mapping):
    def __init__(self, entrypoints:Sequence[EntryPoint]) -> None:
        self._class_mapping = {e.attr: e.module for e in entrypoints}

    def __getitem__(self, key: str) -> Optimizer:
        return getattr(
            importlib.import_module(self._class_mapping[key]),
            key
        )
    
    def __iter__(self) -> Iterator[tuple[str, Optimizer]]:
        return iter(self._class_mapping.keys())
    
    def __len__(self) -> int:
        return len(self._class_mapping) 