"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    
    for x in items:
        if(frequencies.get(str(x)) == None):
            frequencies[str(x)]=1
        else:
            frequencies[str(x)]=frequencies.get(str(x))+1

    return frequencies

items =['0', 4,4,'4','d','d','e',0,'a','d','4']
print(frequencies(items))