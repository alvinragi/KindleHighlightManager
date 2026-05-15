import re
from datetime import datetime
from models.clippings import Clipping


def parse_clippings(file_path):
    """Parses the Kindle My clippings.txt file and returns a list of Clipping objects."""
    with open(file_path, "r", encoding="utf-8-sig") as file:
        content = file.read()

    # Split the content into individual clippings using the delimiter "=========="
    raw_clippings = content.split("==========")

    parsed_clippings = []

    for clipping in raw_clippings:
        clipping = clipping.strip()
        if not clipping:
            continue

        # Each clipping is expected to have a specific structure:
        lines = clipping.split("\n")

        metadata_line = lines[1]

        # Skip bookmarks as they don't contain text content
        if metadata_line.startswith("- Your Bookmark"):
            continue

        # Extract book title, author, page/location, date, and content
        book, author = extract_title(lines[0])
        page_or_loc = extract_page_or_location(metadata_line)
        datetime_str = extract_date(metadata_line)
        text_content = "\n".join(lines[3:])

        parsed_clippings.append(
            Clipping(
                book=book,
                author=author,
                page_or_location=page_or_loc,
                datetime=datetime_str,
                content=text_content
            )
        )

    return parsed_clippings

def extract_title(title):
    match = re.match(r"(.+)\s\((.+)\)", title.strip())
    if match:
        book = match.group(1)
        author = match.group(2)
    else:
        book = title
        author = "Unknown"
    return book, author

def extract_page_or_location(metadata):
    page_match = re.search(r"Page\s+(\d+)", metadata)
    loc_match = re.search(r"Location\s+([\d-]+)", metadata)

    # Prioritize page number if both are present, otherwise return location or empty string
    if page_match:
        return f"Page {page_match.group(1)}"
    elif loc_match:
        return f"Location {loc_match.group(1)}"
    else:
        return ""
    
def extract_date(metadata):
    date_match = re.search(r"Added on (.+)", metadata)
    raw_date = date_match.group(1) if date_match else ""
    return format_date(raw_date)
    
def format_date(raw_date):
    """Formats the raw date string from the clippings file into a more readable format."""
    if not raw_date:
        return ""
    dt = datetime.strptime(raw_date, "%A, %B %d, %Y %I:%M:%S %p")

    #Helper for the 'th', 'st', 'nd', 'rd' suffix
    day = dt.day
    suffix = "th" if 11 <= day <= 13 else {1: "st", 2: "nd", 3: "rd"}.get(day % 10, "th")
    
    formatted_date = dt.strftime(f"{day}{suffix} %b %Y, %-I:%M %p")
    return formatted_date