from models.clippings import Clipping

def format_clipping(clipping: Clipping)-> str:
    """Formats a Clipping object into a readable string format."""
    
    return f"""{clipping.book} ({clipping.author})
{format_date(clipping.datetime)} | {clipping.page_or_location}

{clipping.content}
=====
"""

def format_date(raw_date):
    """Formats the raw date string from the clippings file into a more readable format."""
    if not raw_date:
        return ""

    #Helper for the 'th', 'st', 'nd', 'rd' suffix
    day = raw_date.day
    suffix = "th" if 11 <= day <= 13 else {1: "st", 2: "nd", 3: "rd"}.get(day % 10, "th")
    
    formatted_date = raw_date.strftime(f"{day}{suffix} %b %Y, %-I:%M %p")
    return formatted_date