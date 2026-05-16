from utils.exporter import export_clippings_to_text
from utils.parser import parse_clippings
from utils.sorter import group_and_sort_clippings


clippings = parse_clippings("sample_clippings.txt")
sorted_clippings = group_and_sort_clippings(clippings)
export_clippings_to_text(sorted_clippings)
