"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    
    for x in items:
        if(frequencies.get(x) == None):
            frequencies[x]=1
        else:
            frequencies[x]=frequencies.get(x)+1

    return frequencies

# print("enter values (strings) separated by commas: ")

items =['0', 4,4,'4','d','d','e',0,'a','d','4']# thinglist = sorted([str(value) for value in input().split(",")])
print(frequencies(items))