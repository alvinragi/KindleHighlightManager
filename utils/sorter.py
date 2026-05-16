from collections import defaultdict
import datetime

def group_and_sort_clippings(clippings):
    """Groups clippings by book and sorts them by date within each book."""
    grouped = defaultdict(list)

    # group books
    for c in clippings:
        grouped[c.book].append(c)

    # sort inside each book
    for book in grouped:
        grouped[book].sort(
            key=lambda c: c.datetime or datetime.min
        )

    return dict(grouped)