from dataclasses import dataclass
from typing import Optional


@dataclass
class Clipping:
    book: str
    author: str
    content: str
    page_or_location: str
    datetime: str