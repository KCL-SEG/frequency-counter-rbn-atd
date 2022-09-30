"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    print(items)
    # for i in range(len(items)):
    #     frequencies[items[i]]=items.count(items[i])
    for x in items:
        frequencies[x]=items.count(x)

    return frequencies

print("enter values (strings) separated by commas: ")
thinglist = sorted([str(value) for value in input().split(",")])
print(frequencies(thinglist))