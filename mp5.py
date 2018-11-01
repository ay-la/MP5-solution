"""Part of the stretch goal solution."""


import unicodedata


def string_compare(s1: str, s2: str) -> bool:
    """Performs a very loose string comparison.
    
    This function performs a string comparison that is case-insensitive and
    Unicode normalization-insensitive."""
    s1_for_comp = unicodedata.normalize("NFC", s1.casefold())
    s2_for_comp = unicodedata.normalize("NFC", s2.casefold())
    return s1_for_comp == s2_for_comp
