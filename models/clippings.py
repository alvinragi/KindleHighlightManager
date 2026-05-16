from dataclasses import dataclass
from datetime import datetime

@dataclass
class Clipping:
    book: str
    author: str
    content: str
    page_or_location: str
    datetime: datetime