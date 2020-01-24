"""
MTGJSON CompiledList container
"""
from typing import Any, Dict, List

from .mtgjson_structures_obj import MtgjsonStructuresObject
from ..classes import MtgjsonMetaObject
from ..utils import to_camel_case


class MtgjsonCompiledListObject:
    """
    CompiledList container
    """

    files: List[str]
    meta: MtgjsonMetaObject

    def __init__(self) -> None:
        self.files = MtgjsonStructuresObject().get_compiled_list_files()
        self.meta = MtgjsonMetaObject()

    def for_json(self) -> Dict[str, Any]:
        """
        Support json.dumps()
        :return: JSON serialized object
        """
        return {
            to_camel_case(key): value
            for key, value in self.__dict__.items()
            if not key.startswith("__") and not callable(value)
        }
