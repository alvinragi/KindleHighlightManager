from utils.formatter import format_clipping

def export_clippings_to_text(sorted_clippings):    
    """Export the sorted clippings to a text file."""

    with open("my_kindle_highlights.txt", "w", encoding="utf-8") as file:
        # Iterate through the sorted clippings and write them to the file
        for book_clippings in sorted_clippings.values():
            for clipping in book_clippings:
                file.write(format_clipping(clipping))