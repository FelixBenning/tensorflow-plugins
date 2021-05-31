import importlib
from importlib.metadata import EntryPoint

from collections.abc import Mapping, Sequence, Iterator

from typing import TypeVar, Generic

T = TypeVar("T")

class LazyClassMapping(Mapping, Generic[T]):
    def __init__(self, entrypoints:Sequence[EntryPoint]) -> None:
        self._class_mapping = {e.attr: e.module for e in entrypoints}

    def __getitem__(self, key: str) -> T:
        return getattr(
            importlib.import_module(self._class_mapping[key]),
            key
        )
    
    def __iter__(self) -> Iterator[tuple[str, T]]:
        return iter(self._class_mapping.keys())
    
    def __len__(self) -> int:
        return len(self._class_mapping) 
    
    def __repr__(self) -> str:
        return self.__class__.__name__ + f"({repr(self._class_mapping)})"
    
    def __str__(self) -> str:
        return str(self._class_mapping)
    