import warnings

from pyrep.backend import sim
from pyrep.const import ObjectType
from pyrep.errors import WrongObjectTypeError
from typing import Any, Dict, List, Tuple, Union


class Collision(object):
    """
    a collision object
    """

    def __init__(self, name_or_handle: Union[str, int]):
        if isinstance(name_or_handle, int):
            self._handle = name_or_handle
        else:
            self._handle = sim.simGetCollisionHandle(name_or_handle)

    def read_collision(self) -> bool:
        return sim.simReadCollision(self._handle)
