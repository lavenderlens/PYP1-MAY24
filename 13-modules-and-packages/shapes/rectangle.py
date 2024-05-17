'''rectangle module'''

def area(length, width):
    return length * width

def perimeter(length, width):
    return 2 * (length + width)

# supposing I had utility methods that i did not wish to export
def cms_to_inches(cms):
    return cms * 0.39

def inches_to_cms(inches):
    return inches * 2.54

__all__ = ["area", "perimeter"]
# narrows down the import * wildcard
# does not include these functions
# this pattern called revealing module pattern