from .tamppa_code_mem import mem_parse
from .tamppa_code_tim import tim_parse

from ._version import get_versions

__version__ = get_versions()["version"]
del get_versions

from . import _version
__version__ = _version.get_versions()['version']
