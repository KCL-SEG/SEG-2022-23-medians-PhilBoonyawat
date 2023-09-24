"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""
def getMedian(listIn):
    listIn.sort()
    length = len(listIn)
    print(length)
    if length % 2 == 0:
        median = (listIn[int(length/2 - 1)] + listIn[int(length/2)])/2
    else:
        median = listIn[int((length-1)/2)]
    return median

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break
print(getMedian(numbers))
