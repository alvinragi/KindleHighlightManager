from models.clippings import Clipping

def format_clipping(clipping: Clipping)-> str:
    """Formats a Clipping object into a readable string format."""
    
    return f"""{clipping.book} ({clipping.author})
{clipping.datetime} | {clipping.page_or_location}

{clipping.content}
=====
"""