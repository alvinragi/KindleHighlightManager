from utils.parser import parse_clippings
from utils.formatter import format_clipping

clippings = parse_clippings("sample_clippings.txt")

# Write the formatted clippings to a new text file
with open("my_kindle_highlights.txt", "w", encoding="utf-8") as file:
    for clipping in clippings:
        file.write(format_clipping(clipping))