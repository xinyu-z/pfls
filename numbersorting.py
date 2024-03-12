numbers = [3, 1, 6, 4, 3, 8, 1, 1, 1, 2]
uniques = []

def countCounter(arrayofNum):
    arrayofNum = sorted(arrayofNum)
    uniques = []
    for number in arrayofNum:
        if number not in uniques:
            uniques.append(number)

    uniques = sorted(uniques)

    counts = []

    for unique in uniques:
        count = 0
        for number in arrayofNum:
            if number == unique:
                count += 1
        counts.append(count)
    #print(uniques)
    #print(counts)

    print(dict(zip(uniques, counts))) #this pairs the uniques and counts as a dictionary. Remember to tell zip what type of object you want zip to be


countCounter (numbers)

#function to calculate the area of triangles
def triangleArea(a,b):
    print(0.5 * a * b)
    return 0.5 * a * b
triangleArea(3,4)

#difference between return and print:

def doubleNumber(n):
    print(2*n)

doubleNumber(triangleArea(3,4))
# the above line would not run because python won't be able to access the value of triangleArea
# use "return" instead of "print" so that the value of the triangleArea is stored in python
# and "return" does not need brackets because it's a control and not a function, anything after "return" that is in the same line will be returned
# but adding the brackets also works because sometimes what you need to return is longer than one line

    