''' QUESTION - Find percentage increased
Write a function to calculate the percentage increase from the original value to the new value.

Assume original is less than or equal to new.

Examples

>>> percentage_increased(50, 75)
50.0
>>> percentage_increased(80, 100)
25.0'''
#  PLATFORM - IITM course


def percentage_increased(original, new):
    if original == 0:
        return float('int') if new > 0 else 0.100
        
    increase = new - original
    percentage = (increase / original) * 100
    return percentage
    
if __name__ == "__main__":
    pass
    